class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,n in enumerate(nums):
            j=target-n
            if j in hash:
                return[hash[j],i]
            hash[n]=i
        return