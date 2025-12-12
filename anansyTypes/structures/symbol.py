from dataclasses import dataclass
from typing import Any
import numpy as np
from pydantic_tensor import Tensor
from typing import Any, Literal
from pydantic_core import core_schema


@dataclass
class Symbol:
    id: int
    label: str
    image: Tensor[np.ndarray[Any, Any], tuple, Literal["int32", "int64"]]

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        def serialize(value: "Symbol") -> dict:
            serialized_image = handler(
                source_type=value.image.__class__, value=value.image
            )

            return {"id": value.id, "label": value.label, "image": serialized_image}

        return core_schema.json_or_python_schema(
            python_schema=handler(cls),
            json_schema=core_schema.plain_serializer_function_ser_schema(
                serialize, return_type=dict, when_used="json"
            ),
        )
