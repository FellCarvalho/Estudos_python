print(' ## Calculadora ## ')

while True:
    a = int(input('\nInsira um número: '))
    func = input('Função: ')
    b = int(input('Insira outro número: '))
    if func == '+':
        print(f'{a} + {b} = {a + b}')
    elif func == '-':
        print(f'{a} - {b} = {a - b}')
    elif func == '*':
        print(f'{a} x {b} = {a * b}')
    elif func == '/':
        print(f'{a} / {b} = {a / b}')
    else:
        print('Função Invalida')