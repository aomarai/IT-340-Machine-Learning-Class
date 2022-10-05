# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:01:17 2020

@author: xfang13
@editors: John Skluzacek and Ashkan Omaraie
"""
import heapq
# import operator
from heapq import heappush as push
from heapq import heappop as pop

# Make the graph
Romania_Map = {'Oradea': {'Zerind': 71, 'Sibiu': 151},
               'Zerind': {'Arad': 75, 'Oradea': 71},
               'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
               'Timisoara': {'Arad': 118, 'Lugoj': 111},
               'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
               'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
               'Drobeta': {'Mehadia': 75, 'Craiova': 120},
               'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
               'Rimnicu Vilcea': {'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97},
               'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
               'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
               'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
               'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
               'Giurgiu': {'Bucharest': 90},
               'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
               'Neamt': {'Iasi': 87},
               'Iasi': {'Neamt': 87, 'Vaslui': 92},
               'Vaslui': {'Iasi': 92, 'Urziceni': 142},
               'Hirsova': {'Urziceni': 98, 'Eforie': 86},
               'Eforie': {'Hirsova': 86}
               }

# Using Bucharest as the target, Arad as the source
Heuristics = {'Oradea': 380,
              'Zerind': 374,
              'Arad': 366,
              'Timisoara': 329,
              'Lugoj': 244,
              'Mehadia': 241,
              'Drobeta': 242,
              'Craiova': 160,
              'Rimnicu Vilcea': 193,
              'Sibiu': 253,
              'Fagaras': 176,
              'Pitesti': 100,
              'Bucharest': 0,
              'Giurgiu': 77,
              'Urziceni': 80,
              'Neamt': 234,
              'Iasi': 226,
              'Vaslui': 199,
              'Hirsova': 151,
              'Eforie': 161
              }

# Another testing example
# Travel from S to G
G = {'A': {'B': 2, 'C': 5, 'G': 12},
     'B': {'C': 2, },
     'C': {'G': 3},
     'G': {},
     'S': {'B': 4, 'A': 1}
     }

H = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'G': 0}


# 1. Grab available nodes from the source node
# 2. Calculate the f score and path cost for traveling to next layer of visible nodes from current node (f score is the heuristic for current node ONLY + path cost so far)
# 3. Push the tuples with (f score, path cost, path taken so far) onto the queue
# 4. Pop the node with smallest f score
# 5. If the target is not in the route of the popped node, expand next layer of nodes that the last node on the route can see
# 6. Else if the target is in the tuple popped, found path and can finish
# 7. Repeat 2 - 6 until target is found
# 8. profit

#computes the total path cost for a list
def path_total(path, w_map):
    # [s]
    # [s,a,g]
    # [s,a,b,c,g]
    print(path)
    p_cost = 0
    if len(path) == 0 or len(path) == 1:
        return 0
    else:
        cur_node = path[0]
        i = 1
        next_node = path[i]
        while not next_node == path[-1]:
            p_cost += w_map[cur_node][next_node]
            cur_node = next_node
            i += 1
            next_node = path[i]
        p_cost += w_map[path[-2]][path[-1]]
    return p_cost


def A_Star(source, target, weight_map, heuristic_map):
    heap_list = []
    flag = True
    loop_limit = 5
    loop_counter = 0
    while flag:
        #print("source at top loop: ",source)
        route = []
        # source will become a tuple with an array
        prev_path_cost = 0
        if type(source) == tuple:
            route = source[2]
            # we will have to use this variable to see if a route is cheaper
            prev_path_cost = source[1]
            source = source[2][-1]
        print("route = ",route)
        explored_a_node = False
        for next_node in weight_map[source]:
            # explore the next layer of available nodes from the source
            if route:
                if not explored_a_node:
                    #if next_node == target:
                    #    #if route[-1] == target then the path cost and f score are the same
                    #    route.append(next_node)
                    #    explored_a_node = True
                    #    final_path_cost = path_total(route,weight_map)
                    #    tuple_to_push = (final_path_cost,final_path_cost,route)
                    #    push(heap_list,tuple_to_push)
                    #else:

                    route.append(next_node)
                    explored_a_node = True
                    path_cost_to_add = weight_map[source][next_node]
                    #print("if before ppc ",prev_path_cost)
                    prev_path_cost += path_cost_to_add
                    #print("if after pcta ", path_cost_to_add)

                    f_score = prev_path_cost + heuristic_map[next_node]
                    #print(route)
                    tuple_to_push = (f_score, path_total(route, weight_map), route)
                    print("line 164, tuple to push= ", tuple_to_push)
                    push(heap_list, tuple_to_push)
                    print('Heap after exploring first node: ', heap_list)
                    #print('Route after iter', route)
                else:

                    #if next_node == target:
                    #    new_route = route[:-1]
                    #    new_route.append(next_node)
                    #    final_path_cost = path_total(route, weight_map)
                    #    tuple_to_push = (final_path_cost, final_path_cost, route)
                    #    push(heap_list, tuple_to_push)
                    #else:
                    new_route = route[:-1]
                    new_route.append(next_node)
                    #print("else before ppc ", prev_path_cost)
                    # prev_path_cost += weight_map[source][next_node]
                    #print("else after ppc ",prev_path_cost)

                    f_score = path_total(new_route, weight_map) + heuristic_map[next_node]
                    #print('NewRoute: ', new_route)
                    tuple_to_push = (f_score, path_total(new_route, weight_map), new_route)

                    print("line 164, tuple to push= ",tuple_to_push)
                    push(heap_list, tuple_to_push)
                    print('Heap after additonal explore: ', heap_list)
                    #print('New Route after iter', new_route)
                    #print('Prev path cost bigger than 1 route: ', prev_path_cost)
            else: # discover the 1st set of nodes
                f_score = weight_map[source][next_node] + heuristic_map[next_node]
                path_cost = weight_map[source][next_node]
                init_path = [source, next_node]
                tuple_to_push = (f_score, path_cost, init_path)
                push(heap_list, tuple_to_push)
            #print('Heap after exploration: ', heap_list)
        print("heap list: ", heap_list)
        # Pop the smallest path cost on queue
        popped_node = pop(heap_list)
        # exit condition
        if popped_node[2][-1] == target:
            flag = False
            print('Final route: ', popped_node)
            break
        print('Popped ', popped_node)
        # explore the nodes available from the popped item
        new_p_cost = 0
        # print('Heap after 1st for: ', heap_list)
        for next_node in weight_map[popped_node[2][-1]]:
            for node in next_node:
                #print("node = ",node)
                #print("next_node = ",next_node)
                item_list = list(popped_node)
                # lets calculate the cost of traveling to the next items
                # print("item list = ",item_list)
                item_list[2].append(next_node) #changing next_node to node
                item_list[1] = path_total(item_list[2], weight_map)  # path cost
                item_list[0] = heuristic_map[next_node] + item_list[1] # f_score, #changing next_node to node
                print("2x for item list: ",item_list, '\n')
                push(heap_list, tuple(item_list))
                #print("heap list = ",heap_list)
        source = pop(heap_list)
        #print('Source after pop: ', source, '\n')


if __name__ == "__main__":
    source = 'S'
    target = 'G'
    A_Star(source, target, G, H)
    source = 'Arad'
    target = 'Bucharest'
    A_Star(source, target, Romania_Map, Heuristics)