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
        'A': {'1': .4, '2': .6},
        'B': {'1': 1, '2': 0},
        'C': {'1': 0, '2': 1}}
}
# Where you can go from each node
action_set = {1, 2}
reward_model = -10
# Transition model: the .9 or .1 or whatever
state_transition_model = {
                          1: {'A': {'B': .9, 'C': .1}, 'B': {'A': .1, 'D': .9}, 'C': {'A': .9, 'D': .1}},
                          2: {'B': {'A': .1, 'D': .1}, 'C': {'A': .1, 'D': .9}, 'A': {'B': .1, 'C': .9}},
                          }
# The value of each node
state_value_table = {'A': 0, 'B': 0, 'C': 0, 'D': 100}
# Gamma
discounting_factor = .8

def policy_eval(iterations,policies,start,terminal):
    for i in range(iterations):
        list = []
        value = 0
        for policy in policies:
            if policy != 3:
                for next_states in state_transition_model[policy][start]:
                    #print(next_states)
                    value = state_transition_model[policy][start][next_states]
                    #print("value from stm = ",value)
                    for action in action_set:
                        value = value * policy_map[policy][next_states][action]
                        #might need to set things before recursing or runing another iteration
                        #print(" value * action = ",value)
                        #print("next_state = ",next_states)
                        bracket_eq = (reward_model + discounting_factor * state_value_table[next_states])
                        prob = value * bracket_eq
                        list.append(prob)
                        #print("bracket_eq = ", bracket_eq)
            else:
                for next_states in state_transition_model[policy][start]:
                    #print(next_states)
                    value = state_transition_model[policy][start][next_states]
                    #print("value from stm = ",value)
                    for action in action_set:
                        value = value * policy_map[policy][next_states][action]
                        #might need to set things before recursing or runing another iteration
                        #print(" value * action = ",value)
                        #print("next_state = ",next_states)
                        bracket_eq = (reward_model + discounting_factor * state_value_table[next_states])
                        prob = value * bracket_eq
                        list.append(prob)
                        #print("bracket_eq = ", bracket_eq)

            num = 0
            for j in list:
                num += j
            state_value_table[start] = num
            print('num = ', num)
            # [-10 + gamma * V(C)]


if __name__ == '__main__':
    policy_eval(1,1,'A','D')