from eval_functions import available_actions, terminal_test, utility, calculate_score, action

import math


count = 0

# Return action that maximizes player's chance of winning
def alpha_beta(state, player, pits):
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
            u_a = max_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta)
            if u < u_a:
                u = u_a
                max_action = a
            alpha = max(u_a, alpha)
        else:  # Run min_value if next player is MIN
            u_a = min_alpha_beta(result_state, result_player, pits,
                                 initial_max, alpha,
                                 beta)  # Get the utility of the resulting state assuming player is minimum
            if u < u_a:
                u = u_a
                max_action = a
            alpha = max(u_a, alpha)
    count_final = count
    count = 0
    return max_action,count_final

# Return utility of the state given that player is MAX
def max_alpha_beta(state, player, pits, initial_max, alpha, beta):
    global count
    count = count + 1
    if terminal_test(state, pits):
        return utility(state, pits, initial_max)
    u = -math.inf  # min possible utility
    actions = available_actions(state, player, pits)
    for a in actions:  # Check each possible action for maximum utility
        player_copy = player
        state_copy = [row[:] for row in state]
        result_player, result_state = action(player_copy, a, state_copy, pits)
        if result_player == player:  # Run max_value if next player is MAX
            u = max([u, max_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta)])
            if u >= beta:
                return u
            alpha = max(alpha, u)
        else:  # Run min_value if next player is MIN
            u = max([u, min_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta)])
    return u

# Return utility of the state given that player is MIN
def min_alpha_beta(state, player, pits, initial_max, alpha, beta):
    global count
    count = count + 1
    if terminal_test(state, pits):
        return utility(state, pits, initial_max)
    u = math.inf  # max possible utility
    actions = available_actions(state, player, pits)
    for a in actions:  # Check each possible action for minimum utility
        player_copy = player
        state_copy = [row[:] for row in state]
        result_player, result_state = action(player_copy, a, state_copy, pits)
        if result_player == player:  # Run min_value if next player is MIN
            u = min([u, min_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta)])
            if u <= alpha:
                return u
            beta = min(beta, u)
        else:  # Run max_value if next player is MAX
            u = min([u, max_alpha_beta(result_state, result_player, pits, initial_max, alpha, beta)])
    return u
