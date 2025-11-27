def writing():
    print ('\'stop\' чтобы прекратить \n')
    n = 'start'
    with open('user_input.txt', 'a', encoding='utf-8') as file:
        while n != 'stop':
            n = input()
            if n != 'stop':
                file.write(n + '\n')

writing()
        

