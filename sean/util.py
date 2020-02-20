def square(number):
    return number * number

def sortLibraries(libraries,days,bookScores):
    for idx,library in enumerate(libraries):
        library["books"] = sorted(library["books"], key=lambda x: bookScores[x], reverse=True)
        library["score"] = float(sum([bookScores[x] for idx,x in enumerate(library["books"]) if (idx < (days-library["signUpDays"])*library["numOfShipsPerDay"])])) / days
        library["id"] = idx

    return sorted(libraries, key=lambda x: x["score"], reverse=True)