from .util import square


def printSquare(seed, inp, log):   
    sortedLibs = sorted(inp.libDetails, key=lambda lib: sum(lib['books']))
    print(sortedLibs)
    
