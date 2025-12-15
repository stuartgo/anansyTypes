from pydantic import BaseModel as PydanticBaseModel
from typing import List, Any, Dict, Optional,Union


from .structures import Embedding,Word, Symbol,Phrase,NoEmbeddingPhrase
from pydantic import field_validator, ConfigDict
from pydantic_tensor import Tensor
import torch
from typing import Any, Literal
class ModifiedBaseModel(PydanticBaseModel):
    pass
    #model_config = ConfigDict(arbitrary_types_allowed=True)


class EmbeddingRequest(ModifiedBaseModel):
    stemmed_words: List[str]
    tokens: dict
    word_ids: List[int]

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
    word_ids: List[int]

class GetSymbolRequest(ModifiedBaseModel):
    lexeme_id: int

class GetSymbolResponse(ModifiedBaseModel):
    symbol: Optional[Symbol]

class GetWordRequest(ModifiedBaseModel):
    word_text: str
    stemmed: bool = False

class GetWordResponse(ModifiedBaseModel):
    word: Optional[Word]

class GetSimilarWordRequest(ModifiedBaseModel):
    embedding: Embedding

class GetAllPhrasesResponse(ModifiedBaseModel):
    phrases: List[NoEmbeddingPhrase]

class GetTranscriptionRequest(ModifiedBaseModel):
    audio_data: bytes

class GetTranscriptionResponse(ModifiedBaseModel):
    transcription: str







