class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypted_str = ""
        for value in strs:
            for letter in value:
                encrypted_str += chr(ord(letter) + 14)
            encrypted_str += chr(1114111)
        return encrypted_str

    def decode(self, s: str) -> List[str]:
        value = ""
        answer = []
        for letter in s:
            if letter == chr(1114111):
                answer.append(value)
                value = ""
                continue
            value += chr(ord(letter) - 14)
        return answer
