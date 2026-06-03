class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # qzxyzoi
        # pwwk
        # l = 0, r = 0, v = p , maxLen = 1, soFar = {(p,0)}
        # l = 0, r = 1, v = w, maxLen = 2, soFar = {(p,0),(w,1)}
        # l = 0, r = 2, v= w -> l = 1, soFar = {(p,0),(w,2)}
        l = prevL = 0
        maxLength = 0
        soFar = dict() # store a pair (character, index)
        for r, v in enumerate(s):
            if soFar.get(v, None) is not None:
                oldL = l
                l = soFar[v] + 1 # it should move to one index after the first repetition
                for i in range(oldL, l):
                    soFar.pop(s[i], None)
                soFar[v] = r
            else:
                curLen = r - l + 1
                if curLen > maxLength:
                    maxLength = curLen
                soFar[v] = r
        return maxLength
