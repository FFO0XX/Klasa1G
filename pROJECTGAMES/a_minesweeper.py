import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flagged = [[False for _ in range(cols)] for _ in range(rows)]
        self._place_mines()
        self._calculate_adjacent_counts()

    def _place_mines(self):
        while len(self.mine_positions) < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) not in self.mine_positions:
                self.mine_positions.add((row, col))
                self.board[row][col] = 'M'

    def _calculate_adjacent_counts(self):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 'M':
                    continue
                mine_count = 0
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == 'M':
                        mine_count += 1
                self.board[row][col] = str(mine_count) if mine_count > 0 else ' '

    def reveal(self, row, col):
        if self.revealed[row][col] or self.flagged[row][col]:
            return
        self.revealed[row][col] = True
        if self.board[row][col] == 'M':
            return 'Game Over'
        elif self.board[row][col] == ' ':
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    self.reveal(r, c)
        return 'Continue'

    def flag(self, row, col):
        self.flagged[row][col] = not self.flagged[row][col]

    def check_win(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.revealed[row][col] and self.board[row][col] != 'M':
                    return False
        return True

    def display(self):
        print("  " + " ".join(str(i) for i in range(self.cols)))
        for r in range(self.rows):
            row_display = []
            for c in range(self.cols):
                if self.flagged[r][c]:
                    row_display.append('F')
                elif not self.revealed[r][c]:
                    row_display.append('-')
                else:
                    row_display.append(self.board[r][c])
            print(f"{r} " + " ".join(row_display))

def play_game(rows, cols, mines):
    game = Minesweeper(rows, cols, mines)
    while True:
        game.display()
        if game.check_win():
            print("Congratulations! You've won!")
            break
        action = input("Enter action (reveal r c / flag r c): ").split()
        if len(action) != 3:
            print("Invalid action. Try again.")
            continue
        command, row, col = action[0], int(action[1]), int(action[2])
        if command == 'reveal':
            result = game.reveal(row, col)
            if result == 'Game Over':
                print("You hit a mine! Game Over.")
                game.display()
                break
        elif command == 'flag':
            game.flag(row, col)
        else:
            print("Invalid command. Use 'reveal' or 'flag'.")


