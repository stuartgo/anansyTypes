from abc import ABC, abstractmethod
from typing import List, Union, Any
from dataclasses import dataclass
from .embedding import Embedding


@dataclass
class Lexeme(ABC):
    id: int

    @property
    @abstractmethod
    def content(self) -> Union[str, List[str]]:
        """Text content of the lexeme."""
        pass

    @property
    def embedding(self) -> Embedding:
        """Embedding(s) associated with the lexeme."""
        raise NotImplementedError("Embeddings are not supported") #added to allow for NoEmbeddingPhrase

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> "Lexeme":
        """Create instance from dictionary."""
        pass

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        from pydantic_core import core_schema

        def validate_lexeme(value):
            if isinstance(value, cls):
                return value
            if isinstance(value, dict):
                return cls.from_dict(value)
            raise ValueError(f"Cannot convert {type(value)} to {cls.__name__}")

        python_schema = core_schema.with_info_plain_validator_function(
            lambda value, _: validate_lexeme(value),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: {
                    "id": x.id,
                    "content": x.content,
                    "embedding": {"data": x.embedding.data.tolist()},
                },
                when_used="json",
            ),
        )

        return core_schema.json_or_python_schema(
            json_schema=core_schema.typed_dict_schema(
                {
                    "id": core_schema.typed_dict_field(core_schema.int_schema()),
                    "content": core_schema.typed_dict_field(core_schema.str_schema()),
                    "embedding": core_schema.typed_dict_field(
                        handler.generate_schema(Embedding)
                    ),
                }
            ),
            python_schema=python_schema,
        )
