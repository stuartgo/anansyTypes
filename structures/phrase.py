from typing import List

from .lexeme import Lexeme
from .embedding import Embedding
from .word import Word


class Phrase(Lexeme):
    def __init__(self, id: int, content: str, embedding: Embedding):
        self.id = id
        self._content = content
        self._embedding = embedding
        
    @property
    def content(self) -> List[str]:
        return self._content

    @property
    def embedding(self) -> Embedding:
        return self._embedding
    
    def __str__(self):
        return self.content
    
    def __repr__(self):
        return self.__str__()