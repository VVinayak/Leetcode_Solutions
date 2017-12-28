#2080 / 2080 test cases passed.
	
#Runtime: 116 ms

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1 = len(nums1)
        size2 = len(nums2)
        if (size1 > size2):
            return self.findMedianSortedArrays(nums2, nums1)
        if size1 == 0:
            if size2%2 == 0 :
                return (nums2[size2/2] + nums2[(size2/2) - 1])/2.0
            else:
                return nums2[(size2)/2]
        
        start = 0
        end = size1
        halflength = (size1 + size2 + 1)/2     #halflength of combined arrays
        flag = 0
        
        while start <= end and flag == 0 :
            midpoint1 = (start + end)/2
            midpoint2 = halflength - midpoint1
            # print midpoint1, midpoint2
            
            if midpoint2 < size2 and midpoint1 > 0 and nums1[midpoint1 - 1] > nums2[midpoint2]:
                # end needs to be decreased
                end = midpoint1 - 1
                # print "End: ",end
            
            elif midpoint1 < size1 and midpoint2 > 0 and nums2[midpoint2 - 1] > nums1[midpoint1]:
                #start needs to be increased
                start = midpoint1 + 1
                # print "Start: ", start
                
            else:
                #midpoint is correct
                # print "Correct"
                if midpoint1 == 0:
                    max_left = nums2[midpoint2 - 1]
                elif midpoint2 == 0:
                    max_left = nums1[midpoint1 - 1]
                else:
                    max_left = max(nums1[midpoint1 - 1], nums2[midpoint2 - 1])
                    
                if (size1 + size2)%2 == 1:
                    # print "Odd"
                    return max_left
                    
                if midpoint1 == size1:
                    min_right = nums2[midpoint2]
                elif midpoint2 == size2:
                    min_right = nums1[midpoint1]
                else:
                    min_right = min(nums1[midpoint1], nums2[midpoint2])
                
                # print "Left and Right Indices: ", max_left, min_right    
                # print "Even", (max_left + min_right)/2.0
                return (max_left + min_right)/2.0
