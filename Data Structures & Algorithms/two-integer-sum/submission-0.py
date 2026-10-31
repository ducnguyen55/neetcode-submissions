class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, v in enumerate(nums):
            difference = target - v
            if difference in hashMap:
                return [hashMap.get(difference), i]
            else:
                hashMap[v] = i
        return []
