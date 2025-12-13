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

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        from pydantic_core import core_schema

        def validate_phrase(value):
            if isinstance(value, cls):
                return value
            if isinstance(value, dict):
                return cls.from_dict(value)
            raise ValueError(f"Cannot convert {type(value)} to Phrase")

        return core_schema.with_info_plain_validator_function(
            lambda value, _: validate_phrase(value),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: {
                    "id": x.id,
                    "content": x.content,
                    "embedding": {"data": x.embedding.data.tolist()},
                },
                when_used="json",
            ),
        )
