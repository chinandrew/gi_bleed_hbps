import numpy as np


def draw_velocity(d, unit_v=False):
    if unit_v:
        v = np.random.normal(size=d)
        return v / np.linalg.norm(v)
    else:
        return np.random.normal(size=d)


def draw_inertia():
    return np.random.exponential()


def move_position(x, v, t):
    return x + t * v


def reflect_velocity(v, gradient):
    """Reflect v off plane orthogonal to gradient"""
    return v - 2 * (gradient @ v) / (gradient @ gradient) * gradient


def negate_tuple(x):
    return -x[0], -x[1]


def perturb_velocity(v, axis, sd=0.1):
    axis = axis / np.sqrt(sum(axis**2))
    vp = v - sum(v * axis) * axis
    norm_vp = np.sqrt(sum(vp**2))
    perturb_center = vp
    vp_rotated = perturb_center + np.random.normal(0, sd, len(vp))
    vp_rotated = vp_rotated - sum(vp_rotated * axis) * axis
    vp_rotated = norm_vp / np.sqrt(sum(vp_rotated ** 2)) * vp_rotated
    v_rotated = (v - vp) + vp_rotated
    return v_rotated


def quadratic_root_approx(minx, miny, x2, y2):
    return x2 + np.sqrt(-miny*(x2-minx)**2/(y2-miny))
