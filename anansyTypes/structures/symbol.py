from dataclasses import dataclass
from typing import Any
import numpy as np
from pydantic_tensor import Tensor
from typing import Any, Literal
from pydantic_core import core_schema


@dataclass
class Symbol:
    id: int
    label: str
    image: Tensor[np.ndarray[Any, Any], tuple, Literal["int32", "int64"]]

    @classmethod
    def from_dict(cls, data: dict) -> 'Symbol':
        return cls(
            id=data['id'],
            label=data['label'],
            image=np.array(data['image'], dtype=np.int32)
        )

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        from pydantic_core import core_schema
        
        return core_schema.no_info_after_validator_function(
            cls,
            core_schema.dataclass_schema(
                cls=cls,
                schema=core_schema.dataclass_args_schema(
                    cls.__name__,
                    [
                        core_schema.dataclass_field(name='id', schema=handler.generate_schema(int)),
                        core_schema.dataclass_field(name='label', schema=handler.generate_schema(str)),
                        core_schema.dataclass_field(
                            name='image',
                            schema=handler.generate_schema(Tensor[np.ndarray[Any, Any], tuple, Literal["int32", "int64"]])
                        ),
                    ],
                ),
                fields=['id', 'label', 'image'],
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: {
                    'id': x.id,
                    'label': x.label,
                    'image': x.image
                },
                when_used='json',
            ),
        )
