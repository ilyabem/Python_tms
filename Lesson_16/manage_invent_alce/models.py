
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    products = relationship("Product", back_populates="category")

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    contact = Column(String)
    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    quantity = Column(Integer)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    category = relationship("Category", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")
    supply_orders = relationship("SupplyOrder", back_populates="product")

class SupplyOrder(Base):
    __tablename__ = 'supply_orders'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    order_date = Column(DateTime, default=datetime.utcnow)
    product = relationship("Product", back_populates="supply_orders")