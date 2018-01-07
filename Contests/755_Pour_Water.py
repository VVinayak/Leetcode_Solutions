#37 / 37 test cases passed.
	
#Runtime: 92 ms

#  We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each index is 1. After V units of water fall at index K, how much water is at each index?

# Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:
# If the droplet would eventually fall by moving left, then move left.
# Otherwise, if the droplet would eventually fall by moving right, then move right.
# Otherwise, rise at it's current position.
# Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, "level" means the height of the terrain plus any water in that column.

# We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block. 

class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """

        for _ in range(V):
            index = -1
            for i in range(K-1,-1,-1):
                if heights[i] < heights[i+1]:
                    index = i
                elif heights[i] > heights[i+1]:
                    break
                    
            if index != -1:
                heights[index] = heights[index] + 1
                continue
                
            index = -1
            for i in range(K+1, len(heights)):
                if heights[i] < heights[i-1]:
                    index = i
                elif heights[i] > heights[i-1]:
                    break
                    
            if index != -1:
                heights[index] = heights[index] + 1
            else:
                heights[K] = heights[K] + 1
                
            
        return heights
        
