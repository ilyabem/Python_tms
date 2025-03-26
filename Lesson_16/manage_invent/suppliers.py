#В этом файле будут функции для работы с таблицей поставщиков.
#Подключение к БД будет передаваться из main.py.

import psycopg2

def delete_supplier_and_orders(conn, cursor, supplier_name):
    try:
        # Удаление всех связанных заказов
        cursor.execute("DELETE FROM orders WHERE supplier_id = (SELECT id FROM suppliers WHERE name = %s)", (supplier_name,))
        # Удаление поставщика
        cursor.execute("DELETE FROM suppliers WHERE name = %s", (supplier_name,))
        conn.commit()
        print(f"Поставщик '{supplier_name}' и связанные заказы успешно удалены!")
    except Exception as e:
        print(f"Ошибка при удалении поставщика: {e}")
        conn.rollback()

# Пример подключения и использования функции
if __name__ == "__main__":
    conn = psycopg2.connect(
        dbname="python_tms",
        user="admin",
        password="1111",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    delete_supplier_and_orders(conn, cursor, "5 Элемент")
    cursor.close()
    conn.close()