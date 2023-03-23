################################################################################
####################                Minesweeper             ####################
################################################################################
##########                                                            ##########
##########				Intermediate: 16x16,  40 bombs                ########## 
##########                                                            ##########
##########                                                            ##########
##########                                                            ##########
##########                                                            ##########
################################################################################

import time
import random 

game = True
game_setup = True
victory = False

class Grid:
	def __init__(self, height, width, fill=[0]):

		self.height = height
		self.width = width
		self.matrix = [(fill*width) for i in range(height)]
		self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def print_grid(self):

		print("#>" + self.letters[:self.width] + "<#")
		print("$+" + "-"*(self.width) + "+$")
		for i in range(self.height):
			print(self.letters[i] + "|" + str(self.matrix[i]) + "|" + self.letters[i])
		print(f"$+" + "-"*(self.width) + "+$")
		print("#>" + self.letters[:self.width] + "<#")


def place_bombs(grid, num_bombs):

	bombs = []

	while len(bombs) < num_bombs:

		x = random.randint(0,15)
		y = random.randint(0,15)
		if [x, y] not in bombs:

			bombs.append([x, y])
			grid.matrix[x][y] = 9

	return grid, bombs;

def generate_numbers(grid, bombs):

	height = grid.height
	width = grid.width

	for x in range(0,height):
		for y in range(0, width):

			count = 0
			if [x, y] not in bombs:	
				for x2 in range(x-1, x+2):
					for y2 in range(y-1, y+2):
						if x2 in range(0,height) and y2 in range(0, width):
							if [x2, y2] in bombs:
								count += 1

				grid.matrix[x][y] = count

	return grid

def check_input(inp):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if len(inp) == 3: 
		if inp[1] == "," and inp[0] in letters and inp[2] in letters:
			return True
	elif len(inp) == 8:
		if inp[1] == "," and inp[3] == "," and inp[0] in letters and inp[2] in letters and "FLAG" in inp:
			return True
	return False

def change_square(shown, coords, new):

	temp = list(shown.matrix[coords[0]])
	temp[coords[1]] = str(new)
	shown.matrix[coords[0]] = "".join(temp)
	return shown

def click(grid, shown, coordinates, bombs):

	height = grid.height
	width = grid.width

	x_coord = grid.letters.index(coordinates[0])
	y_coord = grid.letters.index(coordinates[2])

	clicked = grid.matrix[x_coord][y_coord]
	clicked_shown = shown.matrix[x_coord][y_coord]

	if len(coordinates) == 8:
		
		if shown.matrix[x_coord][y_coord] == "F":
			shown = change_square(shown,[x_coord,y_coord],".")
		elif shown.matrix[x_coord][y_coord] ==".":
			shown = change_square(shown,[x_coord,y_coord],"F")

	elif clicked == 9 and clicked_shown != "F":

		for bomb in bombs:

			shown = change_square(shown, bomb, "X")

		global game
		game = False

	elif clicked == 0 and clicked_shown != "F": 
		
		shown = change_square(shown, [x_coord,y_coord], "*")
		checking = True
		while checking:

			count = 0
			for x in range(0,height):
				for y in range(0, width):

					if shown.matrix[x][y] == "*":	
						for x2 in range(x-1, x+2):
							for y2 in range(y-1, y+2):
								if x2 in range(0,height) and y2 in range(0, width):
								
									if shown.matrix[x2][y2] == ".":
										count += 1
										if grid.matrix[x2][y2] == 0:
											shown = change_square(shown, [x2,y2], "*")
										else:
											shown = change_square(shown, [x2,y2], grid.matrix[x2][y2])
			print(count)
			shown.print_grid()
			if count == 0:
				checking = False						


	elif clicked_shown != "F":

		shown = change_square(shown, [x_coord,y_coord], clicked)

	return shown

def check_if_victory(shown, num_bombs):

	count = 0
	for x in range(0, shown.height):
		for y in range(0, shown.width):		

			if shown.matrix[x][y] == "."  or shown.matrix[x][y] == "F":
				count += 1
	if count == num_bombs:
		global game
		game = False
		return True
	else:
		return False
		
### Main Loop ###

while game:
	
	if game_setup:
	
		height = 16
		width = 16
		number_of_bombs = 40

		board = Grid(height,width)
		revealed  = Grid(height,width,".")
		board, bombs = place_bombs(board, number_of_bombs)
		board = generate_numbers(board, bombs)
		
		board.print_grid()
		revealed.print_grid()
		print("Input coordinates below (A,B) to click, (A,B,Flag) to place/remove Flag")
		game_setup = False

	coordinates = input("Coordinates: ")

	if check_input(coordinates.upper()):

		revealed = click(board, revealed, coordinates.upper(), bombs)
		revealed.print_grid()
		print("Input coordinates below (A,B) to click, (A,B,Flag) to place/remove Flag")
		victory = check_if_victory(revealed,number_of_bombs)
		
	else:
		print("Coordinates needs to be two uppercase letters seperated by a comma!")

print("\n")
if victory:
	print("Victory! B-)")
else:
	print("GAME OVER")