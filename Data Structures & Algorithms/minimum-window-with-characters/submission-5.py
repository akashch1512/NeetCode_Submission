class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_correct(req, window):
            if len(req) != len(window):
                return False

            for key, value in req.items():
                if key not in window or window[key] < value:
                    return False
            return True

        req_char =  dict()
        window_freq = dict()

        for letter in t: 
            req_char[letter] = req_char.get(letter, 0) + 1
        
        # s="OUZODYXAZV"
        # t="XYZ"

        left = 0
        answer = ""
        
        for right in range(len(s)):
            # Adds right sided element to window freq
            if s[right] in req_char:
                window_freq[s[right]] = window_freq.get(s[right], 0) + 1
            
            # Genrates Answer
            if is_correct(req_char, window_freq):
                while right > left and req_char[s[left]] < window_freq[s[left]]:
                    window_freq[s[left]] -= 1
                    left += 1
                    while s[left] not in window_freq:
                        left += 1

                temp_ans = s[left:right + 1] 
                if not answer or len(temp_ans) < len(answer):
                    answer = temp_ans
            
            # Moves Left Side upon condition mate
            while right >= left and (is_correct(req_char, window_freq) or s[left] not in req_char):
                if s[left] in req_char:
                    window_freq[s[left]] = window_freq.get(s[left], 0) - 1
                left += 1
            
        return answer

        



