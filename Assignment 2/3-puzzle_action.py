# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:13:01 2017

@author: xfang13
"""

import numpy as np
import copy


def action(state):
    x, y = np.where(state == 0)
    x = x[0]
    y = y[0]
    result = []
    if x + 1 <= 1:
        state_copy = copy.deepcopy(state)
        temp = state_copy[x][y]
        state_copy[x][y] = state_copy[x + 1][y]
        state_copy[x + 1][y] = temp
        result.append(state_copy)
    if x - 1 >= 0:
        state_copy = copy.deepcopy(state)
        temp = state_copy[x][y]
        state_copy[x][y] = state_copy[x - 1][y]
        state_copy[x - 1][y] = temp
        result.append(state_copy)
    if y + 1 <= 1:
        state_copy = copy.deepcopy(state)
        temp = state_copy[x][y]
        state_copy[x][y] = state_copy[x][y + 1]
        state_copy[x][y + 1] = temp
        result.append(state_copy)
    if y - 1 >= 0:
        state_copy = copy.deepcopy(state)
        temp = state_copy[x][y]
        state_copy[x][y] = state_copy[x][y - 1]
        state_copy[x][y - 1] = temp
        result.append(state_copy)

    return result


def solvable(goal):
    search_history = [goal]
    explored = [goal]
    possible_moves = action(goal)
    flag1 = True
    search_history.append(possible_moves)
    explored += possible_moves
    while flag1:
        new_states = []
        for i in search_history[-1]:
            for j in action(i):
                flag2 = False
                for k in explored:
                    if np.array(j, k):
                        flag2 = True
                        break
                if flag2 is False:
                    explored.append(j)
                    new_states.append(j)
        if not new_states:
            print('Search complete')
            flag1 = False
    return explored


if __name__ == '__main__':
    results = action(np.asarray([[0, 1], [2, 3]]))
    print(results)
    print('Solvable: ' + solvable(results))
