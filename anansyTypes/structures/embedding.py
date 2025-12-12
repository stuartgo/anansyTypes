from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from pydantic_tensor import Tensor
from pydantic_core import core_schema
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

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        def serialize(value: "Embedding") -> dict:
            serialized_data = handler(source_type=value.data.__class__, value=value.data)
            return {
                'data': serialized_data
            }

        return core_schema.json_or_python_schema(
            python_schema=core_schema.dataclass_schema(cls),
            json_schema=core_schema.plain_serializer_function_ser_schema(
                serialize, when_used='json'
            ),
        )
