messege = input("Введите любое сообщение, состоящее из двух слов: ")
listOfWords = messege.split()
listOfWords.reverse()
result = ' '.join(listOfWords)
print(result)