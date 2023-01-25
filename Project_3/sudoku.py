import math

def printTable(table):
    for i in range(len(table)):
        line = ""
        if i == 3 or i == 6:
            print("----------------------")
        for j in range(len(table[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(table[i,j])+" "
        print(line)

def findZeroes(table):
    for i in range (0,9):
        for j in range (0,9):
            if table[i,j] != 0:
                table[i,j] = 1
    
    return table

def createBlocks ():
    finalListOfBlocks = []
    for r in range (0,9):
        tmpList = []
        block1 = [i + 3*((r)%3) for i in range(0,3)]
        block2 = [i + 3*math.trunc((r)/3) for i in range(0,3)]
        for x in block1:
            for y in block2:
                tmpList.append([x,y])
        finalListOfBlocks.append(tmpList)
    return(finalListOfBlocks) 

    
def checkEmptyCellInBlock (sudoku, oneBlock):
    finalSum = 0
    for box in oneBlock:
        finalSum += sudoku[box[0], box[1]]
    return(finalSum)