#Setting up the sequence list and degree list
sizeOfSeq = int(raw_input("What Is The Size Of The Sequence? "))
sequence = [[] for _ in range(sizeOfSeq+1)]
degrees = [1]*(sizeOfSeq+2)
degreesLeft = len(degrees)
indexer = len(sequence)-sizeOfSeq-1

#The user inputs the label (or number) of each vertex in the sequence
while sizeOfSeq>0:
        input=int(raw_input("Enter The Label (Number) Of A Vertex: "))
        sequence[indexer].append(input)
        degreesLeft = degreesLeft + 1
        degrees[input-1] = degrees[input-1] + 1
        sizeOfSeq=sizeOfSeq-1
        indexer=len(sequence)-sizeOfSeq-1

#Algorithm starts here
sequenceIndex = 0
iteration = 0  #Used to iterate through the degrees list in inner while loop to find a degree of 1
foundOne = False  #Required to stop the while loop after finding a 1 in the degrees list

while degreesLeft >=0:
        while foundOne != True and iteration < len(degrees):
                if degrees[iteration] == 1 and degreesLeft > 2:
                        degrees[iteration] = degrees[iteration] - 1
                        degrees[(sequence[sequenceIndex][0])-1] = degrees[(sequence[sequenceIndex][0])-1] - 1
                        sequence[sequenceIndex].append(iteration+1)
                        sequence[sequenceIndex].reverse()
                        foundOne = True
                elif degrees[iteration] == 1 and degreesLeft <= 2:
                        degrees[iteration] = degrees[iteration] - 1
                        sequence[sequenceIndex].append(iteration+1)
                        foundOne = True
                iteration = iteration + 1
        if degreesLeft >2:
                sequenceIndex = sequenceIndex + 1
        degreesLeft = degreesLeft - 2
        iteration = 0
        foundOne = False

#Prints The State Of The Sequence At The End Of The Algorithm
print 'Set Of Edges In Tree T: {0}'.format(sequence)
