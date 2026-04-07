class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        modified = [] # [[val, idx],[val, idx]]
        for i, v in enumerate(nums):
            modified.append([v, i])
        modified.sort(key=lambda x: x[0])
        l = 0
        r = len(nums) - 1
        
        while l < r:
            if modified[l][0] + modified[r][0] == target:
                return [min(modified[l][1], modified[r][1]),
                        max(modified[l][1], modified[r][1])]
            elif modified[l][0] + modified[r][0] > target:
                r -= 1
            else:
                l += 1
        

        