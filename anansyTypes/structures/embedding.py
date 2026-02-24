from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from pydantic_tensor import Tensor
import torch
from typing import Any, Literal


@dataclass(frozen=True)
class Embedding:
    data: Tensor[torch.Tensor | np.ndarray[Any], tuple, Literal["int64"]]

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
    def from_dict(cls, data: dict) -> "Embedding":
        return cls(data=np.array(data["data"], dtype=np.float32))

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        from pydantic_core import core_schema
        
        def validate_embedding(value):
            if isinstance(value, cls):
                return value
            if isinstance(value, dict):
                return cls.from_dict(value)
            raise ValueError(f"Cannot convert {type(value)} to Embedding")
        
        python_schema = core_schema.with_info_plain_validator_function(
            lambda value, _: validate_embedding(value),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: {"data": x.data.tolist()},
                when_used="json",
            ),
        )
        
        return core_schema.json_or_python_schema(
            json_schema=core_schema.typed_dict_schema({
                'data': core_schema.typed_dict_field(core_schema.list_schema())
            }),
            python_schema=python_schema,
        )

