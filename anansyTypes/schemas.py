from pydantic import BaseModel as PydanticBaseModel
from typing import List, Any, Dict,Union
from structures import Embedding,Word, Symbol,Phrase



class EmbedRequest(PydanticBaseModel):
    stemmed_words: List[str]
    tokens: dict
class EmbeddingResponse(PydanticBaseModel):
    embeddings: List[Embedding]


class ResponseRequest(PydanticBaseModel):
    text: str
    context: Dict[str, Any]
    
    
class PreprocessRequest(PydanticBaseModel):
    text: str

class PreprocessResponse(PydanticBaseModel):
    raw_words: List[str]
    tokens: Dict[str, Any]
    
    
class GetSymbolRequest(PydanticBaseModel):
    lexeme_id: int
    
class GetSymbolResponse(PydanticBaseModel):
    symbol: Symbol
    
class GetWordRequest(PydanticBaseModel):
    word_text: str
    stemmed: bool = False
    

class GetWordResponse(PydanticBaseModel):
    word:Union[Word,None]
    
class GetSimilarWordRequest(PydanticBaseModel):
    embedding: Embedding
    
class GetAllPhrasesResponse(PydanticBaseModel):
    phrases: List[Phrase]
    






