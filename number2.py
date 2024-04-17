import copy

class TicTacToe:
    def __init__(self):
        self.board = [[0, 0, 0] for _ in range(3)]  # Tabuleiro vazio
        self.current_player = 1  # Jogador 1 começa

    def is_winner(self, player):
        # Verifica se algum jogador venceu na linha, coluna ou diagonal
        return (any(all(cell == player for cell in row) for row in self.board) or  # Linhas
                any(all(row[i] == player for row in self.board) for i in range(3)) or  # Colunas
                all(self.board[i][i] == player for i in range(3)) or  # Diagonal principal
                all(self.board[i][2-i] == player for i in range(3)))  # Diagonal secundária

    def is_full(self):
        # Verifica se o tabuleiro está completamente preenchido
        return all(cell != 0 for row in self.board for cell in row)

    def is_terminal(self):
        # Verifica se o jogo acabou (vencedor ou empate)
        return self.is_winner(1) or self.is_winner(-1) or self.is_full()

    def legal_moves(self):
        # Retorna uma lista de todas as jogadas legais (posições vazias)
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def make_move(self, move):
        # Realiza uma jogada na posição especificada
        row, col = move
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player *= -1  # Alterna para o próximo jogador
            return True
        return False

    def print_board(self):
        # Imprime o tabuleiro
        for row in self.board:
            print(" ".join(["X" if cell == 1 else "O" if cell == -1 else "-" for cell in row]))
        print()

    def copy(self):
        # Cria uma cópia do jogo
        return copy.deepcopy(self)

def minimax(game):
    if game.is_terminal():
        if game.is_winner(1):
            return 1
        elif game.is_winner(-1):
            return -1
        else:
            return 0

    scores = []
    for move in game.legal_moves():
        new_game = game.copy()  # Copia o estado atual do jogo
        new_game.make_move(move)
        score = minimax(new_game)
        scores.append(score * game.current_player)

    if game.current_player == 1:
        return max(scores)
    else:
        return min(scores)

def alphabeta(game, alpha, beta):
    if game.is_terminal():
        if game.is_winner(1):
            return 1
        elif game.is_winner(-1):
            return -1
        else:
            return 0

    for move in game.legal_moves():
        new_game = game.copy()  # Copia o estado atual do jogo
        new_game.make_move(move)
        score = alphabeta(new_game, alpha, beta)
        if game.current_player == 1:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if beta <= alpha:
            break

    if game.current_player == 1:
        return alpha
    else:
        return beta

def player_minimax(game):
    best_score = float('-inf')
    best_move = None
    for move in game.legal_moves():
        new_game = game.copy()
        new_game.make_move(move)
        score = minimax(new_game)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def player_alphabeta(game):
    alpha = float('-inf')
    beta = float('inf')
    best_score = float('-inf')
    best_move = None
    for move in game.legal_moves():
        new_game = game.copy()
        new_game.make_move(move)
        score = alphabeta(new_game, alpha, beta)
        if score > best_score:
            best_score = score
            best_move = move
        alpha = max(alpha, best_score)
    return best_move

def play_game(player1, player2):
    game = TicTacToe()
    players = {1: player1, -1: player2}

    while not game.is_terminal():
        player = players[game.current_player]
        move = player(game)
        game.make_move(move)
        game.print_board()

    if game.is_winner(1):
        print("Jogador X venceu!")
    elif game.is_winner(-1):
        print("Jogador O venceu!")
    else:
        print("Empate!")

# Teste do jogo entre dois jogadores usando Mini-Max e Alfa-Beta
play_game(player_minimax, player_alphabeta)
