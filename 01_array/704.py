from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            middle = left + (right-left)//2
            if nums[middle] > target:
                right = middle - 1     #important
            elif nums[middle] < target:
                left = middle + 1      #important
            else:
                return middle
        return -1
s = Solution()
nums = [-1,0,3,5,9,12]
target = 2
print(s.search(nums,target))