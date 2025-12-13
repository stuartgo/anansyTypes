from .lexeme import Lexeme
from typing import Any
from .embedding import Embedding
from pydantic_core import core_schema


class Word(Lexeme):
    def __init__(self, word_id: int, content: str, embedding: Embedding):
        self.id = word_id
        self._content = content
        self._embedding = embedding

    @property
    def content(self) -> str:
        return self._content

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
        )

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        from pydantic_core import core_schema

        def validate_word(value):
            if isinstance(value, cls):
                return value
            if isinstance(value, dict):
                return cls.from_dict(value)
            raise ValueError(f"Cannot convert {type(value)} to Word")

        return core_schema.with_info_plain_validator_function(
            lambda value, _: validate_word(value),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: {
                    "id": x.id,
                    "content": x.content,
                    "embedding": {"data": x.embedding.data.tolist()},
                },
                when_used="json",
            ),
        )
