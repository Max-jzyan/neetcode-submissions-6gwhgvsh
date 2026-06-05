class Solution:
    def isValid(self, s: str) -> bool:
        table = {"}":"{", "]":"[", ")":"("}
        stack = []
        for ch in s:
            if stack and ch in table:
                if table[ch] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch) 
        return False if stack else True