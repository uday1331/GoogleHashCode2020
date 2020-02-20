from .util import square

def solve(seed, ns, log):

    D, B, L = ns.numOfDays, ns.numOfBooks, ns.numOfLibs
    details = ns.libDetails
    daysPassed = 0
    signUp = 0
    currentL = -1
    libraryId = []
    bookIds = []

    while daysPassed < D:

        for id, i in enumerate(libraryId):
            allBooks = details[id]['books']
            s = int(details[id]['numOfShipsPerDay'])
            currentNumber = len(bookIds[i])
            bookIds[i] += allBooks[currentNumber: currentNumber + s]

        if signUp == 0 and currentL + 1 < len(details):
            currentL += 1
            libraryId.append(currentL)
            bookIds.append([])
            signUp = int(details[currentL]['signUpDays'])

        daysPassed += 1
        signUp -= 1

    # output
    out = []
    A = len(libraryId)
    out.append(str(A))
    for i, id in enumerate(libraryId):
        array = bookIds[i]
        books = len(array)
        out.append(str(id) + " " + str(books))
        string = ""
        for i, e in enumerate(array):
            string += str(e)
            if i < len(array) - 1:
                string += " "
        out.append(string)

    return '\n'.join(out)
