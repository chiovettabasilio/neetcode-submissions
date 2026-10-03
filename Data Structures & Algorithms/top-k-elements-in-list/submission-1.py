class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        j = k
        c = Counter(nums)
        res = []
        for el, count in c.most_common(k):
            if j > 0:
                res.append(el)
                j -= 1
        return res