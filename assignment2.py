import sys

def main():
    getSequences(sys.argv[1])
    print(sequence_2 + sequence_1)
    initializeMatrix()
    printPrettyMatrix()
    print(getOptimalScore())
    getOptimalAlignments()
    print(optimal_sequence_2 + "\n" +  optimal_sequence_1)
    print(multipleAlignments)
    writeFiles()
    return 0

def writeFiles():
    scoreFile = open("2.o1","w")
    matrixFile = open("2.o2", "w")
    optimalFile = open("2.o3", "w")
    isThereMoreFile = open("2.o4", "w")
   
    scoreFile.write(str(getOptimalScore()) + "\n")

    writePrettyMatrix(matrixFile)

    optimalFile.write(optimal_sequence_2 + "\n")
    optimalFile.write(optimal_sequence_1 + "\n")

    isThereMoreFile.write(multipleAlignments + "\n")

    scoreFile.close()
    matrixFile.close()
    optimalFile.close()
    isThereMoreFile.close()

def getSequences(inputFile): #Gets sequences from input file
    global sequence_1
    global sequence_2
    input = open(inputFile, "r")
    sequence_2 = input.readline()
    sequence_1 = input.readline()
    input.close()

def initializeMatrix(): # Initializes and fills in matrix
    global grid, gap, match, mismatch
    gap = -2
    match = 2
    mismatch = -1
    grid = [ [0]*len(sequence_1) for i in range(len(sequence_2))]
    
    accumulator = gap # Used for initializing first row and column

    for i in range(1, len(sequence_1)): # Initializes 1st row
        grid[0][i] = accumulator
        accumulator += gap
    
    accumulator = gap
    for i in range(1, len(sequence_2)): # Initializes 1st column
        grid[i][0] = accumulator
        accumulator += gap

    fillInMatrix() # Fill in other rows and columns

def getMax(row,col): # Finds max out of the left element, above element, and upper left diagonal element with match or gap
    return max(grid[row][col-1]+gap, grid[row-1][col]+gap, grid[row-1][col-1]+getMatch(row,col))

def getMatch(row, col): # Determines if two letters in sequence are a match
    return match if sequence_1[col-1:col] == sequence_2[row-1:row] else mismatch

def fillInMatrix(): # Fills in matrix by calculating score of each cell based on the max of its adjacent cells
    for row in range(1, len(sequence_2)) :
        for col in range(1, len(sequence_1)) :
            score = getMax(row,col)
            grid[row][col] = score

def getOptimalScore(): # Retrieves optimal score from the last cell
    return grid[len(sequence_2)-1][len(sequence_1)-1]

def getOptimalAlignments(): # Back tracing to find ONE optimal alignment
    global optimal_sequence_1, optimal_sequence_2, multipleAlignments
    row = len(sequence_2)-1
    col = len(sequence_1)-1
    optimal_sequence_1 = ""
    optimal_sequence_2 = ""
    multipleAlignments = "NO"

    while row >= 1 and col >= 1:
        m = getMax(row, col) # Max out of adjacent values

        if ( #multipleAlignments == "NO" and # Checks if two max values exist and can be used to find multiple optimal alignments
            ( (getMax(row,col) == grid[row][col-1]+gap) and (getMax(row,col) == grid[row-1][col]+gap) ) or
            ( (getMax(row,col) == grid[row][col-1]+gap) and (getMax(row,col) == grid[row-1][col-1]+gap) ) or
            ( (getMax(row,col) == grid[row-1][col]+gap) and (getMax(row,col) == grid[row-1][col]+gap) )
            ):
                multipleAlignments = "YES"

        if m == grid[row][col-1]+gap: # Left
            optimal_sequence_1 += sequence_1[col-1:col] # Keep letter
            optimal_sequence_2 += "-" # Gap
            col -= 1

        elif m == grid[row-1][col]+gap: # Above
            optimal_sequence_1 += "-" # Gap
            optimal_sequence_2 += sequence_2[row-1:row] # Keep letter
            row -= 1

        else: # Upper Left Diagonal
            optimal_sequence_1 += sequence_1[col-1:col] # Keep letter
            optimal_sequence_2 += sequence_2[row-1:row] # Keep letter
            col -= 1
            row -= 1
    optimal_sequence_1 = optimal_sequence_1[::-1] # Reverse optimal sequence 1
    optimal_sequence_2 = optimal_sequence_2[::-1] # Reverse optimal sequence 2



def printPrettyMatrix(): # Prints matrix in a pretty fashion
    for x in range(0, len(sequence_2)):
        for y in range(0, len(sequence_1)):
            print ("%d\t" %(grid[x][y])),
        print ("")

def writePrettyMatrix(f): # Writes matrix in a pretty fashion to file
    for x in range(0, len(sequence_2)):
        for y in range(0, len(sequence_1)):
            f.write("%d\t" %(grid[x][y])),
        f.write("\n")
    

main()

