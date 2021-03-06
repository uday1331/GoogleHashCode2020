import argparse
import random
from score import parse
from uday.main import printSquare as udayPrintSquare
from ahsan.main import printSquare as ahsanPrintSquare
from welvin.main import printSquare as welvinPrintSquare
from sean.main import solve as seanSolve
# inp is an input file as a single string
# return your output as a string


def solve(seed, inp, log):
    random.seed(seed)
    ns = parse(inp)
    # print(ns)

    # TODO: Solve the problem
    # udayPrintSquare(seed, inp, log)
    # ahsanPrintSquare(seed, inp, log)
    # welvinPrintSquare(seed, inp, log)
    sean = seanSolve(seed, ns, log)
    

    return sean
