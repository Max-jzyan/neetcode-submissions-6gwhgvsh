class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix + suffix array -> result
        pref = [] # 1, 2, 8,48 pref[i] is the num of on the left
        res = 1
        for n in nums:
            res *= n
            pref.append(res)

        suf = [] # 6, 24 ,48, 48 suf[i] is the num of on the right
        res = 1
        for i in range(len(nums)-1, -1, -1):
            res *= nums[i]
            suf.append(res)
        
        ans = []
        for i in range(0, len(nums)):
            l = i
            r = len(nums) - i - 1
            leftProduct = 1 if l == 0 else pref[l-1]
            rightProduct = 1 if r == 0 else suf[r-1]
            ans.append(leftProduct*rightProduct)
        return ans