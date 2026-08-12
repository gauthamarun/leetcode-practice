class Solution(object):

  def setZeroes(self, matrix):
    m, n = len(matrix), len(matrix[0])
    rowZero = False

    # 1. First pass: set markers in row 0, col 0, and rowZero flag
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          matrix[0][j] = 0
          if i > 0:
            matrix[i][0] = 0
          else:
            rowZero = True

    # 2. Second pass: update inner cells based on markers
    for r in range(1, m):
      for c in range(1, n):
        if matrix[0][c] == 0 or matrix[r][0] == 0:
          matrix[r][c] = 0

    # 3. Handle column 0
    if matrix[0][0] == 0:
      for r in range(m):
        matrix[r][0] = 0

    # 4. Handle row 0
    if rowZero:
      for c in range(n):
        matrix[0][c] = 0

    return matrix