class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setA = set(nums)
        
        longest = 0
        for n in nums:
            if n - 1 not in setA:
                count = 1

                while n + count in setA:
                    count += 1
                
                longest = max(longest, count)

        return longest