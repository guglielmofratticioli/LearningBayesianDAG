import itertools
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
                score = score + math.log(math.gamma(alphaij(node, comb))) - math.log( math.gamma(alphaij(node, comb) + Dataset.Nij(data, node, [comb, j[1]])) )
                for k in range(node.domine):
                    score = score + math.log(math.gamma(alphaijk(node, comb, k) + Dataset.Nijk(data, node, [comb, j[1]], k)) - math.log(math.gamma(alphaijk(node, comb, k))))

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
def Learn(graph, dataset, SAindex):
    current = Score( graph , dataset)
    score = 0
    run = True
    time = 0
    while(run):
        time+=1
        print(time)
        print(current)
        run = False
        vstruct = graph.VStruct()
        G = []
        S = []

        Visualizer.printdot(graph)
        Visualizer.printpng()

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

        #       #       #       #       #       #       #       #   END FOR

        #   #
        # San Andreas Step
        if random.randint(0, 100) < SAindex:
            run = True
            gSA = copy.deepcopy(graph)
            if bool(random.getrandbits(1)):
                gSA.invertEdgeSA()
            else:
                gSA.removeEdgeSA()

            if not gSA.isCyclic():
                graph = gSA

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


#   #
# Calls Learn several times on random generated DAGs to find best Learning 
def bestLearn(graph, dataset, SAindex, iter):
    G = []
    S = []
    for i in range(iter):
        g = copy.deepcopy(graph)
        g.initDAG()
        Visualizer.printdot(g)
        Visualizer.printpng()
        [gr, sc] = Learn(g, dataset, SAindex)
        G.append(gr)
        S.append(sc)
    return G[S.index(max(S))]
