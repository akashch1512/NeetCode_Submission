class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()

        for word in strs:
            letters = [0] * 26

            for letter in word:
                letters[ord(letter) - 97] += 1
            
            tup_word = tuple(letters)
            
            if tup_word not in hash_map:
                hash_map[tup_word] = [word]
            else:
                hash_map[tup_word].append(word)
        
        return list(hash_map.values())