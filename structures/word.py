from .lexeme import Lexeme
from .embedding import Embedding


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
