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

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def place_bombs(grid, height, length, num_bombs):

	bombs = []

	while len(bombs) < num_bombs:

		x = random.randint(0,15)
		y = random.randint(0,15)
		if [x, y] not in bombs:

			bombs.append([x, y])
			grid[x][y] = 9

	return grid, bombs;

def generate_numbers(grid, height, length, bombs):

	for x in range(0,height):
		for y in range(0, length):

			count = 0

			if [x, y] not in bombs:

				# First the corners
				if x == 0 and y == 0:
					grid[x][y] = bombs.count([0, 1]) + bombs.count([1, 0]) + bombs.count([1, 1])

				elif x == 0 and y == length-1:
					grid[x][y] = bombs.count([0, length-2]) + bombs.count([1, length-2]) + bombs.count([1, length-1])

				elif x == height-1 and y == 0:
					grid[x][y] = bombs.count([height-2, 0]) + bombs.count([height-2, 1]) + bombs.count([height-1, 1])

				elif x == height-1 and y == length-1:
					grid[x][y] = bombs.count([height-2, length-2]) + bombs.count([height-1, length-2]) + bombs.count([height-2, length-1])

				# Next the edges
				elif x == 0:
					for x2 in range(x-1, x+2):
						for y2 in range(y, y+2):

							if [x2, y2] in bombs:
								count += 1

					grid[x][y] = count

				elif x == height-1:
					for x2 in range(x-1, x+2):
						for y2 in range(y-1, y+1):

							if [x2, y2] in bombs:
								count += 1

					grid[x][y] = count

				elif y == 0:
					for x2 in range(x, x+2):
						for y2 in range(y-1, y+2):

							if [x2, y2] in bombs:
								count += 1

					grid[x][y] = count

				elif y == length-1:
					for x2 in range(x-1, x+1):
						for y2 in range(y-1, y+2):

							if [x2, y2] in bombs:
								count += 1

					grid[x][y] = count

				# Lastly everything else
				else:
					for x2 in range(x-1, x+2):
						for y2 in range(y-1, y+2):

							if [x2, y2] in bombs:
								count += 1


					grid[x][y] = count

	return grid

def check_input(inp):
	if len(inp) == 3: 
		if inp[1] == "," and inp[0] in letters and inp[2] in letters:
			return True
	elif len(inp) == 8:
		if inp[1] == "," and inp[3] == "," and inp[0] in letters and inp[2] in letters and "FLAG" in inp:
			return True
	return False

def click(grid, shown, coordinates, bombs):

	x_cord = letters.index(coordinates[2])
	y_cord = letters.index(coordinates[0])

	clicked = grid[x_cord][y_cord]
	clicked_shown = shown[x_cord][y_cord]
	if len(coordinates) == 8:
		
		temp = list(shown[x_cord])
		if shown[x_cord][y_cord] == "F":
			temp[y_cord] = "."
			shown[x_cord] = "".join(temp)
		elif shown[x_cord][y_cord] ==".":
			temp[y_cord] = "F"
			shown[x_cord] = "".join(temp)
		return shown

	elif clicked == 9 and clicked_shown != "F":

		for bomb in bombs:
			temp = list(shown[bomb[0]])
			temp[bomb[1]] = "X"
			shown[bomb[0]] = "".join(temp)

			global game
			game = False

		return shown

	elif clicked_shown != "F":

		temp = list(shown[x_cord])
		temp[y_cord] = str(clicked)
		shown[x_cord] = "".join(temp)
		return shown

	else:

		return shown

def print_game(shown, height, length, check):

	back = "\033[F"
	# This line is to clear the input line 
	print(f"""{back}                           """)

	back = "\033[F" * (height + 8)

	print(f"""{back}
#>""" + letters[:length] + "<#")
	print("$+" + "-"*(length) + "+$")
	for i in range(height):
		print(letters[i] + "|" + shown[i] + "|" + letters[i])
	print(f"$+" + "-"*(length) + "+$")
	print("#>" + letters[:length] + "<#                            ")
	if check:
		print("Input coordinates below (A,B) to click, (A,B,Flag) to place/remove Flag")
	else:
		print("Coordinates needs to be two uppercase letters seperated by a comma!              ")

### Main Loop ###

while game:
	
	if game_setup:
	
		height = 16
		length = 16

		board = [([0]*length) for i in range(height)]
		revealed  = [("."*length) for i in range(height)]
		board, bombs = place_bombs(board, height, length, 40)
		board = generate_numbers(board, height, length, bombs)
		
		print(bombs[0])
		print("\n" * 5)
		print("#>" + letters[:length] + "<#")
		print("$+" + "-"*(length) + "+$")
		for i in range(height):
			print(letters[i] + "|" + revealed[i] + "|" + letters[i])
		print(f"$+" + "-"*(length) + "+$")
		print("#>" + letters[:length] + "<#")
		print("Input coordinates below (A,B) to click, (A,B,Flag) to place/remove Flag")
		game_setup = False

	coordinates = input("Coordinates: ")

	if check_input(coordinates.upper()):

		revealed = click(board, revealed, coordinates.upper(), bombs)
		print_game(revealed, height, length, True)

	else:	
		print_game(revealed, height, length, False)



print("\n")
print("GAME OVER")