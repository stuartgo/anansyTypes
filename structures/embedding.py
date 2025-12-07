from __future__ import annotations
from dataclasses import dataclass
import torch


@dataclass(frozen=True)
class Embedding:
    data: torch.Tensor

    def __post_init__(self):
        if not isinstance(self.data, torch.Tensor):
            raise TypeError(f"data must be a torch.Tensor, got {type(self.data)}")

    def compare(self, other: Embedding) -> float:
        """
        Compare this embedding with another embedding.
        """
        raise NotImplementedError("compare method must be implemented")
