user_index = int(input('Enter index: '))
a = 0
b = 1
index = 1

while index < user_index:
    result = a + b
    a = b
    b = result
    index = index + 1

if user_index == 0:
    b = 0
print(f"Индекс {user_index} в ряду Фибоначчи соответствует числу: {b}")
