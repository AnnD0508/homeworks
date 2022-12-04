user_letter = input('Введите любую букву английского алфавита: ')

with open('task_three.txt') as f:
    count = 0

    for line in f:
        for letter in line:
            if letter.lower() == user_letter.lower():
                count = count + 1
    print(f'Введенная буква {user_letter} встречается в тексте:{count} раз')
