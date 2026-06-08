class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26

        # Parsing first word
        for letter in s:
            letters[ord(letter) - 97] += 1
        
        # Parsing the Second Word
        for letter in t:
            letters[ord(letter) - 97] -= 1
        
        # checking for remaning
        return not any(letters)