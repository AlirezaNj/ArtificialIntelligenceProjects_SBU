import json
import sudoku
import sa
import numpy as np
from time import time

# *** you can change everything except the name of the class, the act function and the problem_data ***


class AI:
    # ^^^ DO NOT change the name of the class ***

    def __init__(self):
        pass

    # the solve function takes a json string as input
    # and outputs the solved version as json
    def solve(self, problem):
        # ^^^ DO NOT change the solve function above ***

        problem_data = json.loads(problem)
        # ^^^ DO NOT change the problem_data above ***

        # TODO implement your code here
        sudoku_list =  problem_data['sudoku']
        table = np.array(sudoku_list)

        t0 = time()
        tmpSudoku = self.simmulatedAnnealing(table)
        finished = {"sudoku": tmpSudoku.tolist()}
        finished = json.dumps(finished)
        print(f'\nRuntime: { time() - t0:.3f} s')
        # finished is the solved version
        return finished

    def simmulatedAnnealing(self, table):
        solved = False
        while (solved == False):
            decreaseFactor = 0.99
            stuckCount = 0
            fixedSudoku = np.copy(table)
            print('\nInput sudoku table:')
            sudoku.printTable(table)
            sudoku.findZeroes(fixedSudoku)
            listOfBlocks = sudoku.createBlocks()
            tmpSudoku = sa.fillBlocks(table, listOfBlocks)
            sigma = sa.initialSigma(table, fixedSudoku, listOfBlocks)
            score = sa.errorsTotal(tmpSudoku)
            itterations = sa.numOfItterations(fixedSudoku)
            if score <= 0:
                solved = True

            while (solved == False):
                previousScore = score
                for i in range (0, itterations):
                    newState = sa.ChooseNewState(tmpSudoku, fixedSudoku, listOfBlocks, sigma)
                    tmpSudoku = newState[0]
                    scoreDiff = newState[1]
                    score += scoreDiff
                    # print(score)
                    if score <= 0:
                        solved = True
                        break

                sigma *= decreaseFactor
                if score <= 0:
                    solved = True
                    break
                if score >= previousScore:
                    stuckCount += 1
                else:
                    stuckCount = 0
                if (stuckCount > 80):
                    sigma += 2
                if(sa.errorsTotal(tmpSudoku)==0):
                    sudoku.printTable(tmpSudoku)
                    break
        print('\nResult:')
        sudoku.printTable(tmpSudoku)
        return tmpSudoku

input = """{
    "sudoku": [
        [1,0,4, 8,6,5, 2,3,7],
        [7,0,5, 4,1,2, 9,6,8],
        [8,0,2, 3,9,7, 1,4,5],
        [9,0,1, 7,4,8, 3,5,6],
        [6,0,8, 5,3,1, 4,2,9],
        [4,0,3, 9,2,6, 8,7,1],
        [3,0,9, 6,5,4, 7,1,2],
        [2,0,6, 1,7,9, 5,8,3],
        [5,0,7, 2,8,3, 6,9,4]
    ]
}"""
ai = AI()
solution = ai.solve(input)