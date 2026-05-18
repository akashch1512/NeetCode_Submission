class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1

        high_left = 0
        high_right = 0
        answer = 0

        while left <= right:
            if high_left <= high_right:
                answer += max(0, high_left - height[left])
                high_left = max(high_left, height[left])
                left += 1
            
            else:
                answer += max(0, high_right - height[right])
                high_right = max(high_right, height[right])
                right -= 1
        
        return answer

