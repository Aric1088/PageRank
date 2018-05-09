import numpy as np
#Please run in IDLE
numPages = 0
def run():
    print("Page Rank Simulation:\n @Author = Aric Zhuang")
    numPages = input("Please enter the number of pages: ")
    initialRank = 1.0/int(numPages)
    stringGen = ''
    stringGen += str(initialRank)
    for x in range(0, int(numPages)-1):
        stringGen += ';' + str(initialRank) 
    initRankVector = np.matrix(stringGen)
    multiply(initRankVector, getWeights(numPages), 0.001)

def getWeights(numPages):
    crow = ''
    for x in range(1, int(numPages) +1):
        numLink = input("How many pages does page " + str(x) + " link to? Must be <= " +str(numPages) +":")
        if x != 1:
            crow += ';'
        print("Please enter 'y' and press enter if there exists\n a link to that page or enter 'n' otherwise\n")
        for y in range(1, int(numPages) +1):
            linkback = input("Does page " + str(x) + " link to page " + str(y) + "?")
            if linkback == "y":
                crow += ' ' + str(1.0/int(numLink))
            else:
                crow += ' 0'
    tpose= np.matrix(crow)
    return tpose.transpose()

def multiply(rank, transition, epsilon):
    old = rank
    new = np.matmul(transition, old)
    print( "Iteration 1")
    print(new)
    print("\n")
    
    counter = 1
    while(np.linalg.norm(new - old) > epsilon):
        old = new
        new = np.matmul(transition, old)
        counter += 1
        print( "Iteration " + str(counter) + "\n") 
        print(new)
        print("\n") 
while(True):
    run()
