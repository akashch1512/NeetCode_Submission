class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        start = 0
        end = x

        while start <= end:
            mid = (start + end) // 2
            curr = mid * mid

            if curr == x:
                return mid 
            
            elif curr > x:
                end = mid - 1
            
            elif curr < x:
                start = mid + 1
            
        return end