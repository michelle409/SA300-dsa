# Problem: Range Sum Query 2D
# Pattern: 2D prefix sum - build matrix, query rectangle in O(1)
# Time: O(m*n) build, O(1) query | Space: O(m*n)

class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (matrix[i-1][j-1]
                    + self.prefix[i-1][j]
                    + self.prefix[i][j-1]
                    - self.prefix[i-1][j-1])

    def sumRegion(self, r1, c1, r2, c2):
        return (self.prefix[r2+1][c2+1]
                - self.prefix[r1][c2+1]
                - self.prefix[r2+1][c1]
                + self.prefix[r1][c1])