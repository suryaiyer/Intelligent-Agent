# Return possible actions at given state and player
def available_actions(state, player, pits):
    possible_moves = []
    for i in range(1, pits + 1):
        if state[player][i] > 0:
            possible_moves.append(i)
    return possible_moves


# Test state to see if it indicates that the game is over
def terminal_test(state, pits):
    sum = [0, 0]
    for i in range(2):
        for j in range(1, pits + 1):
            sum[i] = sum[i] + state[i][j]

    if sum[0] == 0 or sum[1] == 0:
        return True
    else:
        return False

# Define utility of output
def utility(state, pits, initial_max):
    p0, p1 = calculate_score(state, pits)
    if initial_max == 0:  # Return utility if player0 is MAX
        return p0 - p1
    else:  # Return utility if player1 is MAX
        return p1 - p0

# Calculate each players score based on number of stones in pits and stores
def calculate_score(board, pits):
    player0_score = 0
    player1_score = 0
    for y in range(1, pits + 2):
        player0_score = player0_score + board[0][y]
        player1_score = player1_score + board[1][y]
    return player0_score, player1_score

# Perform specified move on game board, return next player and state
def action(player, move, state, pits):
    stones_total = state[player][move]
    state[player][move] = 0
    x = player
    y = move

    while stones_total > 1:
        if y < pits:   # If in middle then do normally
            y = y + 1
            state[x][y] = state[x][y] + 1
            stones_total = stones_total - 1

        elif y == pits:
            if x == player:  # If the axis is that of the player go to store
                y = y + 1
                state[x][y] = state[x][y] + 1
                stones_total = stones_total - 1
                y = 0
                x = 1 - x

            else:  # If Not in axis of the player switch axis
                y = 1
                x = 1 - x
                state[x][y] = state[x][y] + 1
                stones_total = stones_total - 1

    if y == pits:
        if x == player:  # If the axis is that of the player go to store
            y = y + 1
            state[x][y] = state[x][y] + 1
            return (player, state)  # If ending stone is on store return player

        else:  # If Not in axis of the player switch axis
            y = 1
            x = 1 - x
            if state[x][y] == 0:  # if empty put opp box into store
                state[x][pits + 1] = state[x][pits + 1] + state[1 - x][pits + 1 - y]
                state[1 - x][pits + 1 - y] = 0
            state[x][y] = state[x][y] + 1
            return (1 - player, state)

    else:
        y = y + 1
        if x == player:
            if state[x][y] == 0:
                if state[1 - x][pits + 1 - y] > 0:
                    state[x][pits + 1] = state[x][pits + 1] + state[1 - x][pits + 1 - y] + 1
                    state[1 - x][pits + 1 - y] = 0
                else:
                    state[x][y] = state[x][y] + 1
            else:
                state[x][y] = state[x][y] + 1
        else:
            state[x][y] = state[x][y] + 1

        return 1 - player, state
