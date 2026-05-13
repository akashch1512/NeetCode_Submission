class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for word in strs:
            chars = [0]*26
            for char in word:
                chars[(ord(char) - 97)] += 1

            chars = tuple(chars)

            if chars not in hashmap:
                hashmap[chars] = []

            hashmap[chars].append(word)

        return [answer for answer in hashmap.values()]