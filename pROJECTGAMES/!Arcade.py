from a_minesweeper import*
from a_tictactoe_connect4 import*



startscreen =""" ___________________________________________________
|                Welcome to the ARCADE              |
|                                                   |
|         WHAT GAME WOULD YOU LIKE TO PLAY?         |
|                                                   |
|                =>Minesweeper                      |
|                =>TicTacToe(2 players)             |
|                =>Connect4(2 players)              |
|                                                   |
|      to play write 'I want to play [gamename]'    |
|                   to exit write: 'IQuit'          |
|___________________________________________________|
    """

def whatgame(game):
    # game = input("what game would you like to play?: ").split()
    while True:
        if game[4] == "Minesweeper":
            play_game(11,11,10)
            break
        elif game[4] == "TicTacToe":
            tictactoe = TicTacToe()
            play_game_tictactoe_connect4(tictactoe)
            break
        elif game[4] == "Connect4":
            connect4 = Connect4()
            play_game_tictactoe_connect4(connect4)
            break
def arcade():
    print(startscreen)
    while True:
        game = input("what game would you like to play?: ").split()
        if game[0] == "IQuit":
            break
        else: 
            whatgame(game)

arcade()
