from dataclasses import dataclass, field

import numpy as np


@dataclass
class State:
    x: np.ndarray
    v: np.ndarray
    inertia: float
    xprecv: float
    vprecv: float
    xprecx: float = None