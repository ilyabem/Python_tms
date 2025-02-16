def demical_to_binary(n):
    if n == 0:
        return "0"

    #создаем пустую строку для записи результата
    binary = ""
    while n>0:
        #берем остаток от деления и добавляем его в строку binary
        binary = str(n % 2) + binary
        n = n//2
    return binary
n = 12
print (demical_to_binary(n))