################################################################################
####################                Minesweeper             ####################
################################################################################
##########                                                            ##########
##########				Intermediate: 16x16,  40 bombs                ##########
##########                                                            ##########
##########                           Version 2                        ##########
##########                                                            ##########
##########                                                            ##########
################################################################################

import random

class Square:

    def __init__(self):
        self.content = 0
        self.face = "."
        self.bomb = False
        self.flag = False

class Game:
    def __init__(self, height, width, num_bombs):
        self.height = height
        self.width = width
        self.size = height*width
        self.num_bombs = num_bombs
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.revealed = 0
        self.game_on = True
        self.game_win = False

        self.matrix = []
        for i in range(0,self.size):
            self.matrix.append(Square())

        self.bombs = []
        while len(self.bombs) < num_bombs:

            i = random.randint(0,self.size-1)
            if i not in self.bombs:
                self.bombs.append(i)
                self.matrix[i].bomb = True
    
        for y in range(0,height):
            for x in range(0,width):

                count = 0
                for y2 in range(y-1,y+2):
                    for x2 in range(x-1,x+2):
                        if x2 in range(0,width) and y2 in range(0,height):
                            #print([count, x, y, y*width+x, x2, y2,y2*width + x2])
                            if self.matrix[y2*width + x2].bomb:
                                count += 1

                self.matrix[y*width + x].content = count       

    def print_board(self):
        
        print("#>" + self.letters[:self.width] + "<#")
        print("$+" + "-"*(self.width) + "+$")
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += str(self.matrix[y*self.height + x].face)
            print(self.letters[y] + "|" + row + "|" + self.letters[y])
        print(f"$+" + "-"*(self.width) + "+$")
        print("#>" + self.letters[:self.width] + "<#")

    def check_win(self):

        count = 0
        for i in range(self.size):
            if self.matrix[i].face == "F" or self.matrix[i].face == ".":
                count += 1
        if count == self.num_bombs:
            self.game_win = True
            self.game_on = False

    def click(self, coords):

        index = coords[1]*self.width + coords[0]
    
        if self.matrix[index].flag:
            return False
        else:
            if self.matrix[index].bomb:
                for i in self.bombs:
                    self.matrix[i].face = "X"
                self.game_on = False

            elif self.matrix[index].content > 0:
                self.matrix[index].face = str(self.matrix[index].content)
                self.check_win()
        
            else:
                self.matrix[index].face = "*"
                for y in range(coords[1]-1,coords[1]+2):
                    for x in range(coords[0]-1,coords[0]+2):
                        if x in range(0,self.width) and y in range(0,self.height) and self.matrix[y*self.width + x].face == ".":
                            self.click([x,y])
                self.check_win()

            return True
    
    def flag(self,coords):
        
        index = coords[1]*self.width + coords[0]
        if self.matrix[index].flag:
            self.matrix[index].face = "."
            self.matrix[index].flag = False
        else:
            self.matrix[index].face = "F"
            self.matrix[index].flag = True

def check_input(inp, game):

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
    if len(inp) == 3: 
        if inp[1] == "," and inp[0] in letters and inp[2] in letters:
            x = letters.index(inp[2])
            y = letters.index(inp[0])
            game.click([x,y])
            return True
    elif len(inp) == 8:
        if inp[1] == "," and inp[3] == "," and inp[0] in letters and inp[2] in letters and "FLAG" in inp:
            x = letters.index(inp[2])
            y = letters.index(inp[0])
            game.flag([x,y])
            return True
    return False
                            
board = Game(16,16,40)
repeat = False


while board.game_on:

    if not repeat:
        board.print_board()
        print("Input coordinates below (A,B) to click, (A,B,Flag) to place/remove Flag")
    repeat = False
    coordinates = input("Coordinates: ")

    inp_check = check_input(coordinates.upper(), board)
    if  not inp_check:

        print("Coordinates needs to be two uppercase letters seperated by a comma!")
        repeat = True   

board.print_board()
print("\n")
if board.game_win:
    print("Victory! B-)")
else:
    print("GAME OVER")