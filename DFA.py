__author__ = 'jonerik13'


import string as s

mapping = {}
def runDFA():

    #total number of states in the DFA
    states = raw_input("How many states are in this DFA?: ")


    #designate accepting states
    aStates = str(raw_input("Which of these states are accepting states? Enter in 01234 format:  "))

    #used set() to make sure user did not duplicate
    acceptStates = list(set(aStates))

    #take the alphabet into a list, use to make a mock transition graph
    sigma = str(raw_input("List the digits in the alphabet for your DFA. Enter in abc123&^$ format: "))
    alphabet = list(set(sigma))

    newDict = {}
    numDict = {}
    for i in alphabet:

            mapA = {}

            count = 0
            letter = int(states)
            for x in range(0, int(states)):
                temp = raw_input("At stage " + str(count) + " if you see a (" + str(i) + ") what stage will the DFA transition to?: ")

                count+=1

                mapA[x] = int(temp)

                mapping[str(i)] =mapA

    path = []
    stringTest = raw_input("Enter a string to test: " )
    stringT = list(stringTest)
    current = 0

    for e in stringT:

        letter = (mapping[str(e)])[current]

        path.append(int(letter))

        current = int(letter)

    finalStage = str(path[-1])
    print '*****'

    if finalStage in acceptStates:
        print "String Accepted!"

    else:
        print "String Rejected"

runDFA()