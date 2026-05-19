class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        a = set()
        answer = 0
    
        for char in s:
            if char in a:
                index = start
                
                while index < end:
                    if char == s[index]:
                        start = index + 1
                        end += 1
                        break
                
                    a.remove(s[index])
                    index += 1
            
            else:
                a.add(char)
                end += 1
    
            answer = max(answer, end - start)
        
        return answer