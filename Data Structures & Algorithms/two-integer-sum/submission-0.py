class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            current = nums[i]
            needed = target - current
            if needed in seen:
                return [seen[needed],i]
            else:
                seen[current] = i    
obj = Solution()
print(obj.twoSum([3,4,5,6],7))       