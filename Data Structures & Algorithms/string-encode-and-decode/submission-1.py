class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypted_str = []
        for value in strs:
            for letter in value:
                encrypted_str.append(chr(ord(letter) + 14))
            encrypted_str.append(chr(1114111))
        return "".join(encrypted_str)

    def decode(self, s: str) -> List[str]:
        value = []
        answer = []
        for letter in s:
            if letter == chr(1114111):
                answer.append("".join(value))
                value = []
                continue
            value.append(chr(ord(letter) - 14))
        return answer
