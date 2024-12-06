from sqlalchemy import BigInteger, Text, ForeignKey, func, Numeric
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from backend.app.main_models import Base


class Shops(Base):
    __tablename__ = 'shops'

    shop_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    categories: Mapped[str] = mapped_column()
    count_reviews: Mapped[int] = mapped_column()
    creater_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class Products(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    seller: Mapped[int] = mapped_column(BigInteger, ForeignKey("shops.shop_id"))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Numeric)
    count_reviews: Mapped[int] = mapped_column()
