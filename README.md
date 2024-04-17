# Actividade2-IA
TRABALHO DE CARACTER AVALIATIVO DE IA. 

Elementos de Grupo: Gildo Cumbane, Marcelina Pinto & Belísio Pateguana

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