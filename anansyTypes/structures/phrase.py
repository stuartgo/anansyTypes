from typing import List, Any
from pydantic_core import core_schema

from .lexeme import Lexeme
from .embedding import Embedding


class Phrase(Lexeme):
    def __init__(self, id: int, content: str, embedding: Embedding):
        self.id = id
        self._content = content
        self._embedding = embedding

    @property
    def content(self) -> str:
        return self._content

    @property
    def embedding(self) -> Embedding:
        return self._embedding

    @classmethod
    def from_dict(cls, data: dict) -> "Phrase":
        return cls(
            id=data["id"],
            content=data["content"],
            embedding=Embedding.from_dict(data["embedding"]),
        )
        
        
class NoEmbeddingPhrase():
    def __init__(self, id: int, content: str):
        self.id = id
        self._content = content

    @property
    def content(self) -> str:
        return self._content


    @classmethod
    def from_dict(cls, data: dict) -> "Phrase":
        return cls(
            id=data["id"],
            content=data["content"]
        )