'''DESCRIPTION OF CODE-
From lines 1 to 7, all libraries and helper scripts can be seen to be imported.
Minimax is the helper script from which minimax algorithm with alpha beta pruning is imported. Similarly, from checkers_helpers script various game constants and the game class is imported.
From lines 8 to 29, tkinter is used for making a selection window for the difficulty level of the checkers game. The difficulty level is selected using a popup window with various levels of difficulties that are selected using the radio buttons to the side of each selection.
Line 32 sets the frame per second of the game and lines 34 and 35 creates the window object for the game using pygame library in python3.7.
Lines 37 to 41 defines a function to get the row and column of the checkers board for the selected square on the board using mouse click.
From lines 43 to 73, the main function is defined which creates a game object and updates the game with each move of the player and when it is AI’s turn to play calls the minimax function to get appropriate and optimal action to take from all the action space.
Lastly, on line 75, the main function is called which starts the game of checkers.'''

import math
import pygame
from checkers_helpers import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers_helpers import Game
from Minimax import minimax
from tkinter import messagebox
from tkinter import Tk, Label, Button, Radiobutton, IntVar

def choose_difficulty(prompt, options):
    root = Tk()
    if prompt:
        Label(root, text=prompt).pack()
    v = IntVar()
    for i, option in enumerate(options):
        Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
    Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    return options[v.get()]

result = choose_difficulty(
    "Please choose the difficulty of the checkers game",
    [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]
)

# print(int(result))
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), int(result),-math.inf,math.inf, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            run = False
            if game.winner()==(255,255,255):
                messagebox.showinfo('','WHITE is the winner')
            else:
                messagebox.showinfo('','RED is the winner')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()