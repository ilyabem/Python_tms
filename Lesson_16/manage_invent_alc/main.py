from sqlalchemy.exc import IntegrityError # Для обработки ошибок уникальности

try:
    from Lesson_16.manage_invent_alc.database import (
        SessionLocal, init_db, get_all_products, get_all_categories,
        get_all_suppliers, get_all_orders, add_product, add_category,
        add_supplier, create_order, search_product, update_product_price,
        delete_product, delete_supplier, get_product_by_id, get_supplier_by_id
    )
except ImportError:
    print("="*50)
    print("ОШИБКА ИМПОРТА: Не удалось найти модуль 'database'.")
    print("Пожалуйста, убедитесь, что файл 'database.py' находится в правильном месте")
    print("и путь импорта в 'main.py' указан верно.")
    print("Если 'database.py' находится в той же папке, что и 'main.py', используйте:")
    print("from database import ...")
    print("="*50)
    exit() # Выход, если импорт не удался

def print_menu():
    """Выводит меню доступных команд."""
    print("\n--- Меню Управления Инвентарем ---")
    print("0. Выход")
    print("1. Показать все товары")
    print("2. Показать все категории")
    print("3. Показать всех поставщиков")
    print("4. Показать все заказы")
    print("5. Добавить товар")
    print("6. Добавить категорию")
    print("7. Добавить поставщика")
    print("8. Создать заказ")
    print("9. Найти товар по названию")
    print("10. Обновить цену товара")
    print("11. Удалить товар")
    print("12. Удалить поставщика")
    print("----------------------------------")


