# Made by John Skluzacek and Ashkan Omaraie 10/19/2022

# What should be chosen depending on policy
policy_map = {
    1: {
        'A': {1: 1, 2: 0},
        'B': {1: 1, 2: 0},
        'C': {1: 1, 2: 0}},
    2: {
        'A': {1: 0, 2: 1},
        'B': {1: 0, 2: 1},
        'C': {1: 0, 2: 1}},
    3: {
        'A': {1: .4, 2: .6},
        'B': {1: 1, 2: 0},
        'C': {1: 0, 2: 1}}
}
# actions available
action_set = {1, 2}
# state transition model
state_transition_model = {
    'A': {1: {'B': .9, 'C': .1}, 2: {'B': .1, 'C': .9}},
    'B': {1: {'D': .9, 'A': .1}, 2: {'D': .1, 'A': .9}},
    'C': {1: {'A': .9, 'D': .1}, 2: {'A': .1, 'D': .9}}
}
# The value of each node
state_value_table = {'A': 0, 'B': 0, 'C': 0, 'D': 100}
# Gamma
discounting_factor = .8
reward_model = -10


def policy_eval(iterations, policy):
    """Evaluates the policies in the policy map based on a Markov Decision Process."""
    # do it for 100 iteration
    for i in range(iterations):
        # Check each state
        for state in state_transition_model:
            if not state == 'D':
                state_val = 0
                # Check each action
                for action in action_set:
                    # Check each subsequent action
                    for sub_state in state_transition_model[state][action]:
                        # Multiplies the action taken to the probability of an action with the reward, gamma,
                        # and value of subsequent states
                        state_val += state_transition_model[state][action][sub_state] * policy_map[policy][state][
                            action] * (reward_model + discounting_factor * state_value_table[sub_state])
                        state_value_table[state] = round(state_val, 2)
    # formatting

    print('Vπ(A)= ', state_value_table['A'])
    print('Vπ(B)= ', state_value_table['B'])
    print('Vπ(C)= ', state_value_table['C'])
    print('Vπ(D)= ', state_value_table['D'])


if __name__ == '__main__':
    print('Policy 1')
    policy_eval(100, 1)
    print('\nPolicy 2')
    policy_eval(100, 2)
    print('\nPolicy 3')
    policy_eval(100, 3)
