from .lexeme import Lexeme
from typing import Any
from .embedding import Embedding
from pydantic_core import core_schema


class Word(Lexeme):
    def __init__(self, word_id: int, content: str,original_content: str, embedding: Embedding):
        self.id = word_id
        self._content = content
        self._original_content = original_content
        self._embedding = embedding

    @property
    def content(self) -> str:
        return self._content

    @property
    def original_content(self) -> str:
        return self._original_content
    @property
    def embedding(self) -> Embedding:
        return self._embedding

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> "Word":
        return cls(
            word_id=data["id"],
            content=data["content"],
            embedding=Embedding.from_dict(data["embedding"]),
            original_content=data["original_content"],
        )
