from eval_functions import available_actions, terminal_test, utility, calculate_score, action
import math

count = 0

# Return utility of state given that player is MAX
def max_value(state, player, pits, initial_max):
    global count
    count = count + 1
    if terminal_test(state, pits):
        return utility(state, pits, initial_max)
    u = -math.inf  # Set minimum possible utility
    actions = available_actions(state, player, pits)
    for a in actions:  # Check each possible action for maximum utility
        player_copy = player
        state_copy = [row[:] for row in state]
        result_player, result_state = action(player_copy, a, state_copy, pits)
        if result_player == player:  # Run max_value if next player is MAX
            u = max([u, max_value(result_state, result_player, pits, initial_max)])
        else:  # Run min_value if next player is MIN
            u = max([u, min_value(result_state, result_player, pits, initial_max)])
    return u


# Return utility of state given that player is MIN,a
def min_value(state, player, pits, initial_max):
    global count
    count = count + 1
    if terminal_test(state, pits):
        return utility(state, pits, initial_max)
    u = math.inf  # Set maximum possible utility
    actions = available_actions(state, player, pits)
    for a in actions:  # Check each possible action for minimmum utility
        player_copy = player
        state_copy = [row[:] for row in state]
        result_player, result_state = action(player_copy, a, state_copy, pits)
        if result_player == player:  # Run min_value if next player is MIN
            u = min([u, min_value(result_state, result_player, pits, initial_max)])
        else:  # Run max_value if next player is MAX
            u = min([u, max_value(result_state, result_player, pits, initial_max)])
    return u


# Return action that maximizes player's chance of winning
def minimax(state, player, pits):
    global count
    actions = available_actions(state, player, pits)
    max_action = 0
    initial_max = player  # Define initial MAX player for purpose of defining utility
    u = -(math.inf)
    for a in actions:
        player_copy = player
        state_copy = [row[:] for row in state]
        result_player, result_state = action(player_copy, a, state_copy, pits)  # Check resulting state of each action
        if result_player == player:  # Run max_value if next player is MAX
            u_a = max_value(result_state, result_player, pits, initial_max)
            if u < u_a:
                u = u_a
                max_action = a
        else:  # Run min_value if next player is MIN
            u_a = min_value(result_state, result_player, pits,
                            initial_max)  # Get the utility of the resulting state assuming player is minimum
            if u < u_a:
                u = u_a
                max_action = a
    count_final = count
    count = 0

    return max_action,count_final
