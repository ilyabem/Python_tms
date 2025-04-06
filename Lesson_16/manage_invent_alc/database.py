from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# --- Конфигурация Базы Данных ---
# Строка подключения к БД указана напрямую
DATABASE_URL = "postgresql://admin:1111@localhost:5432/python_tms" # Имя пользователя, пароль, хост, порт, имя БД

# Создаем движок sqlalchemy для работы с БД
# echo=False, чтобы не выводить SQL-запросы в консоль
engine = create_engine(DATABASE_URL, echo=False)

# Создаем фабрику сессий для работы с БД
# expire_on_commit=False позволяет использовать объекты после коммита сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

# Создаем базовый класс для моделей
Base = declarative_base()


# --- Модели SQLAlchemy ---

class Category(Base):
    """Модель для категории товаров."""
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)

    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"


class Product(Base):
    """Модель для товара."""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)

    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    category = relationship("Category", back_populates="products")

    order_items = relationship("OrderItem", back_populates="product", cascade="all, delete-orphan")
    suppliers = relationship("ProductSupplier", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, quantity={self.quantity})>"


class Supplier(Base):
    """Модель для поставщика."""
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    contact_info = Column(String(255), nullable=True)

    products = relationship("ProductSupplier", back_populates="supplier", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="supplier")

    def __repr__(self):
        return f"<Supplier(id={self.id}, name='{self.name}')>"


class ProductSupplier(Base):
    """Ассоциативная таблица для связи многие-ко-многим между Product и Supplier."""
    __tablename__ = "products_suppliers"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id", ondelete="CASCADE"), nullable=False)

    product = relationship("Product", back_populates="suppliers")
    supplier = relationship("Supplier", back_populates="products")

    def __repr__(self):
        return f"<ProductSupplier(product_id={self.product_id}, supplier_id={self.supplier_id})>"


class Order(Base):
    """Модель для заказа."""
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id", ondelete="SET NULL"), nullable=True)
    order_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String(50), default="Ожидание", nullable=False)

    supplier = relationship("Supplier", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, supplier_id={self.supplier_id}, status='{self.status}')>"


class OrderItem(Base):
    """Модель для конкретного товара в заказе."""
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem(order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})>"


# --- Функции для работы с базой данных ---

def init_db():
    """Создает все таблицы в базе данных, если они еще не существуют."""
    try:
        Base.metadata.create_all(bind=engine)
        print("Таблицы успешно созданы или уже существуют.")
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")


# --- Функции CRUD (Create, Read, Update, Delete) ---

def get_all_products(db):
    """Возвращает все товары из базы данных."""
    return db.query(Product).all()


def get_all_categories(db):
    """Возвращает все категории товаров из базы данных."""
    return db.query(Category).all()


def get_all_suppliers(db):
    """Возвращает всех поставщиков из базы данных."""
    return db.query(Supplier).all()


def get_all_orders(db):
    """Возвращает все заказы из базы данных."""
    from sqlalchemy.orm import joinedload
    return db.query(Order).options(joinedload(Order.supplier)).all()


def add_product(db, name: str, price: float, category_id: int, quantity: int):
    """Добавляет новый товар в базу данных."""
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        print(f"Ошибка: Категория с ID {category_id} не найдена.")
        return None

    new_product = Product(name=name, price=price, category_id=category_id, quantity=quantity)
    db.add(new_product)
    return new_product


def add_category(db, name: str):
    """Добавляет новую категорию товаров в базу данных."""
    new_category = Category(name=name)
    db.add(new_category)
    return new_category


def add_supplier(db, name: str, contact_info: str):
    """Добавляет нового поставщика в базу данных."""
    new_supplier = Supplier(name=name, contact_info=contact_info)
    db.add(new_supplier)
    return new_supplier


def create_order(db, supplier_id: int):
    """Создает новый заказ и возвращает его."""
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        print(f"Ошибка: Поставщик с ID {supplier_id} не найден.")
        return None

    new_order = Order(supplier_id=supplier_id)
    db.add(new_order)
    return new_order


def search_product(db, query: str):
    """Ищет товары по названию (без учета регистра)."""
    return db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()


def get_product_by_id(db, product_id: int):
    """Получает товар по его ID."""
    return db.query(Product).filter(Product.id == product_id).first()


def update_product_price(db, product_id: int, new_price: float):
    """Обновляет цену товара по его ID."""
    product = get_product_by_id(db, product_id)
    if product:
        product.price = new_price
        return product
    else:
        print(f"Ошибка: Товар с ID {product_id} не найден.")
        return None


def delete_product(db, product_id: int):
    """Удаляет товар из базы данных по его ID."""
    product = get_product_by_id(db, product_id)
    if product:
        db.delete(product)
        return True
    else:
        print(f"Ошибка: Товар с ID {product_id} не найден.")
        return False


def get_supplier_by_id(db, supplier_id: int):
    """Получает поставщика по его ID."""
    return db.query(Supplier).filter(Supplier.id == supplier_id).first()


def delete_supplier(db, supplier_id: int):
    """Удаляет поставщика из базы данных по его ID."""
    supplier = get_supplier_by_id(db, supplier_id)
    if supplier:
        db.delete(supplier)
        return True
    else:
        print(f"Ошибка: Поставщик с ID {supplier_id} не найден.")
        return False
