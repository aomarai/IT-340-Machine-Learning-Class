# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:01:17 2020

@author: xfang13
@editors: John John Skluzacek and Ashkan Omaraie
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


def main():
    # oh, god oh heck oh fuck

    # gist of A*
    # first we need to mark out start and see what available
    # then we need to calculate the f value for each of the nodes
    # the f value is calculated by adding the cost with the heuristic value
    # we then chose the lowest value from the list (priority heap queue pop) and repeat the process
    # we are going to keep the items in the heap queue and update the f costs and path costs
    # we are going to be storing tuples in out heap queue

    # 1. Grab available nodes from the source node
    # 2. Calculate the f score and path cost for traveling to all visible nodes from current node (f score is the heuristic for current node ONLY + path cost so far)
    # 3. Push the tuples with (f score, path cost, path taken so far) onto the queue
    # 4. Pop the node with smallest f score
    # 5. If the target is not in the route of the popped node, expand nodes that the last node on the route can see
    # 6. Else if the target is in the tuple popped, found path and can finish
    # 7. Repeat 2 - 6 until target is found
    # 8. profit

    # Set current node to the starting node
    current_node = source
    # get the available node we can travel to
    A_Star(source, target)


def A_Star(source, target, weight_map, heuristic_map):
    heap_list = []
    flag = True
    while flag:
        print('Heaplist at start of loop: ', heap_list)
        for next_node in weight_map[source]:
            # in order want to push (f score, path cost, path from source to now)
            push(heap_list,tuple_to_push)
            print('Priority queue after pushing: ', heap_list)

        next_item = pop(heap_list)
        # discover all the nodes from the next item
        print("next item 2,-1: ",next_item[2][-1])
        for next_node in weight_map[next_item[2][-1]]:
            print('next node: ', next_node)
            for node in next_node:
                # Update the f score, path score, and path taken
                item_list = list(next_item)
                print(weight_map[next_item[2][-1]][node])
                # Convert tuple into a list, so it can be modified and then update path cost
                item_list[1] += weight_map[next_item[2][-1]][node]
                print('listified tuple: ', item_list)
                # Update the f score by adding the heuristic for current node ONLY to the path cost so far
                item_list[0] = heuristic_map[next_node] + item_list[1]
                item_list[2].append(next_node)
                # Re-convert the list back into a tuple
                next_item = tuple(item_list)
                print('re-tupled: ', next_item)
                # Push the new tuple onto the priority queue
                push(heap_list, next_item)
                #print("next item at 1: ",next_item[1])
        # Pop the next node from the priority queue if not empty
        source = pop(heap_list)
        #source = heap_list[0]
        print('Popped ', source)
        if source[2][-1] == target:
            flag = False
            print('Source: ', source)
        source = source[2][-1]

        #print('Next item: ', next_item)
        print('Priority queue: ', heap_list,'\n')
        # flag = False
    print('Loop ended')




if __name__ == "__main__":
    source = 'S'
    target = 'G'
    A_Star(source, target, G, H)
    # source = 'Arad'
    # target = 'Bucharest'
    # A_Star(source, target, Romania_Map, Heuristics)