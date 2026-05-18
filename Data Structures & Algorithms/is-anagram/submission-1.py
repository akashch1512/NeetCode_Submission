class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        # renamed it to letters rather keyword map
        letters = [0] * 26
        for letter in s:
            letters[ord(letter) - 97] += 1
        
        for letter in t:
            letters[ord(letter) - 97] -= 1
        
        return not any(letters)