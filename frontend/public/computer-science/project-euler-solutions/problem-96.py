import numpy as np
import os
import sys
import re

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p096_sudoku.txt")

file = open(src_filename, "r")

src = file.read()



allGrids = [k for k in  re.split("Grid \d+", src)][1:]


class Sudoku():
    def __init__(self, data):
        """Data is a string where every set of 9 characters are seperated by new lines 9 times"""
        self.board = np.array([[int(n) for n in line] for line in data.lstrip().rstrip().split("\n")])
        self.possibilities = [[[] for r in range(9)] for c in range(9)]
        self.guesses = []

    def getRows(self):
        return [line for line in self.board]

    def getCols(self):
        return [line for line in self.board.T]

    def getSquares(self):
        return [(self.board[x*3:(x+1)*3, y*3:(y+1)*3]).flatten() for y in range(3) for x in range(3)]

    def getPossibilities(self, x, y):
        poss = np.arange(1, 10)
        row = self.getRows()[x]
        col = self.getCols()[y]
        sqr = self.getSquares()[3*(y//3)+x//3]

        used = np.unique(np.hstack([row, col, sqr]))
        used = used[(used!=0)]

        return np.setdiff1d(poss, used)

    def replaceKnown(self):
        indexesThatAreZero = np.argwhere(self.board == 0)
        for index in indexesThatAreZero:
            self.possibilities[index[0]][index[1]] = mboard.getPossibilities(index[0], index[1]).tolist()
            if len(self.possibilities[index[0]][index[1]]) == 1:
                self.board[index[0], index[1]] = self.possibilities[index[0]][index[1]][0]
                self.possibilities[index[0]][index[1]] = []
            elif len(self.possibilities[index[0]][index[1]]) == 0:
                self.guesses[-1][2] += 1
                lastGuess = self.guesses[-1]
                while lastGuess[2] >= len(lastGuess[3]):
                    self.guesses.pop()
                    self.guesses[-1][2] += 1
                    lastGuess = self.guesses[-1]
                self.board = lastGuess[-1]
                self.board[lastGuess[0], lastGuess[1]] = lastGuess[3][lastGuess[2]]

    def makeAGuess(self):
        indexesThatAreZero = np.argwhere(self.board == 0)
        guessCandidates = [[index[0], index[1], 0, self.possibilities[index[0]][index[1]], self.board.copy()] for index in indexesThatAreZero]
        bestGuessToMake = min(guessCandidates, key=lambda x: len(x[3]))
        self.guesses.append(bestGuessToMake)
        self.board[bestGuessToMake[0], bestGuessToMake[1]] = bestGuessToMake[3][bestGuessToMake[2]]

    def solve(self):
        #This will go through and add as we solve pieces of the board
        while 0 in self.board:
            oldBoard = self.board.copy()
            self.replaceKnown()
            while (oldBoard != self.board).any():
                oldBoard = self.board.copy()
                self.replaceKnown()
            if 0 in self.board:
                self.makeAGuess()
            else:
                return self.board

ans = []

for grid in allGrids:
    mboard = Sudoku(grid)
    ans.append("".join(map(str, (mboard.solve()[0, 0:3]).tolist())))

print sum(map(int, ans))
