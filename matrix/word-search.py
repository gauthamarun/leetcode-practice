class Solution(object):

    def exist(self, board, word):
        m, n = len(board), len(board[0])
        w = len(word)

        def backtrack(r, c, index):
            # Base case: Found all characters in word
            if index == w:
                return True

            # Boundary and character match check
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False

            # Mark current cell as visited
            char = board[r][c]
            board[r][c] = "#"

            # Explore all 4 adjacent directions
            found = (
                backtrack(r + 1, c, index + 1)
                or backtrack(r - 1, c, index + 1)
                or backtrack(r, c + 1, index + 1)
                or backtrack(r, c - 1, index + 1)
            )

            # Backtrack (restore original character)
            board[r][c] = char
            return found

        for i in range(m):
            for j in range(n):
                # Optimization: Only start search if the first character matches
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False