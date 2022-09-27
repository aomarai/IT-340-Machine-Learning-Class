# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:01:17 2020

@author: xfang13
"""
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
    # oh, god oh heck oh jeez

    # gist of A*
    # first we need to mark out start and see what available
    # then we need to calculate the f value for each of the nodes
    # the f value is calculated by adding the cost with the hueristc value
    # we then chose the lowest value from the list (priority queue) and repeat the process
    # if any of the nodes are the target we chose that and end

    # first lets create a list of the nodes that we could travel to
    print(G)
    # Set current node to the starting node
    current_node = source
    # get the available node we can travel to
    A_Star(source, target)


def A_Star(source, target):
    current_node = source
    route = [source]
    total_cost = 0
    flag = True
    while flag:
        if (current_node == target):
            print('Reached destination')
            break
        dict_next_node_and_f_score = {}
        list_f_scores = []
        # Get the g scores for the availble nodes to travel to from current node
        # get the costs to travel to each node
        for node_name in G[current_node]:
            dict_next_node_and_f_score.update({node_name:G[current_node][node_name]})
        print('list of scores with g score = : ', dict_next_node_and_f_score)


        # compute the f scores
        for i in dict_next_node_and_f_score.keys():
            dict_next_node_and_f_score[i] += H[i]
        #get the lowest node of the f score
        lowest_node = min(dict_next_node_and_f_score, key=dict_next_node_and_f_score.get)

        print(lowest_node)
        current_node=lowest_node
        route.append(current_node)
        # Add total cost here
        print('route: ', route)


if __name__ == "__main__":
    source = 'S'
    target = 'G'
    main()
