import argparse
import random
from score import parse
from utkarsh.main import printSquare as utkarshPrintSquare
from waqas.main import printSquare as waqasPrintSquare
from divyansh.main import printSquare as divyanshPrintSquare
from sean.main import printSquare as seanPrintSquare
# inp is an input file as a single string
# return your output as a string


def solve(seed, inp, log):
    random.seed(seed)
    ns = parse(inp)

    # TODO: Solve the problem
    divyanshPrintSquare(1)
    waqasPrintSquare(2)
    utkarshPrintSquare(3)
    seanPrintSquare(4)

    return '0'
