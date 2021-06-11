import itertools
import mpmath
import math
import Dataset
import random
import copy
import Visualizer
#   #
# Dirichet Priors
def alphaijk(i, j, k):
    if len(i.fathers) == 0:
        return 0
    return 1

def alphaij(i, j):
    if len(i.fathers) == 0:
        return 0
    a = 0
    for k in range(i.domine):
        a = a + 1
    return a


#   #
# log Cooper and Herskovits scoring
def Score(graph, data):
    score = 0
    for node in graph.nodes:
        if len(node.fathers) != 0:
            j = make_j(node)
            for comb in j[0]:
                score = score + mpmath.log(mpmath.gamma(alphaij(node, comb))) - mpmath.log( mpmath.gamma(alphaij(node, comb) + Dataset.Nij(data, node, [comb, j[1]])) )
                for k in range(node.domine):
                    score = score + mpmath.log(mpmath.gamma(alphaijk(node, comb, k) + Dataset.Nijk(data, node, [comb, j[1]], k)) - mpmath.log(mpmath.gamma(alphaijk(node, comb, k))))

    return score    


#   #
# Returns [ [cartesian_prod_of_fathers] , [ list_of_fathers] ]  <->  [ [[0,0,0] ,[0,0,1] ... ] , [2,5,3] ]
def make_j(node):
    jj = []
    labels = []
    for father in node.fathers:
        labels.append(father.label)
        ff = list(range(father.domine))
        jj.append(ff)
    j = itertools.product(*jj)
    jj.clear()
    for e in j:
        jj.append(e)
    return [jj, labels]
 

#   #
# Search for local maximum and does some random choices
def Learn(graph, dataset):
    graph.initDAG()
    current = Score( graph , dataset)
    score = 0
    run = True
    time = 0
    while(run):
        time+=1
        print(time)
        print(current)
        Visualizer.printdot(graph)
        Visualizer.printpng()
        run = False
        vstruct = graph.VStruct()
        G = []
        S = []

        #   #
        # Relevant Actions added to list graph->G , score->S
        for i in range(len(graph.nodes)):
            for j in range(i, len(graph.nodes)) :
                if i != j:
                    g1 = copy.deepcopy(graph)
                    g2 = copy.deepcopy(graph)
                    g3 = copy.deepcopy(graph)

                    g1.addEdge(g1.nodes[i], g1.nodes[j])
                    g2.removeEdge(g2.nodes[i], g2.nodes[j])
                    g3.invertEdge(g3.nodes[i], g3.nodes[j])

                    #   #
                    # only changing-VStructure acyclic steps are relevant
                    if g1.VStruct() != vstruct and not g1.isCyclic():
                        S.append(Score(g1, dataset))
                        G.append(g1)
                    if g2.VStruct() != vstruct and not g2.isCyclic():
                        S.append(Score(g2, dataset))
                        G.append(g2)
                    if g3.VStruct() != vstruct and not g3.isCyclic():
                        S.append(Score(g3, dataset))
                        G.append(g3)

        #   #
        # Is there a better graph in G ? 
        if len(S) > 0:
            score = Score(G[S.index(max(S))], dataset)
            if  score > current :
                graph = G[S.index(max(S))]
                current = score
                run = True
            
    #       #       #       #       #       #       #       à       #      END WHILE

    return [ graph , current ]

def QuickLearn(graph, dataset):
    graph.initDAG()
    run = True
    time = 0
    while(run):
        current = Score( graph , dataset)
        time+=1
        print(time)
        print(current)
        #Visualizer.printdot(graph)
        #Visualizer.printpng()
        run = False
        vstruct = graph.VStruct()

        catch = False
        i = 0
        while (not catch) and i <len(graph.nodes) :
            j = i + 1
            while (not catch) and j < len(graph.nodes) :
                g1 = copy.deepcopy(graph)
                g2 = copy.deepcopy(graph)
                g3 = copy.deepcopy(graph)

                g1.addEdge(g1.nodes[i], g1.nodes[j])
                g2.removeEdge(g2.nodes[i], g2.nodes[j])
                g3.invertEdge(g3.nodes[i], g3.nodes[j])

                #   #
                # the first graph to be a better one breaks the cycles
                    
                if g2.VStruct() != vstruct and not g2.isCyclic():
                    if Score(g1,dataset) > current : 
                        graph = g2
                        run = True
                        catch = True 
                elif g1.VStruct() != vstruct and not g1.isCyclic():
                    if Score(g1,dataset) > current : 
                        graph = g1
                        run = True
                        catch = True
                elif g3.VStruct() != vstruct and not g3.isCyclic():
                    if Score(g1,dataset) > current : 
                        graph = g3
                        run = True
                        catch = True 
                j = j + 1
            i = i + 1

            
    #       #       #       #       #       #       #       à       #      END WHILE

    return [ graph , current ]

