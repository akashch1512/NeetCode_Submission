class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            print(mid)

            if target == nums[mid]:
                return mid
            
            elif nums[mid] >= nums[start]:
                # mid and start in one half
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
                
            else:
                # mid and end in one half
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
            
        return -1