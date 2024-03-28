import random

print('\nVamos começar o nosso jogo de advinhação!\n')
print('### Preste atenção nas dicas! Elas vão te ajudar bastante. ###\n')


def game():
    a = random.randint(1, 10)
    while True:
        b = int(input('Adivinhe o número que estou pensando entre 1 e 10: '))
        if a > b:
            print(f'O número que estou pensado é maior que {b}\n')
        elif a < b:
            print(f'O número que estou pensando é menor que {b}\n')
        else:
            print(f'PARABÉNS! O NÚMERO QUE ESTAVA PENSANDO ERA O {b}\n')
            break


game()
