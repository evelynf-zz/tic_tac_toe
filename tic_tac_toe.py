# Implement tic, tac, toe
# Write a board class that supports:
# print method
# method that places a marker of a certain type (X or O on the board)
# method that checks win condition
# method that checks for tie
# method that randomly places tile of a certain type on the board
# allows for someone to play against random player 

import random 
class GameBoard:

	def __init__(self, size):
		self.board = [['E' for i in range(size)] for j in range(size)]
		self.size = size
	def play(self, x_y_tup, value):
		(x, y) = x_y_tup
		assert(x < self.size and x >= 0)
		assert(y < self.size and y >= 0)
		assert(value == 'X' or value == 'O')
		if (len(self.check_winners()) == 0):
			if self.board[x][y] == 'E':
				self.board[x][y] = value
			else:
				return "This space is not empty"
		else:
			return self.check_game()
 
	def check_rows(self):
		#returns the winners or an empty set if none
		winners = set() #in case there is a tie return two
		for r in range(self.size):
			x_count = 0
			o_count = 0
			for c in range(self.size):
				if self.board[r][c] == 'X':
					x_count +=1
				elif self.board[r][c] == 'O':
					o_count +=1
			if x_count == self.size:
				winners.add('X')
			if o_count == self.size:
				winners.add('O')
		return winners

	def check_cols(self):
		#returns the winners or an empty set if none
		winners = set() #in case there is a tie return two
		for c in range(self.size):
			x_count = 0
			o_count = 0
			for r in range(self.size):
				if self.board[r][c] == 'X':
					x_count +=1
				elif self.board[r][c] == 'O':
					o_count +=1
			if x_count == self.size:
				winners.add('X')
			if o_count == self.size:
				winners.add('O')
		return winners

	def check_left_diagonal(self):
		#returns the winners or an empty set if none
		winners = set() #in case there is a tie return two
		for i in range(self.size):
			x_count = 0
			o_count = 0
			if self.board[i][i] == 'X':
				x_count +=1
			elif self.board[i][i] == 'O':
				o_count +=1
		if x_count == self.size:
			winners.add('X')
		if o_count == self.size:
			winners.add('O')
		return winners
	def check_right_diagonal(self):
		winners = set() #in case there is a tie return two
		i = self.size - 1
		while i >= 0:
			x_count = 0
			o_count = 0
			if self.board[i][i] == 'X':
				x_count +=1
			elif self.board[i][i] == 'O':
				o_count +=1
			i -= 1
		if x_count == self.size:
			winners.add('X')
		if o_count == self.size:
			winners.add('O')
		return winners

	# determines if there is a winner, tie or nothing
	def check_winners(self):
		winners = set()
		winners = winners.union(self.check_rows())
		winners = winners.union(self.check_cols())
		winners = winners.union(self.check_left_diagonal())
		winners = winners.union(self.check_right_diagonal())
		return winners

	def check_game(self):
		winners = self.check_winners()
		if len(winners) == 0:
			return "No winner yet! Keep playing!"
		elif len(winners) == 2:
			return "There's a tie!"
		else:
			return "The winner is: " + winners.pop()

	def print_board(self):
		# print 3 '-' between every row
		# print 1 '|' between every column
		board_string = ''
		for r in range(self.size - 1):
			for c in range(self.size - 1):
				board_string += self.board[r][c] + ' | '
			# add last col without '|'
			board_string += self.board[r][self.size-1]
			board_string += '\n' + '---'*self.size + '\n'
		# add last row without '--'
		for c in range(self.size - 1):
			board_string += self.board[self.size - 1][c] + ' | '
		# add last col without '|'
		board_string += self.board[self.size-1][self.size-1]
		return board_string

	def get_empty_spots(self):
		empty_spots = []
		for r in range(self.size):
			for c in range(self.size):
				if self.board[r][c] == 'E':
					empty_spots.append((r, c))
		return empty_spots

	def random(self, value):
		empty_spots = self.get_empty_spots()
		if len(empty_spots) > 0:
			spot = random.choice(empty_spots)
			return self.play(spot, value)
		else:
			return "No empty spaces"

	def random_player(self):
		value = random.choice(['X', 'O'])
		return self.random(value)


A = GameBoard(3)
A.play((1, 2), "X")

# print(A.print_board())
A.random_player()
# print(A.print_board())
A.random_player()
print(A.print_board())
print(A.check_game())
A.random_player()
print(A.print_board())
A.random_player()
print(A.print_board())
A.random_player()
print(A.print_board())
A.random_player()
print(A.print_board())
print(A.check_game())
