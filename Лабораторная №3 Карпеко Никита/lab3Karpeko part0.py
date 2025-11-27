#Полное чтение
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
print(content)
    
#Построчное чтение
with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)

