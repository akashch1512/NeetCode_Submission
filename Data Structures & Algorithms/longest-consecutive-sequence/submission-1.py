class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        answer = 0

        # Big Mistake Iterating Over list rather then set ! (Dublicatess!! )
        for num in elements:
            if (num - 1) not in elements:
                curr = 1
                while (num + curr) in elements:
                    curr += 1
                answer = max(answer, curr)
            
        return answer
