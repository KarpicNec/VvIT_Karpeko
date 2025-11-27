def reading(method):
    if method == 'full':
        #Полное чтение
        with open('example.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        print(content)
    elif method == 'parts':
        #Построчное чтение
        with open('example.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line)
    else:
        print('no such method')

n = input('reading using \'full\' or \'parts\'? \n')
reading(n)

