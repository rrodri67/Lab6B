#Raul Rodriguez
#80549657
#Last Modified - 11/26/2018
#Diego Aguirre - Professor
#Manoj Saha - Assistant

from Lab6utils import topological_sort
from Lab6utils import kruskals
from GraphAL import GraphAL


def main():
  print("Kruskal's algorithm, formatted as:")
  print("[source, dest, weight].")
  print()
  # Kruskal Graph 
  # 0--1
  # |\/|
  # |/\|
  # 2--3
  graph_kruskals = GraphAL(initial_num_vertices=4, is_directed=False)

  graph_kruskals.add_edge(0, 1, 6.0)
  graph_kruskals.add_edge(1, 3, 4.0)
  graph_kruskals.add_edge(0, 3, 3.0)
  graph_kruskals.add_edge(2, 3, 2.0)
  graph_kruskals.add_edge(0, 2, 1.0)
  graph_kruskals.add_edge(1, 2, 5.0)
  print("A minimum spanning tree for the graph:")
  for value in kruskals(graph_kruskals):
      print(value)
      
      
  print()
  # Topological Sort Graph 
  #   /--> 1 -> 4 -> 7 -\
  #  /                   \
  # 0 -> 2 -> 5 -> 8------> 10
  #  \                  /
  #  \--> 3 -> 6 -> 9--/
  print("The topological order of vertices in the graph: ")
  graph_topological = GraphAL(initial_num_vertices=11, is_directed=True)

  graph_topological.add_edge(0, 1)
  graph_topological.add_edge(0, 2)
  graph_topological.add_edge(0, 3)

  graph_topological.add_edge(1, 4)
  graph_topological.add_edge(2, 5)
  graph_topological.add_edge(3, 6)

  graph_topological.add_edge(4, 7)
  graph_topological.add_edge(5, 8)
  graph_topological.add_edge(6, 9)

  graph_topological.add_edge(7, 10)
  graph_topological.add_edge(8, 10)
  graph_topological.add_edge(9, 10)
  print(topological_sort(graph_topological))    
  
main()  
