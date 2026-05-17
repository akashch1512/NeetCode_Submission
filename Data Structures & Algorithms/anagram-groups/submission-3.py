class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()

        print(ord("a") - 97)
        print(ord("z") - 97)

        for word in strs:
            letters = [0] * 26

            for letter in word:
                letters[ord(letter) - 97] += 1
            
            tup_word = tuple(letters)
            
            if tup_word not in hash_map:
                hash_map[tup_word] = [word]
            else:
                hash_map[tup_word].append(word)
        
        answer = []
        for ans in hash_map.values():
            answer.append(ans)
        
        return answer