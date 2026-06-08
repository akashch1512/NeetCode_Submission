class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = dict()

        for word in strs:
            arr = [0] * 26
            
            for letter in word:
                arr[ord(letter) - 97] += 1
        
            arr = tuple(arr)

            letters.setdefault(arr, []).append(word)
        
        ans = []
        for value in letters.values():
            ans.append(value)
        
        return ans