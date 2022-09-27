# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:01:17 2020

@author: xfang13
"""
#import operator
from heapq import heappush as push
from heapq import heappop as pop

#Make the graph
Romania_Map = {'Oradea':{'Zerind':71,'Sibiu':151},
               'Zerind':{'Arad':75,'Oradea':71},
               'Arad':{'Zerind':75,'Sibiu':140,'Timisoara':118},
               'Timisoara':{'Arad':118,'Lugoj':111},
               'Lugoj':{'Timisoara':111,'Mehadia':70},
               'Mehadia':{'Lugoj':70,'Drobeta':75},
               'Drobeta':{'Mehadia':75,'Craiova':120},
               'Craiova':{'Drobeta':120,'Rimnicu Vilcea':146,'Pitesti':138},
               'Rimnicu Vilcea':{'Craiova':146,'Sibiu':80,'Pitesti':97},
               'Sibiu':{'Oradea':151,'Arad':140,'Fagaras':99,'Rimnicu Vilcea':80},
               'Fagaras':{'Sibiu':99,'Bucharest':211},
               'Pitesti':{'Rimnicu Vilcea':97,'Craiova':138,'Bucharest':101},
               'Bucharest':{'Fagaras':211,'Pitesti':101,'Giurgiu':90,'Urziceni':85},
               'Giurgiu':{'Bucharest':90},
               'Urziceni':{'Bucharest':85,'Vaslui':142,'Hirsova':98},
               'Neamt':{'Iasi':87},
               'Iasi':{'Neamt':87,'Vaslui':92},
               'Vaslui':{'Iasi':92,'Urziceni':142},
               'Hirsova':{'Urziceni':98,'Eforie':86},
               'Eforie':{'Hirsova':86}           
              }

#Using Bucharest as the target, Arad as the source
Heuristics = {'Oradea':380,
               'Zerind':374,
               'Arad':366,
               'Timisoara':329,
               'Lugoj':244,
               'Mehadia':241,
               'Drobeta':242,
               'Craiova':160,
               'Rimnicu Vilcea':193,
               'Sibiu':253,
               'Fagaras':176,
               'Pitesti':100,
               'Bucharest':0,
               'Giurgiu':77,
               'Urziceni':80,
               'Neamt':234,
               'Iasi':226,
               'Vaslui':199,
               'Hirsova':151,
               'Eforie':161           
              }

#Another testing example
#Travel from S to G
G = {'A':{'B':2,'C':5,'G':12},
     'B':{'C':2,},
     'C':{'G':3},
     'G':{},
     'S':{'B':4,'A':1}
     }

H = {'S':7,'A':6,'B':2,'C':1,'G':0}

def main():
    # oh god oh fuck
    # first we need to mark out start and see what availab

if __name__=="__main__":
    source = 'Arad'
    target = 'Bucharest'