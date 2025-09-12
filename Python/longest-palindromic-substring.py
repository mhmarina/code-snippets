class Solution:
    def longestPalindrome(self, s: str) -> str:
        # use every index as center

        max_len = -1
        max_string = ""

        # odd length palindromes
        for i in range(len(s)):
            j = 1
            curr_len = 1

            while (i + j < len(s)) and (i - j >= 0):
                right = s[i+j]
                left = s[i-j]
                middle = s[i]
                if (right == left):
                    curr_len += 2
                    j += 1
                else:
                    break

            if curr_len > max_len:
                max_len = curr_len
                max_string = s[i-j+1 : i+j]
                if curr_len == 1:
                    max_string = s[i]

        # even length palindromes
        for i in range(len(s)):
            if(i+1 < len(s) and s[i] == s[i+1]):
                curr_len = 2
                j = 1
                while (i + j + 1 < len(s)) and (i - j >= 0):
                    right = s[i+j+1]
                    left = s[i-j]
                    middle = s[i]
                    if (right == left):
                        curr_len += 2
                        j += 1
                    else:
                        break

                if curr_len > max_len:
                    max_len = curr_len
                    max_string = s[i-j+1 : i+1+j]
                
        return max_string