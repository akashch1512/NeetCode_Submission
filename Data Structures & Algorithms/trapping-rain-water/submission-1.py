class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left = [0] * n
        curr_high = 0
        for index, l in enumerate(height):
            left[index] = curr_high

            if l > curr_high:
                curr_high = l
            
        curr_high = 0
        right = [0] * n
        for index in range(n - 1, -1, -1):
            right[index] = curr_high

            if height[index] > curr_high:
                curr_high = height[index]
        
        answer = 0
        for index in range(n):
            print(min(left[index],right[index]))
            answer += max(0,min(left[index],right[index]) - height[index])
    
        return answer
        