from dataclasses import dataclass, field

import numpy as np


@dataclass
class Event:
    time: float
    type: str
    constraint_idx: float = -1
    constraint_plane: np.ndarray = field(default_factory=lambda: np.array([]))