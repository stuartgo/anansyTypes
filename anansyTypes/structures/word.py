from .lexeme import Lexeme
from typing import  Any
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
                    'embedding': x.embedding  # Let Pydantic serialize Embedding
                },
                when_used='json',
            ),
        )
