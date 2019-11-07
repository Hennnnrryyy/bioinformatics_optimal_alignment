import sys

def main():
    getSequences(sys.argv[1])
    print(sequence_1 + sequence_2)
    initializeMatrix()
    printPrettyMatrix()
    print(getOptimalScore())
    getOptimalAlignments()
    print(optimal_sequence_1 + "\n" +  optimal_sequence_2)
    print(multipleAlignments)
    return 0

def getSequences(inputFile):
    global sequence_1
    global sequence_2
    input = open(inputFile, "r")
    sequence_1 = input.readline()
    sequence_2 = input.readline()
    input.close()

def initializeMatrix():
    global grid, gap, match, mismatch
    gap = -2
    match = 2
    mismatch = -1
    grid = [ [0]*len(sequence_1) for i in range(len(sequence_2))]
    
    accumulator = gap #Used for initializing first row and column

    for i in range(1, len(sequence_2)): #Initializes 1st row
        grid[0][i] = accumulator
        accumulator += gap
    
    accumulator = gap
    for i in range(1, len(sequence_1)): #Initializes 1st column
        grid[i][0] = accumulator
        accumulator += gap

    fillInMatrix()

def getMax(row,col): #Finds max out of the left element, above element, and upper left diagonal element
    return max(grid[row][col-1]+gap, grid[row-1][col]+gap, grid[row-1][col-1]+getMatch(row,col))

def getMatch(row, col):
    return match if sequence_1[col-1:col] == sequence_2[row-1:row] else mismatch

def fillInMatrix():
    for row in range(1, len(sequence_2)) :
        for col in range(1, len(sequence_1)) :
            score = getMax(row,col)
            grid[row][col] = score

def getOptimalScore():
    return grid[len(sequence_2)-1][len(sequence_1)-1]

def getOptimalAlignments():
    global optimal_sequence_1, optimal_sequence_2, multipleAlignments
    row = len(sequence_2)-1
    col = len(sequence_1)-1
    optimal_sequence_1 = ""
    optimal_sequence_2 = ""
    multipleAlignments = "NO"

    while row >= 1 and col >= 1:
        m = getMax(row, col)
        if ( 
            ( (getMax(row,col) == grid[row][col-1]+gap) and (getMax(row,col) == grid[row-1][col]+gap) ) or
            ( (getMax(row,col) == grid[row][col-1]+gap) and (getMax(row,col) == grid[row-1][col-1]+gap) ) or
            ( (getMax(row,col) == grid[row-1][col]+gap) and (getMax(row,col) == grid[row-1][col]+gap) )
            ):
                multipleAlignments = "YES"
        if m == grid[row][col-1]+gap: # Left
            optimal_sequence_1 += sequence_1[col-1:col]
            optimal_sequence_2 += "-"
            col -= 1

        elif m == grid[row-1][col]+gap: #Above
            optimal_sequence_1 += "-"
            optimal_sequence_2 += sequence_2[row-1:row]
            row -= 1

        else:
            optimal_sequence_1 += sequence_1[col-1:col]
            optimal_sequence_2 += sequence_2[row-1:row]
            col -= 1
            row -= 1
    optimal_sequence_1 = optimal_sequence_1[::-1]
    optimal_sequence_2 = optimal_sequence_2[::-1]



def printPrettyMatrix():
    for x in range(0, len(sequence_2)):
        for y in range(0, len(sequence_1)):
            print ("%d\t" %(grid[x][y])),
        print ("")
    

main()

