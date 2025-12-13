from pydantic import BaseModel as PydanticBaseModel
from typing import List, Any, Dict,Union
from .structures import Embedding,Word, Symbol,Phrase
from pydantic import field_validator, ConfigDict
from pydantic_tensor import Tensor
import torch
from typing import Any, Literal
class ModifiedBaseModel(PydanticBaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def convert_custom_types(cls, v):
        if isinstance(v, Word):
            return {
                'id': v.id,
                'content': v.content,
                'embedding': {'data': v.embedding.data.tolist()}
            }
        if isinstance(v, Phrase):
            return {
                'id': v.id,
                'content': v.content,
                'embedding': {'data': v.embedding.data.tolist()}
            }
        if isinstance(v, Embedding):
            return {'data': v.data.tolist()}
        if isinstance(v, list):
            return [cls.convert_custom_types(item) for item in v]
        return v


class EmbeddingRequest(ModifiedBaseModel):
    stemmed_words: List[str]
    tokens: dict
    word_ids: List[int]

class EmbeddingResponse(ModifiedBaseModel):
    embeddings: List[Tensor[torch.Tensor, tuple, Literal["float32", "float64"]]]

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
    symbol: Union[Symbol, None]

class GetWordRequest(ModifiedBaseModel):
    word_text: str
    stemmed: bool = False

class GetWordResponse(ModifiedBaseModel):
    word: Union[dict, None]

class GetSimilarWordRequest(ModifiedBaseModel):
    embedding: Tensor[torch.Tensor, tuple, Literal["float32", "float64"]]

class GetAllPhrasesResponse(ModifiedBaseModel):
    phrases: List[dict]

class GetTranscriptionRequest(ModifiedBaseModel):
    audio_data: bytes

class GetTranscriptionResponse(ModifiedBaseModel):
    transcription: str







