import warnings
from functools import partial

import numpy as np

from .dynamics import move_position, reflect_velocity, quadratic_root_approx
from .optimization import find_root, find_minimum


class HBPSDynamics:

    def __init__(self):
        self.hamiltonian = None

    def compute_hamiltonian(self, logp, v, inertia):
        self.hamiltonian = -logp + inertia + v @ v / 2
        return self.hamiltonian

    @staticmethod
    def find_root_fallback(current_inertia):
        minimization_objective = partial(current_inertia, gradient=False)
        def grad(t):
            return current_inertia(t, gradient=True)[1]
        new_start = find_minimum(minimization_objective, grad, 1e-3)[0] * 2
        root = find_root(current_inertia, new_start)
        return root

    @staticmethod
    def find_root_with_start(current_inertia, start):
        root = find_root(current_inertia, start)
        return root

    @staticmethod
    def find_root_quadratic(current_inertia):
        minimization_objective = partial(current_inertia, gradient=False)
        def grad(t):
            return current_inertia(t, gradient=True)[1]
        xm, ym = find_minimum(minimization_objective, grad, 1e-3)
        if abs(xm) < 1e-7:
            x2 = 0.02 # if minimum too close to 0, choose different second point for approximation
            start = quadratic_root_approx(xm, ym, x2, minimization_objective(x2))
        else:
            start = quadratic_root_approx(xm, ym, 0, minimization_objective(0))
        start = start - xm if xm < 0 else start + xm
        rt = find_root(current_inertia, start)
        return rt

    @staticmethod
    def next_bounce_time(f, start, x, v, inertia, Ux):
        def current_inertia(t, gradient=True):
            if not gradient:
                logp, _ = f(x + v * t, loglik_only=True)
                fx = -logp - Ux - inertia
                return fx
            else:
                logp, grad = f(x + v * t)
                fx = -logp - Ux - inertia
                return fx, v @ -grad
        if start:  # assume at 0 inertia immediately after a bounce if a starting guess is provided
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("error")
                    next_bounce = HBPSDynamics.find_root_with_start(current_inertia, start)
                    assert next_bounce > 1e-9
            except (AssertionError, RuntimeWarning, UserWarning):
                next_bounce = HBPSDynamics.find_root_fallback(current_inertia)
        else:
            next_bounce = HBPSDynamics.find_root_quadratic(current_inertia)
        assert next_bounce > 1e-9
        return next_bounce

    @staticmethod
    def advance_rec(f, t, x, v, inertia, bounces, previous_logp=None,  direction=1, num_bounces=0):
        if previous_logp is None:
            previous_logp, _ = f(x, loglik_only=True)
        bounces = (bounces, 0, 0, 0) if isinstance(bounces, float) else bounces
        next_bounce, last_bounce = bounces[:2] if direction == 1 else bounces[2:]
        if t < next_bounce:
            x_new = move_position(x, v, direction * t)
            logp, _ = f(x_new, loglik_only=True)
            new_bounce = (next_bounce - t, last_bounce + t, *bounces[2:]) if \
                direction == 1 else (*bounces[:2], next_bounce - t, last_bounce + t)

            new_inertia = inertia - previous_logp + logp
            return x_new, v, logp, new_bounce, new_inertia, num_bounces
        else:
            x_new = move_position(x, v, direction * next_bounce)
            logp, grad = f(x_new)
            grad = -grad
            v_new = reflect_velocity(v, grad)
            new_bounce = HBPSDynamics.next_bounce_time(f, next_bounce + last_bounce,
                                                       x_new, direction * v_new, 0, -logp)
            num_bounces += 1
            new_bounce = (new_bounce, 0, *bounces[2:]) if \
                direction == 1 else (*bounces[:2], new_bounce, 0)
            return HBPSDynamics.advance(f, t - next_bounce, x_new, v_new, 0,  new_bounce, logp, direction,  num_bounces)

    @staticmethod
    def advance(f, t, x, v, inertia, bounces, previous_logp=None,  direction=1, num_bounces=0):
        if previous_logp is None:
            previous_logp, _ = f(x, loglik_only=True)
        bounces = (bounces, 0, 0, 0) if isinstance(bounces, float) else bounces
        total_time = 0
        next_bounce, last_bounce = bounces[:2] if direction == 1 else bounces[2:]
        while total_time < t:
            remaining_time = t - total_time
            if remaining_time < next_bounce:
                x_new = move_position(x, v, direction * remaining_time)
                logp, _ = f(x_new, loglik_only=True)
                new_bounce = (next_bounce - remaining_time, last_bounce + remaining_time, *bounces[2:]) if \
                    direction == 1 else (*bounces[:2], next_bounce - remaining_time, last_bounce + remaining_time)
                new_inertia = inertia - previous_logp + logp
                return x_new, v, logp, new_bounce, new_inertia, num_bounces
            else:
                total_time += next_bounce
                x = move_position(x, v, direction * next_bounce)
                logp, grad = f(x)
                grad = -grad
                v = reflect_velocity(v, grad)
                next_bounce = HBPSDynamics.next_bounce_time(f, next_bounce + last_bounce,
                                                           x, direction * v, 0, -logp)
                last_bounce = 0
                num_bounces += 1
