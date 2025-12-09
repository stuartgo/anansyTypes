from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Embedding:
    data: np.ndarray

    def __post_init__(self):
        if not isinstance(self.data, np.ndarray):
            raise TypeError(f"data must be a numpy.ndarray, got {type(self.data)}")

    def compare(self, other: Embedding) -> float:
        """
        Compare this embedding with another embedding.
        """
        raise NotImplementedError("compare method must be implemented")
