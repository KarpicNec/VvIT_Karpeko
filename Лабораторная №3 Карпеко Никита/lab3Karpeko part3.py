def spec_reading(name, method):
    try:
        if method == 'full':
            #Полное чтение
            with open(str(name) + '.txt', 'r', encoding='utf-8') as file:
                content = file.read()
            print(content)
        elif method == 'parts':
            #Построчное чтение
            with open(str(name) + '.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    print(line)
        else:
            print('no such method')
    except Exception as FileNotFoundError:
        print("Нет такого файла...")

n = input('write a name of file and you like reading using \'full\' or \'parts\'? \n')
a, b = n.split()
spec_reading(a, b)
