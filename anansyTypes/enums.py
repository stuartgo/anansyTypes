from enum import Enum
class ModelType(Enum):
    EMBEDDING = "embedding"
    TRANSCRIPTION = "transcription"
    RESPONSE = "response"
    
class EmbeddingModelName(Enum):
    NB_BERT = "nb_bert"

class TranscriptionModelName(Enum):
    NB_WHISPER_SMALL = "nb_whisper_small"

class ResponseModelName(Enum):
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

