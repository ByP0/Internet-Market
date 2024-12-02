from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional
from datetime import datetime


class RegisterSchema(BaseModel):
    username: Annotated[str, Field(title="Имя пользователя", examples=['BigJohn123'])]
    email: Annotated[EmailStr, Field(title="Почта пользователя", examples=['example1@gmail.com'])]
    password: Annotated[str, Field(title="Пароль пользователя", examples=['Password123'])]


class LogginingSchema(BaseModel):
    username: Annotated[str, Field(title="Имя пользователя", examples=['BigJohn123'])]
    password: Annotated[str, Field(title="Пароль пользователя", examples=['Password123'])]


class UserInfoSchema(BaseModel):
    username: Annotated[str, Field(title="Имя пользователя", examples=['BigJohn123'])]
    email: Annotated[EmailStr, Field(title="Почта пользователя", examples=['example1@gmail.com'])]
    phone: Annotated[str | None, Field(title="Номер телефона", examples=['79211234567'])]
    verife_phone: Annotated[bool, Field(title="Номер телефона подтвержден?", examples=['True'], default=False)]
    verife_email: Annotated[bool, Field(title="Электронная почта подтверждена?", examples=['True'], default=False)]
    created_at: Annotated[Optional[datetime], Field(title="Дата и время создание профиля", examples=['2024-12-02 10:27:34.850575'])]