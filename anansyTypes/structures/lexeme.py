from abc import ABC, abstractmethod
from typing import List, Union
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
    @abstractmethod
    def embedding(self) -> Embedding:
        """Embedding(s) associated with the lexeme."""
        pass
    
    
    
