# We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

# For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

# We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

# Return true if we can build the pyramid all the way to the top, otherwise false. 

#63 / 63 test cases passed.

#Runtime: 42 ms

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # creating the mapping from first 2 elemnts of every triple to the third triple
        pyramid_map = {}
        for triple in allowed:
            if triple[0:2] not in pyramid_map:
                pyramid_map[triple[0:2]] = []
            pyramid_map[triple[0:2]].append(triple[2])
            
        memo = {}
        return self.dfs(bottom, pyramid_map, memo)
    
    def dfs(self, bottom, pyramid_map, memo):
        if bottom not in memo:
            if len(bottom) == 2 and bottom in pyramid_map:
                memo[bottom] = True
            # checking if we are at the top of the pyramid
            
            else:
                next_layer = []
                # getting a list of all possible blocks for the next layer
                for i in xrange(len(bottom)-1):
                    if bottom[i:i+2] in pyramid_map:
                        next_layer.append(pyramid_map[bottom[i:i+2]])
                    else:
                        memo[bottom] = False
                        return memo[bottom]
                    
                for opt in itertools.product(*next_layer):
                    # creates a cartesian product of all possible blocks in the next layer above bottom
                    if self.dfs(''.join(opt), pyramid_map, memo):
                        memo[bottom] = True
                        return memo[bottom]
                memo[bottom] = False  # in case when no opt formed can act as the next layer
            
        return memo[bottom]
