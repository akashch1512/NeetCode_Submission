class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for string in strs:
            encoded_string.append(f"{len(string)}#{string}")
        return "".join(encoded_string)


    def decode(self, s: str) -> List[str]:
        answer = []
        index = 0

        while index < len(s):
            # Finding length of string
            l = index
            while s[index] != '#':
                index += 1
            length = int(s[l:index])

            index += 1

            answer.append(s[index:index + length])
            index += length

        return answer
