class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen =set()
        cur_sum = 0
        max_sum = 0
        l = 0
        
        for num in nums:
            while num in seen:
                cur_sum -= nums[l]
                seen.remove(nums[l])
                l += 1
            
            cur_sum += num
            seen.add(num)
            max_sum = max(max_sum , cur_sum)
        
        return max_sum
            
        
