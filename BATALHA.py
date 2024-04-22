import random


# STATUS DO PERSONAGEM
def danop():
    return random.choice([1, 2, 3]) * 100


hp = 1500


# STATUS DO MONSTRO
def danom():
    return random.choice([1, 2]) * 100


hpM = 2500

while hpM >= 0:
    esc = input('Voce deseja ATACAR ou FUGIR?: ')
    if esc == 'ATACAR':
        atq = danop()
        hpM -= atq
        print(f'O seu ataque causou {atq} de dano no monstro ele ficou com {hpM} de vida')
        atqM = danom()
        hp -= atqM
        print(f'O monstro ficou furioso e revidou. Causando {atqM} de dano e seu personagem ficou com {hp} de vida.')
    if hp <= 0:
        print('Voce lutou com bravura e isso não foi o suficiente.')
        break
    if hpM <= 0:
        print('Voce derrotou o monstro. Teu nome será honrado e glorificado')
        break
    elif esc == 'FUGIR':
        f = random.randint(1, 3)
        match f:
            case 1:
                hp -= 15
                print(f'Voce tentou escapar, mas tropeçou em um boraco e recebeu 15 de dano! Seu HP agpra e de {hp}.')
            case 2:
                print('Voce é bem rápido, mas não o suficiente para escapar!')
            case 3:
                print('Voce foi extremamente veloz e conseguiu fugir do monstro!')
                break
    else:
        print('Comando incorreto. Tente novamente.')
