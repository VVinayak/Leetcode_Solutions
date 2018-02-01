#22 / 22 test cases passed.
	
#Runtime: 34 ms

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        m = len(board); n = len(board[0])

        for i in range(m):
            for j in range(n):
                lives = self.neighbors(board, m, n, i, j)

                if board[i][j] ==  1 and 2 <= lives <= 3:
                    board[i][j] = 3  # 3 is 11  : 01 to 11
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2 # 00 to 10

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1  #shifting bits to the right by 1 position

    def neighbors(self, board, m, n, i, j):
        lives = 0
        for x in range( max(i-1, 0), min(i+1, m -1)+1):
            for y in range(max(j-1, 0), min(j+1, n-1)+1):
                lives +=  board[x][y] & 1

        lives -= board[i][j] & 1

        return lives
