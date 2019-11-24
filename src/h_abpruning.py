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

# Return action that maximizes players chance of winning based on heuristic alpha beta pruning algorithm
def halpha_beta(state, player, pits, d):
    global count
    actions = available_actions(state, player, pits)
    max_action = 0
    initial_max = player  # Define initial MAX player for purpose of defining utility
    u = -math.inf
    alpha = -math.inf
    beta = math.inf
    for a in actions:
        player_copy = player
        state_copy = [row[:] for row in state]
        result_player, result_state = action(player_copy, a, state_copy, pits)  # Check resulting state of each action
        if result_player == player:  # Run max_value if next player is MAX
            u_a = hmax_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta, d)
            if u < u_a:
                u = u_a
                max_action = a
            alpha = max(u_a, alpha)
        else:  # Run min_value if next player is MIN
            u_a = hmin_alpha_beta(result_state, result_player, pits,
                                  initial_max, alpha,
                                  beta, d)  # Get the utility of the resulting state assuming player is minimum
            if u < u_a:
                u = u_a
                max_action = a
            alpha = max(u_a, alpha)
    count_final = count
    count = 0
    return max_action,count_final

# Return utility of the state given that player is MAX
def hmax_alpha_beta(state, player, pits, initial_max, alpha, beta, d):
    global count
    count = count + 1
    if d == 0:  # Reached depth threshold, evaluate heuristic
        return evaluate(state, pits, initial_max)

    if terminal_test(state, pits):
        return utility(state, pits, initial_max)

    u = -math.inf  # min possible utility

    actions = available_actions(state, player, pits)

    for a in actions:  # Check each possible action for maximum utility
        player_copy = player
        state_copy = [row[:] for row in state]
        result_player, result_state = action(player_copy, a, state_copy, pits)
        if result_player == player:  # Run max_value if next player is MAX
            u = max([u, hmax_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta, d - 1)])
            if u >= beta:
                return u
            alpha = max(alpha, u)
        else:  # Run min_value if next player is MIN
            u = max([u, hmin_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta, d - 1)])
    return u

# Return utility of the state given that player is MIN
def hmin_alpha_beta(state, player, pits, initial_max, alpha, beta, d):
    global count
    count = count + 1
    if d == 0:  # Reached depth threshold, evaluate heuristic
        return evaluate(state, pits, initial_max)

    if terminal_test(state, pits):
        return utility(state, pits, initial_max)
    u = math.inf  # max possible utility
    actions = available_actions(state, player, pits)
    for a in actions:  # Check each possible action for minimmum utility
        player_copy = player
        state_copy = [row[:] for row in state]
        result_player, result_state = action(player_copy, a, state_copy, pits)
        if result_player == player:  # Run min_value if next player is MIN
            u = min([u, hmin_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta, d - 1)])
            if u <= alpha:
                return u
            beta = min(beta, u)
        else:  # Run max_value if next player is MAX
            u = min([u, hmax_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta, d - 1)])
    return u
