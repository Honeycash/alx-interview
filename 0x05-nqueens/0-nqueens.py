#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """

import sys

class NQueen:
    """ Class for solving N Queen Problem """
    def __init__(self, n):
        """ Initialize the board and variables """
        self.n = n
        self.x = [0 for _ in range(n + 1)]  # Position of queens
        self.res = []  # Store results
    
    def place(self, k, i):
        """ Checks if k-th Queen can be placed in column i """
        for j in range(1, k):
            # Check column and diagonal conflicts
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True
    
    def nQueen(self, k):
        """ Tries to place all queens on the board """
        # Try placing the k-th Queen in all columns
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    # All queens placed, save the solution
                    solution = [(i - 1, self.x[i] - 1) for i in range(1, self.n + 1)]
                    self.res.append(solution)
                else:
                    # Place the next queen
                    self.nQueen(k + 1)
        return self.res

# Main program execution
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    queen = NQueen(N)
    res = queen.nQueen(1)
    
    # Print the result in a more readable format
    for solution in res:
        print(solution)

