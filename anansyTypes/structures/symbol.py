from dataclasses import dataclass
from typing import Optional
import numpy as np
from pydantic_tensor import Tensor
from typing import Any, Literal
import torch
@dataclass
class Symbol:
    id: int
    label: str
    image: Tensor[ np.ndarray[Any, Any],tuple, Literal["int32", "int64"]]

