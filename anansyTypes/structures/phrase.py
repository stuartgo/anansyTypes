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
        from pydantic_core import core_schema
        
        return core_schema.no_info_after_validator_function(
            lambda x: x if isinstance(x, cls) else cls(**x),
            core_schema.typed_dict_schema(
                {
                    'id': core_schema.typed_dict_field(handler.generate_schema(int)),
                    'content': core_schema.typed_dict_field(handler.generate_schema(str)),
                    'embedding': core_schema.typed_dict_field(handler.generate_schema(Embedding)),
                }
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: {
                    'id': x.id,
                    'content': x.content,
                    'embedding': x.embedding
                },
                when_used='json',
            ),
        )

