import random


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    #   #
    # San Andreas invert/remove a random Edge that changes VStructure
    def removeEdgeSA(self):
        i = 0
        while i < len(self.nodes) and len(self.nodes[i].fathers) < 2:
            i += 1
        if i < len(self.nodes) and len(self.nodes[i].fathers) >= 2:
            node = self.nodes[i]
            f = random.choice(node.fathers)
            if len(node.fathers) > 1 and len(f.sons) > 1:
                node.fathers.remove(f)
                f.sons.remove(node)

    def invertEdgeSA(self):
        i = 0
        while i < len(self.nodes) and len(self.nodes[i].fathers) < 2:
            i += 1
        if i < len(self.nodes) and len(self.nodes[i].fathers) >= 2:
            node = self.nodes[i]
            f = random.choice(node.fathers)
            node.sons.append(f)
            node.fathers.remove(f)
            f.fathers.append(node)
            f.sons.remove(node)

    #   #
    # Operation on Graph 
    def addEdge(self, node, father):
        if father not in node.fathers:
            node.fathers.append(father)
            father.sons.append(node)

    def removeEdge(self, node, father):
        if father in node.fathers and len(node.fathers) > 1 and len(father.sons) > 1:
            node.fathers.remove(father)
            father.sons.remove(node)

    def invertEdge(self, node, father):
        if father in node.fathers:
            node.sons.append(father)
            node.fathers.remove(father)
            father.fathers.append(node)
            father.sons.remove(node)

    
    #   #
    # Graph Properties
    def initDAG(self):
        q = []
        for n in self.nodes:
            q.append(n)
        for n in self.nodes:
            random.shuffle(q)
            q.remove(n)
            max = len(q)
            if max > 3 : max = 3
            k = random.randint(0, max)   # 3 sons max to have lighter graphs
            for i in range(k):
                n.fathers.append(q[i])
                q[i].sons.append(n)
        # FIX isolate nodes
        for node in self.nodes:
            if len(node.fathers) == len(node.sons) == 0:
                q = self.nodes.copy()
                q.remove(node)
                son = random.choice(q)
                node.sons.append(son)
                son.fathers.append(node)
        return

    def VStruct(self):
        v = []
        for n in self.nodes:
            if len(n.fathers) >= 2:
                v.append(1)
            else:
                v.append(0)
        return v

    def isCyclic(self):
        visit = []
        cycle = False
        fam = []
        for v in self.nodes:
            fam.clear()
            fam.append(v)
            if v not in visit:
                if self.DFS_R(v, visit, fam):
                    cycle = True
        return cycle

    def DFS_R(self, node, visit, fam):
        for s in node.sons:
            if s in fam:
                return True
            elif s not in visit:
                fam.append(s)
                return self.DFS_R(s, visit, fam)
        visit.append(node)


class Node:
    def __init__(self, label, domine, name = '' ):
        self.label = label
        self.domine = domine
        self.name = name
        self.fathers = []
        self.sons = []
        self.table = {}
