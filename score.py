import argparse

def ni(itr):
    return int(next(itr))

# parses the next string of itr as a list of integers
def nl(itr):
    return [int(v) for v in next(itr).split()]


def parse(inp):
    itr = (line for line in inp.split('\n'))
    ns = argparse.Namespace()
    inp = inp.split('\n')
    numOfBooks,numOfLibs,numOfDays =  [ int(i) for i in inp[0].split(' ') ]
    bookScores = [ int(i) for i in inp[1].split(' ')]    

    libDetails = []
    for idx in range(0,numOfLibs,2):
        detail = {}
        a,b,c =  [ int(i) for i in inp[idx+2].split(' ') ]
        detail['signUpDays'] = b
        detail['numOfShipsPerDay'] = c
        detail['books'] = [ int(i) for i in inp[idx+3].split(' ') ]
        libDetails.append(detail)
    return argparse.Namespace(numOfBooks = numOfBooks, numOfLibs=numOfLibs, numOfDays=numOfDays, bookScores = bookScores, libDetails= libDetails)


# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer
def score(inp, out):
    ns = parse(inp)
    itr = (line for line in out.split('\n'))
    # TODO: implement

    return 0


