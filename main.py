text=open('text.txt', encoding="utf-8")   
print("Количество слов в файле:", len(text.read().split()))
text.close()