from functools import partial
import warnings
from scipy.optimize import minimize, root_scalar


def find_minimum(func, grad=None, start=0, gtol=1e-5):
    minimum = minimize(func, start, jac=grad, method="BFGS", options={"gtol": gtol})
    return minimum.x[0], minimum.fun


def find_root_scipy(func, start):
    minimization_objective = partial(func, gradient=False)
    return root_scalar(minimization_objective, x0=start, x1=start*1.3).root


def find_root(func,
              start,
              maxiters=50,
              threshold=1e-3,
              positive_threshold=1e-9,
              gradient_threshold=1e-3):
    t_current = t_new = start
    for _ in range(maxiters):
        fx, fprimex = func(t_current)
        while abs(fprimex) < gradient_threshold:  # numerical purposes
            t_current *= 2  # TODO find better option
            fx, fprimex = func(t_current)
        t_new = t_current - fx / fprimex
        if abs(t_new - t_current) / t_current < threshold:
            return t_new
        t_current = t_new
    warnings.warn("Max newton iterations reached.")
    return t_new