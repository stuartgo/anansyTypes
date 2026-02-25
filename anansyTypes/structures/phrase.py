from typing import List, Any
from pydantic import model_validator
from pydantic_core import core_schema
import torch

from .lexeme import Lexeme
from .embedding import Embedding
import numpy as np


class NoEmbeddingPhrase(Lexeme):
    def __init__(self, id: str, content: str,original_content: str):
        #initialised with empty embedding
        super().__init__(id=id, content=content, embedding=Embedding(data=torch.tensor([])), original_content=original_content)

    @classmethod
    def from_dict(cls, data: dict) -> "NoEmbeddingPhrase":
        return cls(
            id=data["id"],
            content=data["content"],
            original_content=data["original_content"],
        )
    @model_validator(mode="before")
    @classmethod
    def ignore_embedding(cls, values):
        # Remove embedding from incoming data
        values.pop("embedding", None)
        return values

class Phrase(Lexeme):

    @classmethod
    def from_dict(cls, data: dict) -> "Phrase":
        return cls(
            id=data["id"],
            content=data["content"],
            original_content=data["original_content"],
            embedding=Embedding.from_dict(data["embedding"]),
        )

    @classmethod
    def from_noembeddingphrase(
        cls, phrase: NoEmbeddingPhrase, embedding: Embedding
    ) -> "Phrase":
        return cls(
            id=phrase.id,
            content=phrase.content,
            original_content=phrase.original_content,
            embedding=embedding,
        )
