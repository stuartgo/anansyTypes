from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from pydantic_tensor import Tensor
import torch
from typing import Any, Literal
@dataclass(frozen=True)
class Embedding:
    data: Tensor[torch.Tensor | np.ndarray[Any, Any], Literal["int32", "int64"]]
    
    

    def __post_init__(self):
        if not isinstance(self.data, np.ndarray):
            raise TypeError(f"data must be a numpy.ndarray, got {type(self.data)}")

    def compare(self, other: Embedding) -> float:
        """
        Compare this embedding with another embedding.
        """
        raise NotImplementedError("compare method must be implemented")
