from pydantic import BaseModel as PydanticBaseModel
from typing import List, Any, Dict,Union
from structures import Embedding,Word, Symbol,Phrase

class ModifiedBaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True



class EmbeddingRequest(ModifiedBaseModel):
    stemmed_words: List[str]
    tokens: dict
class EmbeddingResponse(ModifiedBaseModel):
    embeddings: List[Embedding]


class ResponseRequest(ModifiedBaseModel):
    text: str
    context: Dict[str, Any]
    
    
class PreprocessRequest(ModifiedBaseModel):
    text: str

class PreprocessResponse(ModifiedBaseModel):
    raw_words: List[str]
    tokens: Dict[str, Any]
    
    
class GetSymbolRequest(ModifiedBaseModel):
    lexeme_id: int
    
class GetSymbolResponse(ModifiedBaseModel):
    symbol: Symbol
    
class GetWordRequest(ModifiedBaseModel):
    word_text: str
    stemmed: bool = False
    

class GetWordResponse(ModifiedBaseModel):
    word:Union[Word,None]
    
class GetSimilarWordRequest(ModifiedBaseModel):
    embedding: Embedding
    
class GetAllPhrasesResponse(ModifiedBaseModel):
    phrases: List[Phrase]
    
class GetTranscriptionRequest(ModifiedBaseModel):
    audio_data: bytes

class GetTranscriptionResponse(ModifiedBaseModel):
    transcription: str
    






