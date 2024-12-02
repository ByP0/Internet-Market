from sqlalchemy import BigInteger, Text, ForeignKey, func, Float, text, Null
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from typing import Optional
from main_models import Base


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column(Text)
    phone: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[Optional[str]] = mapped_column(default=Null)
    role: Mapped[str] = mapped_column(default='customer')
    verify_phone: Mapped[bool] = mapped_column(default=False)
    verify_email: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))