import random

print('\n## Vamos começar o nosso jogo de adivinhação! ##\n')
print('OBS: Leia com atenção as dicas. Elas vão te ajudar.\n')

def game():
  a = random.randint(1, 10)
  while True:
    b = int(input('Adivinha o número que eu estou pensando entre 1 e 10: '))
    if a > b:
      print(f'O número que estou pensado é maior que {b}.\n')
    elif a < b:
      print(f'O número que estou pensando é menos que {b}.\n')
    else:
      print(f'Parabéns! Você acertou! O número que eu estava pensando era {a}.\n')
      break

game()
