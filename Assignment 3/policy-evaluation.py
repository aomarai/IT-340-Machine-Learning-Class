# What should be chosen depending on policy
policy_map = {
    1: {
        'A': {'1': 1, '2': 0},
        'B': {'1': 1, '2': 0},
        'C': {'1': 1, '2': 0}},
    2: {
        'A': {'1': 0, '2': 1},
        'B': {'1': 0, '2': 1},
        'C': {'0': 1, '2': 1}},
    3: {
        'A': {'1': .4, '2': .6},
        'B': {'1': 1, '2': 0},
        'C': {'1': 0, '2': 1}}
}
# Where you can go from each node
action_set = {'A':['B', 'C'],
              'B':['A', 'D'],
              'C':['A', 'D'] }
reward_model = -10
# Transition model: the .9 or .1 or whatever
state_transition_model = 0
# The value of each node
state_value_table = {'A': 0, 'B': 0, 'C': 0, 'D': 100}

discounting_factor = .8

def policy_eval():
    for i in range(100):
        state_value_table['A'] = (1 * .9 * (reward_model + discounting_factor * state_value_table['B'])) + (1 * .1 * (reward_model + discounting_factor * state_value_table['B'])) + (0 * .9 * (reward_model + discounting_factor * state_value_table['C'])) + (0 * .1 * (reward_model + discounting_factor * state_value_table['B']))
        state_value_table['B'] = (1 * .9 * (reward_model + discounting_factor * state_value_table['C'])) + (
                    1 * .1 * (reward_model + discounting_factor * state_value_table['A'])) + (
                                             0 * .9 * (reward_model + discounting_factor * state_value_table['A'])) + (
                                             0 * .1 * (reward_model + discounting_factor * state_value_table['C']))
        state_value_table['C'] = (1 * .9 * (reward_model + discounting_factor * state_value_table['B'])) + (
                    1 * .1 * (reward_model + discounting_factor * state_value_table['A'])) + (
                                             0 * .9 * (reward_model + discounting_factor * state_value_table['A'])) + (
                                             0 * .1 * (reward_model + discounting_factor * state_value_table['B']))



if __name__ == '__main__':
    policy_eval()
    print(state_value_table['A'])
    print(state_value_table['B'])
    print(state_value_table['C'])