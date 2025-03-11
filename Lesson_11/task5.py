#5. Разработать класс SuperStr, который наследует
#функциональность стандартного типа str и содержит два
#новых метода:
#● метод is_repeatance(s), который принимает некоторую
#строку и возвращает True или False в зависимости от того,
#может ли текущая строка быть получена целым
#количеством повторов строки s. Считать, что пустая
#строка не содержит повторов
#● метод is_palindrom(), который возвращает True или False в
#зависимости от того, является ли строка палиндромом вне
#зависимости от регистра. Пустую строку считать
#палиндромом.


class SuperStr(str):
        def is_repeatance(self, s):
            # Пустая строка не может быть получена из повторений
            if not s:
                return False
            # Проверяем, делится ли длина строки на длину s
            if len(self) % len(s) == 0:
                # Проверяем, состоит ли строка из повторений s
                return self == s * (len(self) // len(s))
            return False

        def is_palindrom(self):
            # Приводим строку к нижнему регистру
            cleaned_str = self.lower()
            # Сравниваем строку с ее перевернутой версией
            return cleaned_str == cleaned_str[::-1]
s1 = SuperStr("ababab")
print(s1.is_repeatance("ab"))
print(s1.is_repeatance("aba"))

s2 = SuperStr("Madam")
print(s2.is_palindrom())

s3 = SuperStr("hello")
print(s3.is_palindrom())