from .hbps_dynamics import HBPSDynamics


class HBPSSampler:

    @staticmethod
    def generate_next_state(f, x, v, inertia, t):
        logp = f(x, loglik_only=True)[0]
        first_bounce_time = HBPSDynamics.next_bounce_time(f, None, x, v, inertia, -logp)
        output = HBPSDynamics.advance(f, t, x, v, inertia, first_bounce_time, previous_logp=logp)
        return output[0], {"num_bounces": output[-1]}
