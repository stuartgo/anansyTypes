from typing import List, Any
from pydantic import model_validator
from pydantic_core import core_schema
import torch

from .lexeme import Lexeme
from .embedding import Embedding
import numpy as np


class Phrase(Lexeme):

    @classmethod
    def from_dict(cls, data: dict) -> "Phrase":
        return cls(
            id=data["id"],
            content=data["content"],
            original_content=data["original_content"],
            embedding=Embedding.from_dict(data["embedding"]),
        )
