#58 / 58 test cases passed.

#Runtime: 2279 ms

#  In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

# An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s. 

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# Algorithms: For each position (i, j) of the grid matrix, we try to extend in each of the four directions (left, right, up, down) as long as possible, then take the minimum length of 1's out of the four directions as the order of the largest axis-aligned plus sign centered at position (i, j).

# Optimizations: Normally we would need a total of five matrices to make the above idea work -- one matrix for the grid itself and four more matrices for each of the four directions. However, these five matrices can be combined into one using two simple tricks:

#     For each position (i, j), we are only concerned with the minimum length of 1's out of the four directions. This implies we may combine the four matrices into one by only keeping tracking of the minimum length.

#     For each position (i, j), the order of the largest axis-aligned plus sign centered at it will be 0 if and only if grid[i][j] == 0. This implies we may further combine the grid matrix with the one obtained above.

# Implementations:

#     Create an N-by-N matrix grid, with all elements initialized with value N.
#     Reset those elements to 0 whose positions are in the mines list.
#     For each position (i, j), find the maximum length of 1's in each of the four directions and set grid[i][j] to the minimum of these four lengths. Note that there is a simple recurrence relation relating the maximum length of 1's at current position with previous position for each of the four directions (labeled as l, r, u, d).
#     Loop through the grid matrix and choose the maximum element which will be the largest axis-aligned plus sign of 1's contained in the grid.


class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[N] * N for i in range(N)]
        
        for m in mines:
            grid[m[0]][m[1]] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0

            for j, k in zip(range(N), reversed(range(N))):
                l = l + 1 if grid[i][j] != 0 else 0
                if (l < grid[i][j]):
                    grid[i][j] = l

                r = r + 1 if grid[i][k] != 0 else 0
                if (r < grid[i][k]):
                    grid[i][k] = r

                u = u + 1 if grid[j][i] != 0 else 0
                if (u < grid[j][i]):
                    grid[j][i] = u

                d = d + 1 if grid[k][i] != 0 else 0
                if (d < grid[k][i]):
                    grid[k][i] = d

        res = 0

        for i in range(N):
            for j in range(N):
                if (res < grid[i][j]):
                    res = grid[i][j]

        return res
