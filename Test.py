from Graph import Graph, Node
from Dataset import Dataset, Example, Nijk
import Visualizer
import Learning
#   #
# A Foo Graph with a Foo dataset

n1 = Node(label=1, domine=2)
n2 = Node(label=2, domine=3)
n3 = Node(label=3, domine=2)
n4 = Node(label=4, domine=4)
n5 = Node(label=5, domine=3)

nodes = [n1, n2, n3, n4, n5]

n1.fathers = [n5]
n2.fathers = [n1, n4]
n3.fathers = [n1, n4]
n5.fathers = [n4]

graph = Graph(nodes)
Visualizer.printdot(graph)
Visualizer.printpng()

ex1 = Example(nodes, [0, 2, 1, 2, 2])
ex2 = Example(nodes, [0, 2, 1, 0, 1])
ex3 = Example(nodes, [1, 2, 1, 1, 2])
ex4 = Example(nodes, [0, 2, 1, 3, 2])
ex5 = Example(nodes, [1, 2, 0, 0, 2])  #Test2
ex6 = Example(nodes, [0, 0, 1, 1, 2])  #Test1
ex7 = Example(nodes, [0, 1, 0, 1, 2])
ex8 = Example(nodes, [0, 0, 1, 1, 3])  #Test1


examples = [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8]
datas = Dataset(nodes,examples)

# How many examples in which n2 fathers -> [ n1 , n4 ] = [0 , 1] while n2 = 0 
print(Nijk(datas , i=n2, j=[[0, 1], [1, 4]], k=0))  #  should be 2 


# How many examples in which n5 fathers -> [ n4 ] = [ 0 ] while n5 = 2
print(Nijk(datas , i=n5, j=[[0], [4]], k=2))       #should be 1 


# make_j should return a 2D list :  [ [cartesian_prod_of_fathers_domine ] , [ list_of_fathers ] ] 
print( Learning.make_j(n2)[0] , Learning.make_j(n2)[1] )

