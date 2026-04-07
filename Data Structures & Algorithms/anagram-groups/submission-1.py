class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #We can simply use an array of size O(26), since the character set is a through z (26 continuous characters), to count the frequency of each character in a string. Then, we can use this array as the key in the hash map to group the strings.
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