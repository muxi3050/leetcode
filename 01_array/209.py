from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        left = 0
        right = 0
        currentsum = 0
        while right<len(nums):
            currentsum+=nums[right]
            while currentsum>=target:
                ans = min(ans,right-left+1)
                currentsum-=nums[left]
                left+=1
            right+=1
        return 0 if ans==float('inf') else ans
s = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target,nums))

