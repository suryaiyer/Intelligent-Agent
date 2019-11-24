

from eval_functions import available_actions, terminal_test, utility, calculate_score, action
from Minimax import minimax
from abpruning import alpha_beta
from h_minimax import hminimax_decision
from h_abpruning import halpha_beta
import sys
import time
import random

# Fill 2D board array based on number of pits specified
def create_board(board, pits):
    board = [[0] * (pits + 2) for i in range(2)]
    return board

# Print visual representation of board array
def print_board(state, pits):
    str1beg = "  St    "
    str2beg = "  P0   "
    str1mid = ""
    str2mid = ""
    p1mid = ""
    p2mid = ""
    p1beg = "| " + str('%02d' % state[0][pits + 1]) + " ||"
    p2beg = "| " + str(state[1][0]) + " ||"
    for i in range(pits, 0, -1):
        str1mid = str1mid + " " + '%02d' % i + "  "
        str2mid = str2mid + " " + '%02d' % (pits + 1 - i) + "  "
        p1mid = p1mid + ' ' + '%02d' % state[0][i] + " |"
        p2mid = p2mid + ' ' + '%02d' % state[1][pits + 1 - i] + " |"
    str1end = " Pl  "
    str2end = " St  "
    p1end = "| " + str(state[0][0]) + " |"
    p2end = "| " + str('%02d' % state[1][pits + 1]) + " |"

    str1_final = str1beg + str1mid + str1end
    str2_final = str2beg + str2mid + str2end
    p1_final = p1beg + p1mid + p1end
    p2_final = p2beg + p2mid + p2end

    length = len(p1_final)

    line = ""
    for i in range(length):
        line = line + "-"

    print(str1_final)
    print(line)
    print(p1_final)
    print(line)
    print(p2_final)
    print(line)
    print(str2_final)

# Fill board with specified number of stones
def init_board(board, n, pits):
    for i in range(0, 2):
        for j in range(1, pits + 1):
            board[i][j] = n

# Recursively play game of mancala until a terminal case is reached
def play_mancala(player, pits, board, f):
	print_board(board, pits)

	print("Player ", player, " turn")
	possible_moves = available_actions(board, player, pits)

	print("You can play the following moves", *possible_moves, sep=', ')

	if not terminal_test(board, pits):
		if board[player][0] == 'hu':  # Human player
			while True:
				move = input("Please enter your move\n")
				if int(move) in possible_moves:
					break
				else:
					print("Invalid move, you can play the following moves", *possible_moves, sep=',')
					continue

		elif board[player][0] == 'ra':    # Random player
			move = random.choice(possible_moves)

		elif board[player][0] == 'mi':    # Minimax player
			if len(possible_moves) == 1:
				move = possible_moves[0]
				count = 0
			else:
				move,count = minimax(board, player, pits)
			f.write("Number of states searched is " + str(count) + "\n")

		elif board[player][0] == 'ab':    # Alpha Beta Pruning player
			if len(possible_moves) == 1:
				move = possible_moves[0]
				count = 0
			else:
				move,count = alpha_beta(board, player, pits)

			f.write("Number of states searched is " + str(count) +"\n")

		elif board[player][0] == 'hm':    # Heuristic Minimax player
			if len(possible_moves) == 1:
				move = possible_moves[0]
				count = 0
			else:
				move,count = hminimax_decision(board, player, possible_moves, pits, 10)
			f.write("Number of states searched is " + str(count) +"\n")

		elif board[player][0] == 'ha':    # Heuristic Alpha Beta Pruning player
			if len(possible_moves) == 1:
				move = possible_moves[0]
				count = 0
			else:
				move,count = halpha_beta(board, player, pits, 10)
			f.write("Number of states searched is " + str(count) +"\n")


		print("Player", player, " plays ->", int(move))
		f.write("Player " + str(player) + " plays -> " + str(move) + "\n\n")
		move = int(move)
		player, state = action(player, move, board, pits)
		board = state
		play_mancala(player, pits, board, f)  # Play next move

	else:  # Terminal case reached
		p0, p1 = calculate_score(board, pits)

		if p0 > p1:
			print("p0 wins with score", p0, " - ", p1)
			f.write("player 0 wins with score " + str(p0) + " - " + str(p1) + "\n\n")
		elif p0 < p1:
			print("p1 wins with score", p1, " - ", p0)
			f.write("player 1 wins with score " + str(p1) + " - " + str(p0) + "\n\n")
		else:
			print("scores tied", p0, " - ", p1)
			f.write("Scores tied " + str(p1) + " - " + str(p0) + "\n\n")


def main():
    start_time = time.time()
    print("Welcome to Mancala")
    print("The start time is", time.gmtime())

    player1 = sys.argv[1]
    player0 = sys.argv[2]
    filename = sys.argv[3]

    f = open(filename, "w")

    f.write("The Start time is " + str(start_time) + "\n\n")

    k = input("Please enter your choice of number of pits for each player: ")
    k = int(k)
    board = []
    board = create_board(board, k)  # Create board with specified number of pits

    f.write("Number of pits for each player is " + str(k) + "\n")

    board[1][0] = player1[0] + player1[1]
    board[0][0] = player0[0] + player0[1]

    n = input("Please enter your choice of number of stones in the initial State: ")
    n = int(n)
    print("n is ", n)

    f.write("Number of stones in each pit initially is " + str(n) + "\n\n")

    init_board(board, n, k) # Fill board with stones

    play_mancala(1, k, board, f)
    print("End time is ", time.gmtime())
    print("--- %s seconds ---" % (time.time() - start_time))
    f.write("End time is " + str(time.gmtime()) + "\n")
    f.write("The total time in  seconds is " + str(time.time() - start_time))

    f.close()


if __name__ == "__main__":
    main()
