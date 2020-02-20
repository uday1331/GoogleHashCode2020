import argparse
import random
from score import parse
from uday.main import printSquare as udayPrintSquare
from ahsan.main import printSquare as ahsanPrintSquare
from welvin.main import printSquare as welvinPrintSquare
from sean.main import printSquare as seanPrintSquare
# inp is an input file as a single string
# return your output as a string

def parseInput(filename):
    f = open(filename, "r")
    numOfBooks,numOfLibs,numOfDays =  [ int(i) for i in f.readline().split(' ') ]
    bookScores = [ int(i) for i in f.readline().split(' ')]    

    libDetails = []
    for i in range(numOfLibs):
        detail = {}
        a,b,c =  [ int(i) for i in f.readline().split(' ') ]
        detail['signUpDays'] = b
        detail['numOfShipsPerDay'] = c
        detail['books'] = [ int(i) for i in f.readline().split(' ') ]
        libDetails.append(detail)
    print(numOfBooks, numOfLibs, numOfDays)
    print(bookScores)
    print(libDetails)

def solve(seed, inp, log):
    random.seed(seed)
    ns = parse(inp)

    # TODO: Solve the problem
    udayPrintSquare(seed, inp, log)
    ahsanPrintSquare(seed, inp, log)
    welvinPrintSquare(seed, inp, log)
    seanPrintSquare(seed, inp, log)
    

    return '0'
