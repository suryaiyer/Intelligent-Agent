from eval_functions import available_actions, terminal_test, utility, calculate_score, action
import math

count = 0

# Calculate heuristic based on number of empty pits on players side
def evaluate(state, pits, p_o):
    p0, p1 = calculate_score(state, pits)

    gaps_p = 0
    gaps_o = 0

    for i in range(1, pits + 1):
        if state[p_o][i] == 0:
            gaps_p = gaps_p + i / 3

        if state[1 - p_o][i] == 0:
            gaps_o = gaps_o + i / 3

        if p_o == 0:
            return (p0 - p1) + (gaps_p - gaps_o)
        else:
            return (p1 - p0) + (gaps_p - gaps_o)

# Return action that maximizes players chance of winning based on heuristic minimax algorithm
def hminimax_decision(state, player, possible_move, pits, d):
	print("Player m is ", player)
	player_initial = player
	utility = []
	global count
	for move in possible_move:
		new_state = [row[:] for row in state]
		player, new_state_1 = action(player_initial, move, new_state, pits)

		if player == player_initial:
			utility.append(hmaxvalue(new_state_1, player, pits, player_initial, d))

		else:
			utility.append(hminvalue(new_state_1, player, pits, player_initial, d))

	move = 0

	for i in range(len(utility)):
		if utility[i] > utility[move]:
			move = i
	count_final =count
	count =0
	return possible_move[move],count_final

# Return utility of the state given that player is MIN
def hminvalue(state, player, pits, p_o, d):
    global count
    count = count + 1
    v = math.inf
    player_initial = player

    if d == 0:  # Reached depth threshold, evaluate heuristic
        return evaluate(state, pits, p_o)

    if not terminal_test(state, pits):

        actions = available_actions(state, player, pits)

        for move in actions:
            new_state = [row[:] for row in state]
            player, new_state_1 = action(player_initial, move, new_state, pits) # Check resulting state of each action
            if player == player_initial:    # If same player, perform hminvalue again
                v = min(v, hminvalue(new_state_1, player, pits, p_o, d - 1))

            else:                           # If player changes, perform hmaxvalue
                v = min(v, hmaxvalue(new_state_1, player, pits, p_o, d - 1))

    else:   # Terminal case reached, return utility
        return utility(state, pits, p_o)

    return v

# Return utility of the state given that player is MAX
def hmaxvalue(state, player, pits, p_o, d):
	global count
	count = count + 1
	v = -(math.inf)
	player_initial = player

	if d == 0: # Reached depth threshold, evaluate heuristic
		return evaluate(state, pits, p_o)

	if not terminal_test(state, pits):

		actions = available_actions(state, player, pits)

		for move in actions:
			new_state = [row[:] for row in state]
			player, new_state_1 = action(player_initial, move, new_state, pits)  # Check resulting state of each action
			if player == player_initial:     # If same player, perform hmaxvalue again
				v = max(v, hmaxvalue(new_state_1, player, pits, p_o, d - 1))

			else:                            # If player changes, perform hminvalue
				v = max(v, hminvalue(new_state_1, player, pits, p_o, d - 1))

	else:      # Terminal case reached, return utility
		return utility(state, pits, p_o)

	return v
