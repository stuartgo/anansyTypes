from typing import Any
import torch
from pydantic import BaseModel
from pydantic_core import core_schema
from typing_extensions import Annotated


class TensorPydantic:
    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        def validate(v: Any):
            if isinstance(v, torch.Tensor):
                return v
            if isinstance(v, list):
                return torch.tensor(v, dtype=torch.float32)
            raise TypeError(f"Cannot convert {type(v)} to torch.Tensor")

        return core_schema.json_or_python_schema(
            json_schema=core_schema.list_schema(core_schema.any_schema()),
            python_schema=core_schema.no_info_plain_validator_function(validate),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda t: t.detach().cpu().tolist()
            ),
        )


Tensor = Annotated[torch.Tensor, TensorPydantic]


class Embedding(BaseModel):
    data: Tensor