# Criado por Gianlucca Fadiga

# Importar Random
import random

# Importar Time
import time

# Limpar terminal
import os
clear = lambda: os.system('cls')

# Definição do tabuleiro
tabuleiro = [[' ', ' ', ' '],
             [' ', ' ', ' '], 
             [' ', ' ', ' ']]


# Início do jogo
print('Bem vindo ao jogo da velha eletrônico 3000') 
modoDeJogo = int(input(f'Escolha um modo de jogo: \n 1 - Jogador x Máquina \n 2 - Jogador x Jogador \n Sua opção: '))
clear()

# Função de mostrar no terminal o tabuleiro
def mostrar():
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{tabuleiro[l][c]}]', end='') 
        print()

# Def para encontrar ganhador ou velha
def ganhador():
    global temVencedor
    # Verificação de vencedor linha/coluna/diagonal
    for linha in tabuleiro:
        if (linha[0] == linha[1] == linha[2] and linha[0] != ' ' and linha[1] != ' ' and linha[2] != ' '):
            temVencedor = True
        
    for coluna in range(3):
        if (tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' '
            and tabuleiro[1][coluna] != ' ' and tabuleiro[2][coluna] != ' '):
            temVencedor = True

    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ' and tabuleiro[1][1] != ' '
        and tabuleiro[2][2] != ' '):
        temVencedor = True

    elif (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ' and tabuleiro[0][2] != ' '
        and tabuleiro[1][1] != ' ' and tabuleiro[2][0] != ' '):
        temVencedor = True
    
    # Verificação de todas as posições preenchidas    
    elif (tabuleiro[0][0] != ' ' and tabuleiro[0][1] != ' ' and tabuleiro[0][2] != ' '
    and tabuleiro[1][0] != ' ' and tabuleiro[1][1] != ' ' and tabuleiro[1][2] != ' '
    and tabuleiro[2][0] != ' ' and tabuleiro[2][1] != ' ' and tabuleiro[2][2] != ' '):
        print(f'Deu velha! O jogo se encerra')
        exit()

# Função de jogada do jogador 1
def jogador1():
    mostrar()
    jogada1X = int(input('Jogador 1 - Entre com a posição X: '))
    jogada1Y = int(input('Jogador 1 - Entre com a posição Y: '))

    if jogada1X < 0 or jogada1X > 2 or jogada1Y < 0 or jogada1Y > 2:
        print(f'Jogada inválida')
        clear()
        jogador1()
    elif tabuleiro[jogada1X][jogada1Y] != 'X' and tabuleiro[jogada1X][jogada1Y] != 'O':
        tabuleiro[jogada1X][jogada1Y] = 'X'
        clear()
    elif tabuleiro[jogada1X][jogada1Y] == 'O' or tabuleiro[jogada1X][jogada1Y] == 'X':
        clear()
        print(f'Posição já ocupada')
        jogador1()

# Função de jogada jogador 2
def jogador2():
    mostrar()
    jogada2X = int(input('Jogador 2 - Entre com a posição X: '))
    jogada2Y = int(input('Jogador 2 - Entre com a posição Y: '))
    
    if jogada2X < 0 or jogada2X > 2 or jogada2Y < 0 or jogada2Y > 2:
        print(f'Jogada inválida')
        jogador2()
    elif tabuleiro[jogada2X][jogada2Y] != 'X' and tabuleiro[jogada2X][jogada2Y] != 'O':
        tabuleiro[jogada2X][jogada2Y] = 'O'
        clear()
    elif tabuleiro[jogada2X][jogada2Y] == 'O' or tabuleiro[jogada2X][jogada2Y] == 'X':
        clear()
        print(f'Posição já ocupada')
        jogador2()
        
# Função de jogada da máquina
def maquina():
    mostrar()
    random.seed(time.time())
    jogadaMX = int(random.randrange(0, 3))
    jogadaMY = int(random.randrange(0, 3))
    print('A jogada da tentada foi:', jogadaMX, jogadaMY)

    if tabuleiro[jogadaMX][jogadaMY] != 'X' and tabuleiro[jogadaMX][jogadaMY] != 'O':
        tabuleiro[jogadaMX][jogadaMY] = 'O'
        clear()
    elif tabuleiro[jogadaMX][jogadaMY] == 'O' or tabuleiro[jogadaMX][jogadaMY] == 'X':
        clear()
        maquina()

# Modo de jogo jogador x jogador
if modoDeJogo == 2:
    temVencedor = False
    turno = 0 #0:jogador1, #1:jogador2
    # Verificação de vencedor linha/coluna/diagonal
    while not temVencedor:
        ganhador()
        # Verificação de vitória e jogada jogador 1
        if temVencedor == True and turno == 0:
            mostrar()
            print(f'O jogo encerrou com vitória do jogador 2')
            exit()
        elif turno == 0: #jogador1
            ganhador()
            jogador1()
            turno = 1
        
        # Verificação de vitória e jogada jogador 2
        else:
            if temVencedor == True and turno == 1:
                mostrar()
                print(f'O jogo encerrou com vitória do jogador 1')
                exit()
            elif turno == 1: #jogador2
                ganhador()
                jogador2()
                turno = 0

if modoDeJogo == 1:
    temVencedor = False
    turno = 0 #0:jogador1, #1:maquina
    while not temVencedor:
        ganhador()
        # Verificação de vitória e jogada jogador 1
        if temVencedor == True and turno == 0:
            mostrar()
            print(f'O jogo encerrou com vitória da máquina')
            exit()
        elif turno == 0: #jogador1
            ganhador()
            jogador1()
            turno = 1
    
        # Verificação de vitória e jogada máquina
        else:
            if temVencedor == True and turno == 1:
                mostrar()
                print(f'O jogo encerrou com vitória do jogador')
                exit()
            elif turno == 1: #maquina
                ganhador()
                maquina()
                turno = 0