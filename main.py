text = open('text.txt', encoding="utf-8") #Открытие файла с помощью кодировки utf-8 и присваивание его переменной text
print("Количество слов в файле:", len(text.read().split())) #Вывод на консоль количества слов в файле с помощью функции len() и функции разделения на элементы split()
text.close() #Закрытие файла
