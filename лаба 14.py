x = set(int(i) for i in input("Введите первое множество ").split()) #первое множество
y = set(int(i) for i in input("Введите второе множество ").split()) #второе множество
print(x&y)      #выводим общие числа
print(len(x&y)) #выводим их количество

