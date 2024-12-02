from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Annotated, Optional


class RegisterSchema(BaseModel):
    username: Annotated[str, Field(title="Имя пользователя", examples=['BigJohn123'])]
    email: Annotated[Optional[str], Field(title="Почта пользователя", examples=['example1@gmail.com'])]
    password: Annotated[str, Field(title="Пароль пользователя", examples=['Password123'])]


class LogginingSchema(BaseModel):
    username: Annotated[str, Field(title="Имя пользователя", examples=['BigJohn123'])]
    password: Annotated[str, Field(title="Пароль пользователя", examples=['Password123'])]


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    username: Annotated[str, Field(title="Имя пользователя", examples=['BigJohn123'])]
    password: Annotated[bytes, Field(title="Пароль пользователя", examples=['Password123'])]
    email: Annotated[Optional[EmailStr], Field(title="Почта пользователя", examples=['example1@gmail.com'])]
    active: Annotated[Optional[bool], Field(title='Актив пользователя', examples=[True], default=True)]

class AccessJWT(BaseModel):
    access_jwt: Annotated[str, Field(title='Access JWT-token', examples=
                                     ['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'])]
    

class TokenInfo(BaseModel):
    access_token: str
    token_type: str


class JWTPayload(BaseModel):
    subject: Annotated[int, Field(title="ID пользователя", examples=[5])]
    username: Annotated[str, Field(title="Имя пользователя", examples=['BigJohn123'])]
    email: Annotated[Optional[str], Field(title="Почта пользователя", examples=['example1@gmail.com'])]
    role: Annotated[str, Field(title="Роль пользователя", examples=['admin', 'seller', 'customer'], default='customer')]