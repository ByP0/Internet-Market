from pydantic import BaseModel, Field
from typing import Annotated


class RegisterShopSchema(BaseModel):
    name: Annotated[str, Field(title="Название магазина")]
    categories: Annotated[list, Field(title="категории")]
