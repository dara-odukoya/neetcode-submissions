class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for val in nums:
            if val in count:
                count[val]+=1
            else:
                count[val]=1
        for vals in count.values():
            if vals>1:
                return True
        return False
        