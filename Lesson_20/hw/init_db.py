# init_db.py
from models import Base
from base_1 import engine

Base.metadata.create_all(engine)
print("БД пересоздана.")