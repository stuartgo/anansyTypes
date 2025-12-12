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
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        def serialize(value: Phrase) -> dict:
            return {
                "id": value.id,
                "content": value.content,
                "embedding": value.embedding.data.tolist(),
            }

        return core_schema.no_info_after_validator_function(
            lambda x: x,
            core_schema.is_instance_schema(cls),
            serialization=core_schema.plain_serializer_function_ser_schema(
                serialize, return_type=dict, when_used="json"
            ),
        )
