class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for s in strs:
            tmp = str(sorted(s))
            if result.get(tmp) is None:
                result[tmp] = [s]
            else:
                result[tmp].append(s)
        answer = []
        for v in result.values():
            answer.append(v)
        return answer