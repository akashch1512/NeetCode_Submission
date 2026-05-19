class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = dict()
        left = 0
        answer = 0
        max_freq = 0
        
        for right in range(len(s)):
            # Add Elements to Dict
            d[s[right]] = d.get(s[right], 0) + 1
            max_freq = max(max_freq, d[s[right]])

            # More Optimized Checking
            while (right - left + 1) - max_freq > k and left < right:
                d[s[left]] -= 1
                left += 1
        
            answer = max(answer, right - left + 1)
        
        return answer
