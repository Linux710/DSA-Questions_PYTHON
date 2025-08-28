class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#3 2 1
        n = len(nums)
        idx = -1
        
        # check if there is any breakpoint
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        #print(idx)
        if idx == -1:
            # in place reverse
            nums.reverse()

            # break always used inside loop
        
        else:
            for i in range(n-1,idx,-1):
                if nums[i] > nums[idx]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    break
                # if we dont mention immediate break then it will search
                # other integer,resulting in wrong answer
                # reversed(list) can be used to rverse based on iteration
            nums[idx+1:] = reversed(nums[idx+1:])
