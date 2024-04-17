# Actividade2-IA
TRABALHO DE CARACTER AVALIATIVO DE IA. 

Elementos de Grupo: Gildo Cumbane, Marcelina Pinto & Belísio Pateguana

-----------------------------------------------------------------------
Classe PuzzleNode:

Esta classe representa um nó no espaço de busca do quebra-cabeça.
__init__: O construtor da classe inicializa um nó com os seguintes atributos:
state: O estado atual do quebra-cabeça.
parent: O nó pai no espaço de busca (opcional).
action: A ação que levou a este estado (opcional).
g: O custo do caminho do estado inicial até o estado atual.
h: A heurística, que é uma estimativa do custo do estado atual até o estado final.
f: A soma do custo atual g e da heurística h.
__eq__, __hash__, __lt__: Estes métodos são definidos para permitir a comparação, o hash e a ordenação de objetos PuzzleNode.

Função h(state, goal_state):

Esta função define a heurística para o problema, que é o número de peças fora do lugar no estado atual em comparação com o estado final.
Função get_neighbors(state):
Esta função retorna os estados alcançáveis a partir do estado atual realizando movimentos válidos (cima, baixo, esquerda ou direita).
Primeiro, ela encontra a posição do espaço vazio no estado.
Em seguida, determina os movimentos possíveis a partir dessa posição e gera os novos estados resultantes desses movimentos.

Função find_zero_position(state):

Esta função encontra a posição do zero (espaço vazio) no estado atual.
Função generate_random_state(size):
Esta função gera um estado inicial aleatório.
Ela cria uma lista de números de 0 a size-1 e embaralha esses números para representar um estado inicial aleatório do quebra-cabeça.
Função a_star(start_state, goal_state):
Esta função implementa o algoritmo A* para encontrar a solução do quebra-cabeça.
Ela começa com um nó inicial contendo o estado inicial e sua heurística.
Usa uma lista open_list para manter os nós a serem explorados e um conjunto closed_set para manter os nós já explorados.
O algoritmo continua até que a open_list esteja vazia ou até que o estado final seja encontrado.
Para cada nó na open_list, encontra o nó com o menor custo total (f), remove-o da open_list e o adiciona ao closed_set.
Para cada estado vizinho, calcula o custo g e o valor da heurística h, cria um novo nó e o adiciona à open_list se ele ainda não estiver lá.
Retorna a solução (um nó) se for encontrada, caso contrário, retorna None.

Exemplo de Uso:

Gera um estado inicial aleatório e um estado final predefinido.
Chama a função a_star para encontrar a solução.
Se uma solução for encontrada, reconstrói o caminho da solução e imprime cada passo do caminho. Caso contrário, imprime que não foi encontrada uma solução.

-------------------------------------------------------------------------------

Classe TicTacToe:
Esta classe representa o jogo da velha.
__init__: Inicializa o tabuleiro vazio (uma lista de listas) e define o jogador atual como o jogador 1.
is_winner(player): Verifica se um jogador específico venceu o jogo, percorrendo as linhas, colunas e diagonais do tabuleiro.
is_full(): Verifica se o tabuleiro está completamente preenchido.
is_terminal(): Verifica se o jogo acabou, ou seja, se alguém venceu ou se o tabuleiro está cheio.
legal_moves(): Retorna uma lista de todas as jogadas legais disponíveis (posições vazias) no tabuleiro.
make_move(move): Realiza uma jogada na posição especificada no tabuleiro.
print_board(): Imprime o tabuleiro atual.

Função minimax(game):
Implementa o algoritmo Mini-Max para escolher a melhor jogada para um determinado jogador em um determinado estado do jogo.
A recursão ocorre até que o jogo termine.
Retorna o valor de utilidade (pontuação) do estado do jogo.

Função alphabeta(game, alpha, beta):
Implementa o algoritmo Alfa-Beta, que é uma melhoria do Mini-Max para tornar o algoritmo mais eficiente.
Usa os parâmetros alpha e beta para fazer poda alfa-beta.
Retorna o valor de utilidade (pontuação) do estado do jogo.
Funções player_minimax(game) e player_alphabeta(game):
Representam jogadores que utilizam os algoritmos Mini-Max e Alfa-Beta, respectivamente, para fazer suas jogadas.
Cada jogador avalia todas as jogadas legais disponíveis e escolhe aquela que maximiza sua pontuação de utilidade, simulando o jogo até o fim.

Função play_game(player1, player2):
Simula um jogo entre dois jogadores, onde player1 e player2 são funções que representam os jogadores que usam Mini-Max ou Alfa-Beta.
O jogo continua até que haja um vencedor ou até que o tabuleiro esteja cheio.
Imprime o tabuleiro após cada jogada.
No final do jogo, imprime o resultado (vitória de X, vitória de O ou empate).

Execução do Jogo:
Chama a função play_game com player_minimax e player_alphabeta como argumentos para simular um jogo entre dois jogadores que usam Mini-Max e Alfa-Beta, respectivamente.