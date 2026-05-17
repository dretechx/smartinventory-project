from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Date,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    product_name = Column(String)

    category = Column(String)

    base_sale_rate = Column(Integer)

    weekend_multiplier = Column(Float)

    sales = relationship(
        "Sale",
        back_populates="product"
    )


class Sale(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)

    sales_date = Column(Date)

    day_of_week = Column(String)

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    units_sold = Column(Integer)

    weekend_tracker = Column(Boolean)

    product = relationship(
        "Product",
        back_populates="sales"
    )