class Game:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (2 * self.cols - 1))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def check_winner(self):
        lines = []

        # Rows and Columns
        lines.extend(self.board)
        lines.extend([[self.board[r][c] for r in range(3)] for c in range(3)])

        # Diagonals
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0] == line[1] == line[2] and line[0] != ' ':
                return line[0]
        return None

class TicTacToe(Game):
    def __init__(self):
        super().__init__(3, 3)

    def check_winner(self):
        lines = []

        # Rows and Columns
        lines.extend(self.board)
        lines.extend([[self.board[r][c] for r in range(3)] for c in range(3)])

        # Diagonals
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0] == line[1] == line[2] and line[0] != ' ':
                return line[0]
        return None

class Connect4(Game):
    def __init__(self):
        super().__init__(6, 7)

    def make_move(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
        return False

    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == ' ':
                    continue
                for dr, dc in directions:
                    try:
                        if all(self.board[row + i * dr][col + i * dc] == self.board[row][col] for i in range(4)):
                            return self.board[row][col]
                    except IndexError:
                        continue
        return None

# Example usage:
def play_game_tictactoe_connect4(game):
    while True:
        game.display_board()
        if isinstance(game, TicTacToe):
            row, col = map(int, input(f"Player {game.current_player}, enter your move (row column): ").split())
            if game.make_move(row, col):
                if game.check_winner():
                    game.display_board()
                    print(f"Player {game.current_player} wins!")
                    break
                elif game.is_full():
                    game.display_board()
                    print("It's a draw!")
                    break
                game.switch_player()
            else:
                print("Invalid move. Try again.")
        elif isinstance(game, Connect4):
            col = int(input(f"Player {game.current_player}, enter your move (column[]): "))
            if game.make_move(col):
                if game.check_winner():
                    game.display_board()
                    print(f"Player {game.current_player} wins!")
                    break
                elif game.is_full():
                    game.display_board()
                    print("It's a draw!")
                    break
                game.switch_player()
            else:
                print("Invalid move. Try again.")

# print("Welcome to Tic Tac Toe")
# tic_tac_toe = TicTacToe()
# play_game(tic_tac_toe)

