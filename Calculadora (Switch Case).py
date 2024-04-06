print(' ## Calculadora ## ')

while True:
    a = int(input('\nInsira um número: '))
    func = input('Função: ')
    b = int(input('Insira outro número: '))
    match func:
        case '+':
            print(f'{a} + {b} = {a + b}')
        case '-':
            print(f'{a} - {b} = {a - b}')
        case '*':
            print(f'{a} x {b} = {a * b}')
        case '/':
            print(f'{a} / {b} = {a / b}')
        case _:
            print('Função Invalida')