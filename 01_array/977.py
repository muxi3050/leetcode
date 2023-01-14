from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, index = 0, len(nums)-1, len(nums)-1
        ans = [-1]*len(nums)
        while left<=right:
            leftnumber = nums[left]**2
            rightnumber = nums[right]**2
            if leftnumber < rightnumber:
                ans[index]=rightnumber
                right-=1
                index-=1
            else:
                ans[index]=leftnumber
                left+=1
                index-=1
        return ans
s = Solution()
nums = [-4,-1,0,3,10]
print(s.sortedSquares(nums))
