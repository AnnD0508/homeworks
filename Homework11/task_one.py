import random
AVAILABLE_NAMES = [
    'John',
    'Jane',
    'Mary',
    'David',
    'Alex',
    'Max',
    'Nick',
    'Anastasia',
    'Leo'
    ]
AVAILABLE_COLORS = ['blue', 'green', 'brown', 'grey', 'black']


class User():
    def __init__(self, name, nickname, age, eyes_colors):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.eyes_colors = eyes_colors

    @property
    def info(self):
        return {
            'Name': self.name,
            'Nickname': self.nickname,
            'Age': self.age,
            'Eyes_color': self.eyes_colors}

    def __eq__(self, obj):
        if not isinstance(obj, User):
            raise TypeError('Wrong type of object')
        return self.age == obj.age

    def __ge__(self, obj):
        if not isinstance(obj, User):
            raise TypeError('Wrong type of object')
        return self.age >= obj.age

    def __gt__(self, obj):
        if not isinstance(obj, User):
            raise TypeError('Wrong type of object')
        return self.age > obj.age


def users_generator(max_number):
    current_index = 0
    while current_index <= max_number:
        name = random.choice(AVAILABLE_NAMES)
        nickname = f"{name}{random.randint(10000, 99999)}"
        age = random.randint(0, 100)
        eyes_color = random.choice(AVAILABLE_COLORS)
        user = User(name, nickname, age, eyes_color)
        current_index += 1
        yield user


gen = users_generator(500000)
for user in gen:
    print(user.info)
