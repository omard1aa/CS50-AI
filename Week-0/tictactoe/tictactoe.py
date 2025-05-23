"""
Tic Tac Toe Player
"""

import math

EMPTY = None
def initial_state():
    """
    Returns starting state of the board.
    """
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    return board


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nonEmptyCells = [1 for row in board for cell in row if cell is not None]
    return "O" if len(nonEmptyCells) % 2 != 0 else "X"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell is  None}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x, y = action
    if x > 2 or x < 0 or y > 2 or y < 0:
        raise Exception("Invalid move: Out of bounds")
 
    if board[x][y] is not None:
        raise Exception("Invalid move, Cell already taken") 
    
    board[x][y] = player(board)
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1: return 'X'
    elif utility(board) == -1: return 'O'
    elif(utility(board)) == 0: return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    vCheck = checkVertically(board)
    hCheck = checkHorizontally(board)
    dCheck = checkDiagonally(board)
    if hCheck != None:
        if hCheck == "X":
            return 1
        if hCheck == "O":
            return -1
        
    if vCheck != None:
        if vCheck == "X":
            return 1
        if vCheck == "O":
            return -1
            
    if dCheck != None:
        if dCheck == "X":
            return 1
        if dCheck == "O":
            return -1
    return 0    


def checkHorizontally(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != None:
            return row[0]
    return None


def checkVertically(board):
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != None:
            return board[0][column]
    return None


def checkDiagonally(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
        return board[0][2]
    return None


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == 'X':
        return getXBestMove(board)[1]

    elif player(board) == 'O':
        return getYBestMove(board)[1]

def getXBestMove(board):
    optimalMove = ()
    if terminal(board):
        return utility(board), optimalMove
    possibleActions = {}
    x = float('-inf')
    for action in actions(board):
        newBoard = result(board, action)
        x = max(x, getYBestMove(newBoard)[0])
        possibleActions[x] = action
    return max(possibleActions.keys()), possibleActions[min(possibleActions.keys())]

def getYBestMove(board):
    optimalMove = ()
    if terminal(board):
        return utility(board), optimalMove
    possibleActions = {}
    y = float('inf')
    for action in actions(board):
        newBoard = result(board, action)
        y = min(y, getXBestMove(newBoard)[0])
        possibleActions[y] = action
    return min(possibleActions.keys()), possibleActions[min(possibleActions.keys())]

    