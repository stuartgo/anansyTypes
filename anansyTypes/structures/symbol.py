from dataclasses import dataclass
from typing import Any
import numpy as np
from pydantic import BaseModel
from pydantic_tensor import Tensor
from typing import Any, Literal
from pydantic_core import core_schema
import base64


class Symbol(BaseModel):
    id: int
    label: str
    image: str  # Base64-encoded PNG image data


    def from_dict(cls, data: dict) -> "Symbol":
        return cls(
            id=data["id"],
            label=data["label"],
            image=data["image"],
        )