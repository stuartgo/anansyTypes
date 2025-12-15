from typing import List, Any
from pydantic_core import core_schema

from .lexeme import Lexeme
from .embedding import Embedding
import numpy as np

class Phrase(Lexeme):
    def __init__(self, id: int, content: str, embedding: Embedding):
        self.id = id
        self.content = content
        self.embedding = embedding

    @property
    def content(self) -> str:
        return self.content

    @property
    def embedding(self) -> Embedding:
        return self.embedding

    @classmethod
    def from_dict(cls, data: dict) -> "Phrase":
        return cls(
            id=data["id"],
            content=data["content"],
            embedding=Embedding.from_dict(data["embedding"]),
        )
        
        
class NoEmbeddingPhrase(Lexeme):
    def __init__(self, id: int, content: str):
        self.id = id
        self.content = content
        self.embedding=np.array([])  # Placeholder to avoid attribute errors
    @property
    def content(self) -> str:
        return self.content

    @classmethod
    def from_dict(cls, data: dict) -> "Phrase":
        return cls(
            id=data["id"],
            content=data["content"]
        )