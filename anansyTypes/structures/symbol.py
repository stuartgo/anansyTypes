from dataclasses import dataclass
from typing import Any
import numpy as np
from pydantic_tensor import Tensor
from typing import Any, Literal
from pydantic_core import core_schema
import base64


@dataclass
class Symbol:
    id: int
    label: str
    image: np.ndarray 

    @classmethod
    def from_dict(cls, data: dict) -> "Symbol":
        if isinstance(data["image"], str):
            # Decode base64 to numpy array
            image_bytes = base64.b64decode(data["image"])
            image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        else:
            image_array = np.array(data["image"], dtype=np.uint8)
        
        return cls(
            id=data["id"],
            label=data["label"],
            image=image_array,
        )

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        from pydantic_core import core_schema

        def validate_symbol(value):
            if isinstance(value, cls):
                return value
            if isinstance(value, dict):
                return cls.from_dict(value)
            raise ValueError(f"Cannot convert {type(value)} to Symbol")

        python_schema = core_schema.with_info_plain_validator_function(
            lambda value, _: validate_symbol(value),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: {
                    "id": x.id,
                    "label": x.label,
                    "image": base64.b64encode(x.image).decode("utf-8"),
                },
                when_used="json",
            ),
        )

        return core_schema.json_or_python_schema(
            json_schema=core_schema.typed_dict_schema(
                {
                    "id": core_schema.typed_dict_field(core_schema.int_schema()),
                    "label": core_schema.typed_dict_field(core_schema.str_schema()),
                    "image": core_schema.typed_dict_field(core_schema.str_schema()),
                }
            ),
            python_schema=python_schema,
        )
