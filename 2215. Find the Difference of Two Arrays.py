class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        return [list(set(nums1) - set(nums2)), 
                list(set(nums2) - set(nums1))]
        # Approach 1
        # set1, set2 = set(nums1), set(nums2)
        # return [[x for x in set1 if x not in set2], 
        #         [x for x in set2 if x not in set1]]

        # Approach 2
        # set1, set2 = set(nums1), set(nums2)
        # return [list(set1 - set2), list(set2 - set1)]
