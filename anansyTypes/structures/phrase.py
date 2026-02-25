from typing import List, Any
from pydantic_core import core_schema

from .lexeme import Lexeme
from .embedding import Embedding
import numpy as np


class NoEmbeddingPhrase(Lexeme):
    def __init__(self, id: str, content: str):
        super().__init__(id=id, content=content, embedding=None)

    @property
    def embedding(self):
        return None

class Phrase(Lexeme):

    @classmethod
    def from_dict(cls, data: dict) -> "Phrase":
        return cls(
            id=data["id"],
            content=data["content"],
            embedding=Embedding.from_dict(data["embedding"]),
        )

    @classmethod
    def from_noembeddingphrase(
        cls, phrase: NoEmbeddingPhrase, embedding: Embedding
    ) -> "Phrase":
        return cls(
            id=phrase.id,
            content=phrase.content,
            embedding=embedding,
        )
