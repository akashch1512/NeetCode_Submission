class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1,]
        suffix_arr = [1,] # kept inveresed to save insert shifts of index

        index = 0
        while index < len(nums) - 1:
            prefix_arr.append(prefix_arr[index] * nums[index])
            index += 1
        
        index = -1
        while -index < len(nums):
            suffix_arr.append(suffix_arr[-index - 1] * nums[index])
            index -= 1
        
        answer = []
        index = 1
        while index <= len(prefix_arr):
            answer.append(prefix_arr[index - 1] * suffix_arr[-index])
            index += 1

        return answer

            

        