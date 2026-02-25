from typing import List, Any
from pydantic_core import core_schema

from .lexeme import Lexeme
from .embedding import Embedding
import numpy as np


class NoEmbeddingPhrase(Lexeme):
    @classmethod
    def from_dict(cls, data: dict) -> "NoEmbeddingPhrase":
        return cls(id=data["id"], content=data["content"],embedding=None)


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
