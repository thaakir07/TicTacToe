import stdarray
import random
import stdio
import copy
import sys
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ''
from Gui import Gui

def main():
    game_type = int(sys.argv[1])
    size = 3
    stdio.writeln("Tic-Tac-Toe")
    game_board = create_board(size)
    game(game_board, size, game_type)

def game(game_board, size, game_type):
    print_board(game_board, size)
    gui = Gui()
    gui.create_board(game_board, False)
    moves = create_moves(size)
    print(moves)
    player = 1
    print("start game")

    while True:
        stdio.writeln("player " + str(player) + " enter move")
        if game_type == 1:
            move = stdio.readString()
        else: 
            if player == 1: 
                move = stdio.readString()
            else:
                move = ai_move(game_board, size)
                print(move)
        try:
            move = int(move)
        except ValueError:
            print(f"The input is not a valid move: {move}")
            continue
        move -= 1
        if isValidMove(game_board, move, moves, size):
            print("valid move")
            game_board = execute_move(game_board, move, player, moves)
            if check_winner(game_board, size, player):
                print_board(game_board, size)
                print("player " + str(player) + " wins")
                gui.create_board(game_board, True)
                break
            player = 2 if player == 1 else 1
        print_board(game_board, size)
        gui.create_board(game_board, False)
        
def check_winner(game_board, size, player):
    symbol = "X" if player == 1 else "O"
    
    row = 0
    col = 0
    count = 0
    #check rows
    print("checking rows")
    while row < size and col < size:
        if row == size-1 and count == 3:
            return True
        print(row, col)
        if game_board[row][col] == symbol:
            row += 1
            count += 1
            continue
        else: col += 1

    #check columns
    print("checking columns")
    row = 0
    col = 0
    count = 0
    while col < size:
        if game_board[row][col] == symbol:

            if row == size-1:
                return True
            row += 1
            continue
        else: col += 1

    #check right diagonals
    print("checking right diagonals")
    row = 0
    col = 0
    while row < size:
        if game_board[row][col] == symbol:
            if row == size-1 or col == size-1:
                return True
            row += 1
            col += 1
            continue
        else: break

    #check left diagonals
    print("checking left diagonals")
    row = 0
    col = size-1
    while row < size:
        if game_board[row][col] == symbol:
            if row == size or col == 0:
                return True
            row += 1
            col -= 1
            continue
        else: break

    return False

def isValidMove(game_board, move, moves, size):
    if isinstance(move, str):
        return False
    placement = moves[move]
    if move < 0 or move > size*size:
        return False
    elif game_board[placement[0]][placement[1]] == "X" or game_board[placement[0]][placement[1]] == "O":
        return False
    
    return True

def execute_move(game_board, move, player, moves):
    symbol = "O"
    if player == 1:
        symbol = "X"
    choice = moves[move]
    print(choice)
    game_board[choice[0]][choice[1]] = symbol
    return game_board

def print_board(game_board, size):
    for i in range(size):
        print(game_board[i])

def create_board(size):
    count = 1
    game_board = stdarray.create2D(size, size, ".")
    for i in range(size):
        for j in range(size):
            game_board[i][j] = count
            count += 1
    # game_board[0][0] = "O"
    return game_board

def create_moves(size):
    moves = []
    for i in range(size-1, -1, -1):
        for j in range(size):
            moves.append((i, j))
    return moves

def get_adjacent_moves(move, size):
    x, y = move
    adjacent_moves = [(x-1, y-1), (x-1, y), (x-1, y+1),
                      (x, y-1),           (x, y+1),
                      (x+1, y-1), (x+1, y), (x+1, y+1)]
    return [(i, j) for i, j in adjacent_moves if 0 <= i < size and 0 <= j < size]

def ai_move(game_board, size):
    moves = create_moves(size)

    #winning move
    for i in range(len(moves)):
        if isValidMove(game_board, i, moves, size):
            if check_winner(game_board, size, 2):
                return i
   
    #block opponent
    for i in range(len(moves)):
        if isValidMove(game_board, i, moves, size):
            move = moves[i]
            temp_board = copy.deepcopy(game_board)
            temp_board[move[0]][move[1]] = "X"  # Simulate opponent's move
            if check_winner(temp_board, size, 1):
                return i + 1

    #look for O
    for i in range(len(moves)):
        if isValidMove(game_board, i, moves, size):
            adjacent_moves = get_adjacent_moves(move, size)
            for i in range(len(adjacent_moves)):
                adj_move = adjacent_moves[i]
                if isValidMove(game_board, i, moves, size):
                    if game_board[adj_move[0]][adj_move[1]] == "O":
                        return i

    #look for a clear row
    for i in range(size*size):
        count = 0
        for j in range(3):
            if isValidMove(game_board, j, moves, size):
                count += 1
            else:
                if game_board[moves[j][0]][moves[j][1]] == "X":
                    count = 0
                else: count +1
            if count == size:
                return i
    
    #return a random move
    return moves.index(random.choice(moves))

if __name__ == "__main__": main()
