# You are given a m x n 2D grid initialized with these three possible values.
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room.

# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
# Example
# Given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# return the result:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
 
 
class Solution():
	def wallsAndGates(self, rooms):

		if len(rooms)==0 or len(rooms[0])==0:
			return

		#add all gates to a queue
		queue = []
		for i in range( len(rooms) ):
			for j in range( len(rooms[0]) ):
				if rooms[i][j] == 0:
					queue.append((i,j))

		while queue:
			row, col = queue.pop()
			if row > 0 and rooms[row-1][col] == float("Inf"):
				rooms[row-1][col] = rooms[row][col] + 1
				queue = [(row-1, col)] + queue                
			if row < len(rooms)-1 and rooms[row+1][col] == float("Inf"):
				rooms[row+1][col] = rooms[row][col] + 1
				queue = [(row+1, col)] + queue                    
			if col > 0 and rooms[row][col-1] == float("Inf"):
				rooms[row][col-1] = rooms[row][col] + 1
				queue = [(row, col-1)] + queue             
			if col < len(rooms[0])-1 and rooms[row][col+1] == float("Inf"):
				rooms[row][col+1] = rooms[row][col] + 1
				queue = [(row, col+1)] + queue 

def main():
	rooms = [
         [float("Inf"),  -1 , 0 , float("Inf")],
		 [float("Inf"), float("Inf") ,float("Inf"),  -1],
		 [float("Inf"),  -1 ,float("Inf"),  -1],
  		 [0,  -1, float("Inf"), float("Inf")]
         ]

	test = Solution()
	test.wallsAndGates(rooms)
	print rooms

if __name__ == '__main__':
	main()
