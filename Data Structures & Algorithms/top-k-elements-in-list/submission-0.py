class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, freq in count.items():
            arr[freq].append(num)

        answer = []
        index = -1
        while len(answer) < k:
            answer.extend(arr[index])
            index -= 1

        return answer