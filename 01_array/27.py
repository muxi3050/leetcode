from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=2
        return slow
s = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(s.removeElement(nums,val))