class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        map = [0] * 26
        for letter in s:
            map[ord(letter) - 97] += 1
        
        for letter in t:
            map[ord(letter) - 97] -= 1
        
        return not any(map)