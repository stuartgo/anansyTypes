from dataclasses import dataclass
from typing import Optional
from PIL import Image


@dataclass
class Symbol:
    id: int
    label: str
    image: Optional[Image.Image]
