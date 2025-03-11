 #ПчёлоСлон
#Экземпляр класса инициализируется двумя целыми числами,
#первое относится к пчеле, второе – к слону. Класс реализует
#следующие методы:
#● fly() – возвращает True, если часть пчелы не меньше части
#слона, иначе – False
#● trumpet() – если часть слона не меньше части пчелы,
#возвращает строку “tu-tu-doo-doo”, иначе –
#“wzzzz”
#● eat(meal, value) – может принимать в meal только ”nectar”
#или “grass”. Если съедает нектар, то value вычитается из
#части слона, пчеле добавляется. Иначе – наоборот. Не
#может увеличиваться больше 100 и уменьшаться меньше 0.

class BeeElef:
    def __init__(self, bee_part = 50, elephant_part = 50):
        self.bee_part = max(0, min(100,bee_part))
        self.elephant_part = max(0, min(100,elephant_part))

    def fly(self):
        if self.bee_part >= self.elephant_part:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo"
        else:
            return "wzzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant_part = max(0, self.elephant_part- value)
            self.bee_part = max(0, self.bee_part + value)
        elif meal == "grass":
            self.elephant_part = max(0, self.elephant_part + value)
            self.bee_part = max(0, self.bee_part - value)
        else:
            pass

    def __str__(self):
        return f"{self.bee_part}% | {self.elephant_part}%"

# Test
be = BeeElef(30, 70)  # Создаём объект с 30% пчелы и 70% слона
print("Начальное состояние:", be)

# Проверяем способности
print("Может ли летать?", be.fly())
print("Какой звук издаёт?", be.trumpet())

# Кормим нектаром (должно увеличить пчелиную часть и уменьшить слоновью)
be.eat("nectar", 20)
print("После еды (nectar, 20):", be)

# Кормим травой (увеличит слоновью часть и уменьшит пчелиную)
be.eat("grass", 30)
print("После еды (grass, 30):", be)

# Проверяем снова
print("Может ли летать теперь?", be.fly())
print("Какой звук теперь издаёт?", be.trumpet())
