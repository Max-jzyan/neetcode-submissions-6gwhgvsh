class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        table1 = dict()
        table2 = dict()
        for ch in s:
            if table1.get(ch) is None:
                table1[ch] = 1
            else:
                table1[ch] += 1
        for ch in t:
            if table2.get(ch) is None:
                table2[ch] = 1
            else:
                table2[ch] += 1
        
        for k, v in table1.items():
            if table2.get(k) is None or table2[k] != v:
                return False
        return True
        