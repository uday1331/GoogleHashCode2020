def square(number):
    return number * number

def calculateScores(libraries,days,bookScores):
    for library in libraries:
        library["score"] = float(sum([bookScores[x] for idx,x in enumerate(library["books"]) if (idx < (days-library["signUpDays"])*library["numOfShipsPerDay"])])) / days

    return sorted(libraries, key=lambda x: x["score"], reverse=True)