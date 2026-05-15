class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = -1
        n = len(heights)
        answer = 0

        # Area Formula
        # area = w * l

        while (pointer_1 < n) and (-pointer_2 < n):
            w = (n + pointer_2) - pointer_1
            l = min(heights[pointer_1], heights[pointer_2])
            
            area = w * l
            answer = max(answer, area)

            if heights[pointer_1] <= heights[pointer_2]:
                pointer_1 += 1
            else:
                pointer_2 -= 1
            
        return answer
