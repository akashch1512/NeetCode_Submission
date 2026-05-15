class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        # Creation of Dictnory
        answer = 0

        for num in nums:
            if (num - 1) not in elements:
                curr = 1
                while (num + curr) in elements:
                    curr += 1
                answer = max(answer, curr)
            
        return answer
