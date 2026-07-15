class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for val in nums:
            if val in count:
                count[val]+=1
            else:
                count[val]=1
        for val in count.values():
            if val>1:
                return True
        return False


        
        