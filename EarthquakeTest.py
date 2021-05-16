from Learning import Score, bestLearn
from Dataset import Dataset, Example
import Graph
import Visualizer
import random

#   #
# Returns an Examples based on graph's tables
def EQsampler(graph):
    Burglary = graph.nodes[0]
    Earthquake = graph.nodes[1]
    Alarm = graph.nodes[2]
    JohnCall = graph.nodes[3]
    MaryCall = graph.nodes[4]

    b = random.choices(population=[1, 0], weights=[Burglary.table.get(
        'True'), 1 - Burglary.table.get('True')], k=1)
    e = random.choices(population=[1, 0], weights=[Earthquake.table.get(
        'True'), 1 - Earthquake.table.get('True')], k=1)
    a = random.choices(population=[1, 0], weights=[Alarm.table.get(str(
        b[0]) + ',' + str(e[0])), 1 - Alarm.table.get(str(b[0]) + ',' + str(e[0]))], k=1)
    j = random.choices(population=[1, 0], weights=[JohnCall.table.get(
        str(a[0])), 1 - JohnCall.table.get(str(a[0]))], k=1)
    m = random.choices(population=[1, 0], weights=[MaryCall.table.get(
        str(a[0])), 1 - MaryCall.table.get(str(a[0]))], k=1)

    return [b[0], e[0], a[0], j[0], m[0]]

#   #
# Builds just the Nodes of Earthquake model
def BuildEQGraph(): 
    Burglary = Graph.Node(label=1, domine=2, name="Burglary")
    Earthquake = Graph.Node(label=2, domine=2, name="Earthquake")
    Alarm = Graph.Node(label=3, domine=2, name="Alarm")
    JohnCalls = Graph.Node(label=4, domine=2, name="JohnCalls")
    MaryCalls = Graph.Node(label=5, domine=2, name="MaryCalls")

    Burglary.table['True'] = 0.01
    Earthquake.table['True'] = 0.02
    Alarm.table['1,1'] = 0.95
    Alarm.table['0,1'] = 0.29
    Alarm.table['1,0'] = 0.94
    Alarm.table['0,0'] = 0.001
    JohnCalls.table['0'] = 0.9
    JohnCalls.table['1'] = 0.05
    MaryCalls.table['0'] = 0.7
    MaryCalls.table['1'] = 0.01

    nodes = [Burglary, Earthquake, Alarm, JohnCalls, MaryCalls]
    return Graph.Graph(nodes)

#   #
# Builds the Earthquake Model 
def actualEQGraph(): 
    B = Graph.Node(label=1, domine=2, name="Burglary")
    E = Graph.Node(label=2, domine=2, name="Earthquake")
    A = Graph.Node(label=3, domine=2, name="Alarm")
    J = Graph.Node(label=4, domine=2, name="JohnCalls")
    M = Graph.Node(label=5, domine=2, name="MaryCalls")
    A.fathers = [B, E]
    J.fathers = [A]
    M.fathers = [A]
    B.sons = [A]
    E.sons = [A]
    A.sons = [J, M]
    B.table['True'] = 0.01
    E.table['True'] = 0.02
    A.table['1,1'] = 0.95
    A.table['0,1'] = 0.29
    A.table['1,0'] = 0.94
    A.table['0,0'] = 0.001
    J.table['0'] = 0.9
    J.table['1'] = 0.05
    M.table['0'] = 0.7
    M.table['1'] = 0.01

    n = [B, E, A, J, M]
    return Graph.Graph(n)
    
EQGraph = BuildEQGraph()
actualEQGraph = actualEQGraph()

examples = []
actualexamples = []

#   #
# examples = rexamples  ( but references to different <Node> objects )
for i in range(100):
    smp = EQsampler(EQGraph)
    examples.append(Example(EQGraph.nodes, smp ))
    actualexamples.append(Example(actualEQGraph , smp ))

datas = Dataset(EQGraph.nodes, examples)
rdatas = Dataset(actualEQGraph.nodes , actualexamples)

print( " Score of the actual Earthquake model  ")
print(Score(actualEQGraph, rdatas))
Visualizer.printdot(actualEQGraph)
Visualizer.printpng()

input()
learnt = bestLearn(EQGraph, datas, SAindex=99, iter=50)

print( " Score of the learnt Earthquake model  ")
print(Score(learnt, rdatas))
Visualizer.printdot(learnt)
Visualizer.printpng()


