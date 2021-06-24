class Solution:

    visited = -1
    water = 0
    land = 1

    def solve(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                # Found land, and it is surrounded
                "comment"
                if matrix[i][j] is self.land and self.isSurrounded(i, j, matrix):
                    count += 1
        return count

    def isSurrounded(self, i, j, mat) -> bool:
        # Reached OOB
        if i == -1 or i == len(mat) or j == -1 or j == len(mat[0]):
            return False

        # Reached water or visited
        if mat[i][j] is self.water or mat[i][j] == self.visited:
            return True

        # Mark as visited
        mat[i][j] = self.visited

        # Check if rest of island's bounds are surrounded
        above = self.isSurrounded(i - 1, j, mat)
        below = self.isSurrounded(i + 1, j, mat)
        left = self.isSurrounded(i, j - 1, mat)
        right = self.isSurrounded(i, j + 1, mat)

        return above and below and left and right


res = Solution()

# row, column
n, m = (int(x) for x in input().split())
matrix = []

for i in range(0, n):
    matrix.append([int(j) for j in input().split()])

print(res.solve(matrix))
