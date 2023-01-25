import numpy as np
import random
import math
import statistics 

def fillBlocks(sudoku, listOfBlocks):
    for block in listOfBlocks:
        for box in block:
            if sudoku[box[0],box[1]] == 0:
                currentBlock = sudoku[block[0][0]:(block[-1][0]+1),block[0][1]:(block[-1][1]+1)]
                sudoku[box[0],box[1]] = random.choice([i for i in range(1,10) if i not in currentBlock])
    return sudoku

def checkEmptyCellInBlock (sudoku, oneBlock):
    finalSum = 0
    for box in oneBlock:
        finalSum += sudoku[box[0], box[1]]
    if finalSum > 8:
        return True
    else:
        return False

def findTwoZeroCellInBlock(fixedSudoku, block):
    while (True):
        firstBox = random.choice(block)
        secondBox = random.choice([box for box in block if box is not firstBox ])

        if fixedSudoku[firstBox[0], firstBox[1]] != 1 and fixedSudoku[secondBox[0], secondBox[1]] != 1:
            return([firstBox, secondBox])

def flipCells(sudoku, boxesToFlip):
    proposedSudoku = np.copy(sudoku)
    placeHolder = proposedSudoku[boxesToFlip[0][0], boxesToFlip[0][1]]
    proposedSudoku[boxesToFlip[0][0], boxesToFlip[0][1]] = proposedSudoku[boxesToFlip[1][0], boxesToFlip[1][1]]
    proposedSudoku[boxesToFlip[1][0], boxesToFlip[1][1]] = placeHolder
    return (proposedSudoku)

def ChooseNewState (currentSudoku, fixedSudoku, listOfBlocks, sigma):
    randomBlock = random.choice(listOfBlocks)
    while(checkEmptyCellInBlock(fixedSudoku, randomBlock)) :
        randomBlock = random.choice(listOfBlocks)  
    boxesToFlip = findTwoZeroCellInBlock(fixedSudoku, randomBlock)
    proposedSudoku = flipCells(currentSudoku,  boxesToFlip)
    
    currentCost = errorsOfEachRowCol(boxesToFlip[0][0], boxesToFlip[0][1], currentSudoku) + errorsOfEachRowCol(boxesToFlip[1][0], boxesToFlip[1][1], currentSudoku)
    newCost = errorsOfEachRowCol(boxesToFlip[0][0], boxesToFlip[0][1], proposedSudoku) + errorsOfEachRowCol(boxesToFlip[1][0], boxesToFlip[1][1], proposedSudoku)
    
    costDifference = newCost - currentCost
    rho = math.exp(-costDifference/sigma)
    if(np.random.uniform(1,0,1) < rho):
        return([proposedSudoku, costDifference])
    return([currentSudoku, 0])

def numOfItterations(fixed_sudoku):
    numberOfItterations = 0
    for i in range (0,9):
        for j in range (0,9):
            if fixed_sudoku[i,j] != 0:
                numberOfItterations += 1
    return numberOfItterations

def initialSigma (sudoku, fixedSudoku, listOfBlocks):
    listOfDifferences = []
    tmpSudoku = sudoku
    for i in range(1,10):
        randomBlock = random.choice(listOfBlocks)
        while(checkEmptyCellInBlock(fixedSudoku, randomBlock)) :
            randomBlock = random.choice(listOfBlocks)  
        boxesToFlip = findTwoZeroCellInBlock(fixedSudoku, randomBlock)
        tmpSudoku = flipCells(tmpSudoku, boxesToFlip)
        listOfDifferences.append(errorsTotal(tmpSudoku))
    return (statistics.pstdev(listOfDifferences))

def errorsTotal(sudoku):
    numberOfErrors = 0 
    for i in range (0,9):
        numberOfErrors += errorsOfEachRowCol(i ,i ,sudoku)
    return(numberOfErrors)

def errorsOfEachRowCol(row, column, sudoku):
    colErrors = 9 - len(np.unique(sudoku[:,column]))
    rowErrors = 9 - len(np.unique(sudoku[row,:])) 
    return colErrors + rowErrors