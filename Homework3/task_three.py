import random
random_list = [random.randint(-100, 100) for i in range(10)]
print(random_list)

random_list.insert(2, random.randint(-100, 100))
del random_list[6]

print(random_list)
