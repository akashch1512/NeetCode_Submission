class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        for ele in nums:
            d[ele] = d.get(ele, 0) + 1
        
        l = [[] for _ in range(len(nums))]
        for key, value in d.items():
            l[value - 1].append(key)
            
        answer = []
        while len(answer) < k:
            answer += l.pop()
        
        return answer