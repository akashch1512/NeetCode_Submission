class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        pointer_1 = 0
        pointer_2 = n - 1

        answer = 0

        while (pointer_1 < pointer_2):
            w = pointer_2 - pointer_1
            l = min(heights[pointer_1], heights[pointer_2])
            
            area = w * l
            answer = max(answer, area)

            if heights[pointer_1] <= heights[pointer_2]:
                pointer_1 += 1
            else:
                pointer_2 -= 1
            
        return answer
