from abc import ABC, abstractmethod
from typing import List, Union, Any
from dataclasses import dataclass

from pydantic import BaseModel
from .embedding import Embedding

class Lexeme(BaseModel,ABC):
    id: int
    content: Union[str, List[str]]
    original_content: Union[str, List[str]]
    embedding: Embedding
    

    @classmethod
    def from_dict(cls, data: dict) -> "Lexeme":
        return cls(
            id=data["id"],
            content=data["content"],
            embedding=Embedding.from_dict(data["embedding"]),
            original_content=data["original_content"],
        )
    def __new__(cls, *args, **kwargs):
        if cls is Lexeme:
            raise TypeError("Lexeme cannot be instantiated, use a subclass instead")
        return super().__new__(cls)