class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        tb = dict()
        for n in nums:
            tb[n] = tb.get(n, 0) + 1
        
        # we need 0 1 ... len(nums) buckets, each bucket represents frequency, and store the num with that freq
        # we can use sort/min-heap/bucket array to get the top k
        freq = [[] for i in range(0, len(nums)+1)]
        for num, cnt in tb.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) == k:
                return res
            res += freq[i]
        
        return res




        