import numpy as np

from .dynamics import draw_velocity, move_position, reflect_velocity, negate_tuple, quadratic_root_approx
from .hbps_dynamics import HBPSDynamics
from .optimization import find_root, find_minimum


class BPSSampler:

    def __init__(self, f):
        self.f = f

    def generate_next_state(self, x, v, t, refresh_rate, return_velo=False, unit_v=False):
        """Numerically search for first bounce time."""
        total_time = 0
        num_bounces = 0
        while total_time < t:
            tau_bounce = self.find_next_bounce(x, v)
            tau_ref = self.draw_refresh_time(refresh_rate)
            if t - total_time < min(tau_bounce, tau_ref):
                x = move_position(x, v, t - total_time)
                return x, num_bounces if not return_velo else (x,v, num_bounces)
            elif tau_bounce < tau_ref:
                x = move_position(x, v, tau_bounce)
                v = reflect_velocity(v, -self.f(x)[1])
            else:
                x = move_position(x, v, tau_ref)
                v = draw_velocity(len(x), unit_v)
            num_bounces += 1
            total_time += min(tau_bounce, tau_ref)

    def find_next_bounce(self, x, v, maxiters=50, threshold=1e-4):
        xm, ym = self.find_tau_star(x, v)
        tau_star = max(xm, 0)
        Uxvs = -self.f(x + v * tau_star, loglik_only=True)[0]
        V = np.random.random()
        logV = np.log(V)
        def poisprocess(t, gradient=True):
            if gradient:
                Uxvt, gUxvt = negate_tuple(self.f(x + v * t))
                return Uxvt - Uxvs + logV, v @ gUxvt
            else:  # TODO remove redundancy here with taustar calc
                return -self.f(x + v * t, loglik_only=True)[0] - Uxvs + logV
        if np.isclose(xm, 0):  # if minimum too close to 0, choose different second point for approximation
            x2 = 0.01
            start = tau_star + quadratic_root_approx(xm, logV, x2, -self.f(x+v*x2, loglik_only=True)[0]-ym+logV)
        else:
            Ux = -self.f(x, loglik_only=True)[0]
            start = tau_star + quadratic_root_approx(xm, logV, 0, Ux-ym+logV)
        rt = find_root(poisprocess, start, maxiters, threshold)
        return rt

    def find_tau_star(self, x, v):
        def trajectory(t):
            return -self.f(x + v * t, loglik_only=True)[0]
        def trajectory_gradient(t):
            return -self.f(x + v * t)[1] @ v
        return find_minimum(trajectory, trajectory_gradient)

    @staticmethod
    def draw_refresh_time(rate):
        return np.random.exponential(1 / rate)

