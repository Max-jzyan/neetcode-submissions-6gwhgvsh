class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find all the possible starting nums + note all the possible sequential
        s = set(nums)
        tb = dict()
        longest = 0
        for n in nums:
            if n-1 in s:
                continue
            else:
                length = 1
                while (n+length) in s:
                    length += 1
                longest = max(length, longest)
        return longest
        