# Основной цикл работы приложения
def app():
    """Главная функция приложения."""
    try:
        init_db()  # Инициализация базы данных (создание таблиц)
    except Exception as e:
        print(f"Критическая ошибка при инициализации БД: {e}")
        print("Проверьте строку подключения DATABASE_URL в database.py и доступность сервера БД.")
        return # Выход из приложения, если БД недоступна

    print("\nДобро пожаловать в систему управления инвентарем!")

    while True:
        print_menu()

        # Обрабатываем возможный неверный ввод
        try:
            cmd = int(input("Введите номер команды: "))
        except ValueError:
            print("Ошибка: введите число от 0 до 12!")
            continue

        # Используем менеджер контекста для управления сессией БД
        # Сессия создается для каждой операции и автоматически закрывается
        try: # Общий try-блок для обработки ошибок БД внутри сессии
            with SessionLocal() as db:
                if cmd == 0:
                    print("Выход из программы. До свидания!")
                    break

                elif cmd == 1:
                    print("=" * 30)
                    print("Список товаров: ")
                    products = get_all_products(db)
                    if not products:
                        print("Товаров пока нет.")
                    else:
                        for product in products:
                            # Получаем имя категории (если категория есть)
                            category_name = product.category.name if product.category else "Без категории"
                            print(f"ID: {product.id} | Название: {product.name} | Цена: {product.price:.2f} руб. | Кол-во: {product.quantity} | Категория: {category_name}")
                    print("=" * 30)

                elif cmd == 2:
                    print("=" * 30)
                    print("Список категорий: ")
                    categories = get_all_categories(db)
                    if not categories:
                        print("Категорий пока нет.")
                    else:
                        for category in categories:
                            print(f"ID: {category.id} | Название: {category.name}")
                    print("=" * 30)

                elif cmd == 3:
                    print("=" * 30)
                    print("Список поставщиков: ")
                    suppliers = get_all_suppliers(db)
                    if not suppliers:
                        print("Поставщиков пока нет.")
                    else:
                        for supplier in suppliers:
                            contact = supplier.contact_info if supplier.contact_info else "Нет данных"
                            print(f"ID: {supplier.id} | Название: {supplier.name} | Контакты: {contact}")
                    print("=" * 30)

                elif cmd == 4:
                    print("=" * 30)
                    print("Список заказов:")
                    orders = get_all_orders(db)
                    if not orders:
                        print("Заказов пока нет.")
                    else:
                        for order in orders:
                            supplier_name = order.supplier.name if order.supplier else "Поставщик удален"
                            # Используем order_date вместо date_created
                            print(f"ID: {order.id} | Дата: {order.order_date.strftime('%Y-%m-%d %H:%M')} | Статус: {order.status} | Поставщик: {supplier_name} (ID: {order.supplier_id or 'N/A'})")
                    print("=" * 30)

                elif cmd == 5:
                    print("=" * 30)
                    print("Добавление нового товара: ")
                    name = input("Введите название нового товара: ")
                    try:
                        price = float(input("Введите цену нового товара: "))
                        quantity = int(input("Введите количество товара: ")) # Добавлен ввод количества
                        category_id = int(input("Введите ID категории: "))

                        # Вызываем функцию добавления товара, передавая сессию db
                        new_product = add_product(db, name=name, price=price, category_id=category_id, quantity=quantity)

                        if new_product: # Проверяем, что товар был создан
                            db.commit() # Сохраняем изменения в БД
                            db.refresh(new_product) # Обновляем объект из БД (получаем ID и т.д.)
                            print(f"Товар '{new_product.name}' (ID: {new_product.id}) успешно добавлен!")
                        # else: Ошибка уже напечатана в add_product, если категория не найдена

                    except ValueError:
                        print("Ошибка: Введите корректные числовые данные для цены, количества и ID категории!")
                    except IntegrityError: # Обработка ошибки уникальности (например, имя товара уже существует)
                         db.rollback() # Откатываем транзакцию
                         print(f"Ошибка: Товар с названием '{name}' уже существует.")
                    except Exception as e:
                        db.rollback() # Откатываем транзакцию при любой другой ошибке
                        print(f"Непредвиденная ошибка при добавлении товара: {e}")
                    print("=" * 30)

                elif cmd == 6:
                    print("=" * 30)
                    print("Добавление новой категории: ")
                    category_name = input("Введите название категории: ")
                    try:
                        new_category = add_category(db, name=category_name)
                        db.commit() # Сохраняем
                        db.refresh(new_category) # Обновляем
                        print(f"Категория '{new_category.name}' (ID: {new_category.id}) успешно добавлена!")
                    except IntegrityError:
                         db.rollback()
                         print(f"Ошибка: Категория с названием '{category_name}' уже существует.")
                    except Exception as e:
                        db.rollback()
                        print(f"Ошибка добавления категории: {e}")
                    print("=" * 30)

                elif cmd == 7:
                    print("=" * 30)
                    print("Добавление поставщика: ")
                    supplier_name = input("Введите название поставщика: ")
                    contact_info = input("Введите контактную информацию: ") # Добавлен ввод контактов
                    try:
                        new_supplier = add_supplier(db, name=supplier_name, contact_info=contact_info)
                        db.commit() # Сохраняем
                        db.refresh(new_supplier) # Обновляем
                        print(f"Поставщик '{new_supplier.name}' (ID: {new_supplier.id}) успешно добавлен!")
                    except IntegrityError:
                         db.rollback()
                         print(f"Ошибка: Поставщик с названием '{supplier_name}' уже существует.")
                    except Exception as e:
                        db.rollback()
                        print(f"Ошибка добавления поставщика: {e}")
                    print("=" * 30)

                elif cmd == 8:
                    print("=" * 30)
                    print("Создание нового заказа: ")
                    try:
                        supplier_id = int(input("Введите ID поставщика для заказа: "))
                        new_order = create_order(db, supplier_id=supplier_id)
                        if new_order:
                            db.commit() # Сохраняем
                            db.refresh(new_order) # Обновляем
                            print(f"Заказ успешно создан! ID заказа: {new_order.id}")
                        # else: Ошибка уже напечатана в create_order

                    except ValueError:
                        print("Ошибка: Введите корректный ID поставщика (целое число)!")
                    except Exception as e:
                        db.rollback()
                        print(f"Ошибка при создании заказа: {e}")
                    print("=" * 30)

                elif cmd == 9:
                    print("=" * 30)
                    print("Поиск товара по названию: ")
                    query = input("Введите часть названия товара для поиска: ")
                    products = search_product(db, query=query)
                    if products:
                        print("Найденные товары:")
                        for product in products:
                            category_name = product.category.name if product.category else "Без категории"
                            print(f"ID: {product.id} | Название: {product.name} | Цена: {product.price:.2f} руб. | Кол-во: {product.quantity} | Категория: {category_name}")
                    else:
                        print(f"Товары, содержащие '{query}', не найдены.")
                    print("=" * 30)

                elif cmd == 10:
                    print("=" * 30)
                    print("Обновление цены товара:")
                    try:
                        product_id = int(input("Введите ID товара для обновления цены: "))
                        new_price = float(input("Введите новую цену: "))
                        if new_price < 0:
                            print("Ошибка: Цена не может быть отрицательной.")
                        else:
                            updated_product = update_product_price(db, product_id=product_id, new_price=new_price)
                            if updated_product:
                                db.commit() # Сохраняем изменения
                                print(f"Цена товара '{updated_product.name}' (ID: {product_id}) успешно обновлена до {updated_product.price:.2f} руб.")
                            # else: Ошибка уже напечатана в update_product_price

                    except ValueError:
                        print("Ошибка: Введите корректные числовые значения для ID и цены!")
                    except Exception as e:
                        db.rollback()
                        print(f"Ошибка при обновлении цены: {e}")
                    print("=" * 30)

                elif cmd == 11:
                    print("=" * 30)
                    print("Удаление товара:")
                    try:
                        product_id = int(input("Введите ID товара для удаления: "))
                        # Дополнительно получим имя товара перед удалением для сообщения
                        product_to_delete = get_product_by_id(db, product_id)
                        if product_to_delete:
                            product_name = product_to_delete.name
                            if delete_product(db, product_id=product_id):
                                db.commit() # Сохраняем изменения
                                print(f"Товар '{product_name}' (ID: {product_id}) успешно удален!")
                            # else: Ошибка уже напечатана в delete_product
                        else:
                             print(f"Ошибка: Товар с ID {product_id} не найден.")

                    except ValueError:
                        print("Ошибка: Введите корректный ID товара (целое число)!")
                    except IntegrityError as e: # Может возникнуть, если есть связи, которые не каскадируются
                        db.rollback()
                        print(f"Ошибка целостности базы данных при удалении товара: {e}")
                        print("Возможно, товар используется в заказах, которые не позволяют удаление.")
                    except Exception as e:
                        db.rollback()
                        print(f"Ошибка при удалении товара: {e}")
                    print("=" * 30)

                elif cmd == 12:
                    print("=" * 30)
                    print("Удаление поставщика:")
                    try:
                        supplier_id = int(input("Введите ID поставщика для удаления: "))
                        # Получим имя перед удалением
                        supplier_to_delete = get_supplier_by_id(db, supplier_id)
                        if supplier_to_delete:
                            supplier_name = supplier_to_delete.name
                            if delete_supplier(db, supplier_id=supplier_id):
                                db.commit() # Сохраняем изменения
                                print(f"Поставщик '{supplier_name}' (ID: {supplier_id}) успешно удален!")
                                print("Примечание: В связанных заказах ID поставщика был установлен в NULL.")
                            # else: Ошибка уже напечатана в delete_supplier
                        else:
                            print(f"Ошибка: Поставщик с ID {supplier_id} не найден.")

                    except ValueError:
                        print("Ошибка: Введите корректный ID поставщика (целое число)!")
                    except IntegrityError as e: # Маловероятно из-за SET NULL, но возможно
                        db.rollback()
                        print(f"Ошибка целостности базы данных при удалении поставщика: {e}")
                    except Exception as e:
                        db.rollback()
                        print(f"Ошибка при удалении поставщика: {e}")
                    print("=" * 30)

                else:
                    print("Ошибка! Неизвестная команда.")

        except Exception as e: # Перехват ошибок на уровне сессии (например, ошибка подключения)
            print(f"\n--- Произошла ошибка сессии базы данных ---")
            print(f"Ошибка: {e}")
            print("Пожалуйста, проверьте соединение с БД и попробуйте снова.")
            # Можно добавить логику ожидания перед повторной попыткой или выхода


# Запуск программы, если скрипт выполняется напрямую
if __name__ == "__main__":
    app()
11