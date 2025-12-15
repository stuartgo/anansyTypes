import anansyTypes
from enum import Enum
from typing import Union


class ModelType(Enum):
    EMBEDDING = "embedding"
    TRANSCRIPTION = "transcription"
    RESPONSE = "response"


class ModelName(Enum):
    pass


class EmbeddingModelName(ModelName):
    NB_BERT = "nb_bert"


class TranscriptionModelName(ModelName):
    NB_WHISPER_SMALL = "nb_whisper_small"


class ResponseModelName(ModelName):
    GENERIC = "generic"


class PreprocessorType(Enum):
    NORWEGIAN = "norwegian"
    DEFAULT = "norwegian"


class SymbolProvider(Enum):
    TOBII_DYNAVOX = "tobii_dynavox"


class Language(Enum):
    NORWEGIAN = "norwegian"
    ENGLISH = "english"
    DEFAULT = "norwegian"


class ResourceType(Enum):
    WORD = "word"
    SYMBOL = "symbol"
