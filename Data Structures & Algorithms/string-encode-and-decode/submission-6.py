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
            length = ""
            while s[index] != '#':
                length += s[index]
                index += 1
            length = int(length)

            answer.append(s[index + 1:index + length + 1])
            index += length + 1

        return answer
