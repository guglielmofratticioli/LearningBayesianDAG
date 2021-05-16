class Dataset:
    def __init__(self, varlist=[], data=[]):
        self.varlist = varlist
        self.data = data


class Example:
    def __init__(self, varlist=[], values=[]):
        self.varlist = varlist
        self.values = values

#   #
# Nijk counts occurrences in dataset given Node i = k  , j = [ [a_combination] , [fathers_labels] ]
def Nijk(dataset, i, j, k):
    if len(i.fathers) == 0:
        return 0
    n = 0
    for example in dataset.data:
        match = True
        f = 0
        for father in j[1]:
            if (example.values)[i.label - 1] != k or (example.values)[father - 1] != (j[0])[f]:
                match = False
            f = f + 1
        if match:
            n = n + 1
    return n

#   #
# Sum Nijk for every k 
def Nij(dataset, i, j):
    if len(i.fathers) == 0:
        return 0
    else:
        n = 0
        for k in range(i.domine):
            for example in dataset.data:
                match = True
                f = 0
                for father in j[1]:
                    if (example.values)[i.label - 1] != k or (example.values)[father - 1] != (j[0])[f]:
                        match = False
                    f = f + 1
                if match:
                    n = n + 1
        return n
