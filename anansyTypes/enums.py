from enum import Enum
class ModelType(Enum):
    EMBEDDING = "embedding"
    TRANSCRIPTION = "transcription"
    RESPONSE = "response"
class PreprocessorType(Enum):
    NORWEGIAN = "norwegian"
    DEFAULT = "norwegian"
class SymbolProvider(Enum):
    TOBII_DYNAVOX = "tobii_dynavox"


class Language(Enum):
    NORWEGIAN = "norwegian"
    ENGLISH = "english"
    DEFAULT = "norwegian"

