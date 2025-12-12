from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from pydantic_tensor import Tensor
import torch
from typing import Any, Literal


@dataclass(frozen=True)
class Embedding:
    data: Tensor[torch.Tensor | np.ndarray[Any, Any], tuple, Literal["int32", "int64"]]

    def compare(self, other: Embedding) -> float:
        """
        Compare this embedding with another embedding.
        """
        if isinstance(self.data, np.ndarray) and isinstance(other.data, np.ndarray):
            # Simple example: L2 distance (Euclidean distance)
            return np.linalg.norm(self.data - other.data)

        # Fallback or error if not implemented for other types (e.g., torch.Tensor)
        raise NotImplementedError(
            "Comparison must be implemented for all supported data types."
        )