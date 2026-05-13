class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for word in strs:
            chars = [0]*26
            for char in word:
                chars[(97 - ord(char))] += 1

            chars = "".join([str(char) for char in chars])

            if chars not in hashmap:
                hashmap[chars] = [word] 
            else:
                hashmap[chars].append(word)

        return [answer for answer in hashmap.values()]