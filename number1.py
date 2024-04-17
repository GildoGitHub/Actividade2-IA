import random

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g  # custo do caminho do estado inicial até o estado atual
        self.h = h  # heurística (custo estimado do estado atual até o estado final)
        self.f = g + h

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def __lt__(self, other):
        return self.f < other.f

def h(state, goal_state):
    """Heurística: conta o número de peças fora do lugar."""
    return sum(1 for i, j in zip(state, goal_state) if i != j)

def get_neighbors(state):
    """Obtém os estados alcançáveis a partir do estado atual."""
    neighbors = []
    zero_row, zero_col = find_zero_position(state)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimentos possíveis: direita, esquerda, baixo, cima
    for dr, dc in moves:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]  # Criando uma cópia do estado atual
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]  # Troca as posições
            neighbors.append(new_state)
    return neighbors

def find_zero_position(state):
    """Encontra a posição do zero (espaço vazio) no estado."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_random_state(size):
    """Gera um estado inicial aleatório."""
    state = list(range(size))  # Gerando números de 0 a size-1
    random.shuffle(state)
    return [state[i:i+3] for i in range(0, size, 3)]  # Divide a lista em sublistas de tamanho 3

def a_star(start_state, goal_state):
    open_list = [PuzzleNode(start_state, g=0, h=h(start_state, goal_state))]
    closed_set = set()

    while open_list:
        current_node = min(open_list)
        open_list.remove(current_node)

        if current_node.state == goal_state:
            # Encontrou o estado final
            return current_node

        closed_set.add(tuple(map(tuple, current_node.state)))

        for neighbor_state in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor_state)) in closed_set:
                continue

            g = current_node.g + 1  # Custo de movimento é sempre 1
            h_value = h(neighbor_state, goal_state)
            new_node = PuzzleNode(neighbor_state, parent=current_node, action=None, g=g, h=h_value)

            if new_node not in open_list:
                open_list.append(new_node)

    return None  # Não encontrou solução

# Exemplo de uso:
start_state = generate_random_state(9)  # Estado inicial aleatório
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Estado final
solution = a_star(start_state, goal_state)

if solution:
    # Reconstrói o caminho da solução
    path = []
    while solution:
        path.append(solution.state)
        solution = solution.parent
    path.reverse()

    # Imprime o caminho
    for i, state in enumerate(path):
        print(f"Passo {i}:")
        for row in state:
            print(row)
        print()
else:
    print("Não foi encontrada uma solução.")
