import copy
from .util import sortLibraries

def solve(seed, ns, log):

    D, B, L = ns.numOfDays, ns.numOfBooks, ns.numOfLibs
    details = ns.libDetails
    bookScores = ns.bookScores
    daysPassed = 0
    signUp = 0
    libraryId = []
    bookIds = []

    sortedLibraries = sortLibraries(copy.deepcopy(details), D - daysPassed, bookScores)
    while daysPassed < D:

        for id, i in enumerate(libraryId):
            allBooks = details[id]['books']
            s = int(details[id]['numOfShipsPerDay'])
            currentNumber = len(bookIds[i])
            bookIds[i] += allBooks[currentNumber: currentNumber + s]

        if signUp == 0 and len(sortedLibraries) > 0:
            # print(sortedLibraries)
            id = sortedLibraries[0]['id']
            libraryId.append(id)
            print(id)
            bookIds.append([])
            signUp = int(details[id]['signUpDays'])
            sortedLibraries = sortLibraries(sortedLibraries[1:], D - daysPassed, bookScores)

        daysPassed += 1
        signUp -= 1

    # output
    out = []
    A = 0
    for i, id in enumerate(libraryId):
        array = bookIds[i]
        books = len(array)
        if books > 0:
            A += 1
            out.append(str(id) + " " + str(books))
            string = ""
            for i, e in enumerate(array):
                string += str(e)
                if i < len(array) - 1:
                    string += " "
            if len(string) > 0:
                out.append(string)
    out.insert(0, str(A))
    # print(out)

    return '\n'.join(out)

