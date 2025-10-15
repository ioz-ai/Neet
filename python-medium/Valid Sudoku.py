# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

from typing import List

class Solution:

    def HasRowDuplicate(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return True
                s.add(board[i][j])
        return False

    def HasColDuplicate(self, board: List[List[str]]) -> bool:
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in s:
                    return True
                s.add(board[j][i])
        return False

    def HasDuplicate(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                s = set()
                for k in range(3):
                    for t in range(3):
                        if board[i+k][j+t] == ".":
                            continue
                        if board[i+k][j+t] in s:
                            return True
                        s.add(board[i+k][j+t])
        return False
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.HasRowDuplicate(board):
            return False
        if self.HasColDuplicate(board):
            return False
        if self.HasDuplicate(board):
            return False
        return True
