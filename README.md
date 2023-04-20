# Jogo da Velha em Python
Esta é uma implementação simples do clássico jogo da Velha em Python. Neste jogo, a máquina sempre fará uma jogada em um local aleatório no tabuleiro.
O jogo pode ser jogado como "Jogador vs Jogador" ou "Jogador vs Máquina"

## Como Jogar
1. Clone este repositório em sua máquina local.
2. Navegue até o diretório onde o repositório foi clonado.
3. Execute `python tic_tac_toe.py` no seu prompt de comando/terminal.
4. O jogo irá perguntar o modo de jogo.
5. O jogo começará e você será solicitado a fazer sua primeira jogada.
6. A máquina fará sua jogada e o jogo continuará até que um jogador vença ou o tabuleiro esteja cheio.

## Características
- O jogo é jogado em uma simples interface de linha de comando.
- O jogo suporta o modo PvP.
- A máquina faz uma jogada aleatória a cada rodada.

## Funções Utilizadas
As seguintes funções são utilizadas na implementação deste jogo:
- `display_board()`: Exibe o tabuleiro do jogo da Velha na interface de linha de comando.
- `play_game()`: A função principal que lida com a lógica e o fluxo do jogo.
- `handle_turn(player)`: Lida com a vez do jogador e coloca sua jogada no tabuleiro.
- `check_rows()`, `check_columns()`, `check_diagonals()`: Funções auxiliares que verificam o tabuleiro em busca de uma condição de vitória.

## Contribuição
Contribuições são sempre bem-vindas! Se você tiver alguma sugestão ou correção a fazer, sinta-se à vontade para abrir uma issue ou um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

