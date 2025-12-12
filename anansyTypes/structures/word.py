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
        def serialize(value: 'Word') -> dict:
            serialized_embedding = handler(source_type=value.embedding.__class__, value=value.embedding)
            
            return {
                'id': value.id,
                'content': value.content, 
                'embedding': serialized_embedding
            }
            
        return core_schema.json_or_python_schema(
            python_schema=core_schema.is_instance_schema(cls),
            json_schema=core_schema.plain_serializer_function_ser_schema(
                serialize, return_type=dict, when_used='json'
            ),
        )
