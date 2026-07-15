class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            ans = target-num
            if ans in nums and nums.index(ans)!=i:
                return sorted([i, nums.index(ans)])