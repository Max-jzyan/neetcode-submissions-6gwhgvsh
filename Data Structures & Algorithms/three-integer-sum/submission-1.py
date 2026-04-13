class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #[-4, -1, -1, 0, 1,2]
        res = []
        def twoSum(target: int, start: int)->List[List[int]]:
            l = start
            r = len(nums) - 1
            res =[]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([-target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            return res
                    
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -v
            res += twoSum(target, i+1)
            
        return res
