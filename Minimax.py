'''DESCRPTION OF CODE:The minimax function requires 6 arguments that are as follows:
position, depth, alpha, beta, max_player, game. The function implements the minimax algorithm with alpha beta pruning in a recursive way and is implemented as a python recursive function.
Position argument inputs the position of all pieces on the board. Depth defines the depth of the minimax algorithm that has to be traversed in order to find the optimal solution. 
Alpha and beta are the arguments for the alpha beta pruning part of the algorithm and are initially set to a very high negative and positive values and as python allows the use float(‘inf’), we set both alpha and beta to that. 
Max_player is the player whose maximizing move has to be selected and lastly game argument is the game object itself passed to the minimax function. 
The minimax function uses the evaluation method of the game object to get an evealuation/score for the human and AI and then use this as the evaluation metric in the minimax algorithm.'''

from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

def minimax(position, depth,alpha,beta, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1,alpha,beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha,evaluation)
            if beta<=alpha:
                break
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1,alpha,beta, True, game)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta,evaluation)
            if beta<=alpha:
                break
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()