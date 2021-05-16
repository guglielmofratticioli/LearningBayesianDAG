import os


def printdot(graph):
    body = " digraph G { \n\n"
    for node in graph.nodes:
        body = body + "    n" + \
            str(node.label) + " [ label = \"" + \
            str(node.name) + "::" + str(node.domine) + "\"]\n"
        for father in node.fathers:
            body = body + "    n" + \
                str(father.label) + " -> n" + str(node.label) + " \n"

    body = body + "\n}"

    dot = open("..\\Progetto\\render\\graph.dot", 'w')
    dot.write(body)
    dot.close()


def printpng():
    os.system(
        " dot ..\\Progetto\\render\\graph.dot -Tpng -o ..\\Progetto\\render\\graph.png")
