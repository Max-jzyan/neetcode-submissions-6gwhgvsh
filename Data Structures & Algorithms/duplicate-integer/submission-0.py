class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cur = dict()
        for n in nums:
            if cur.get(n) is None:
                cur[n] = 1
            else:
                return True

        return False
        