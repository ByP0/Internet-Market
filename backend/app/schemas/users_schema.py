from pydantic import BaseModel, Field
from typing import Annotated


class RegisterSchema(BaseModel):
    username: Annotated[str, Field(title="Имя пользователя", examples=['BigJohn123'])]
    password: Annotated[str, Field(title="Пароль пользователя", examples=['Password123'])]