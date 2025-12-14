from typing import List


class Solution:
    def isNumeric(self, s: str) -> bool:
        return s in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ret = []
        i = 0
        while i < len(s):
            leng = s[i]
            # while self.isNumeric(s[i+1]):
            while s[i+1] is not "#":
                leng += s[i+1]
                i += 1

            leng = int(leng)
            st = s[i+2:i+2+leng]
            ret.append(st)
            i += leng + 2
        return ret

sol = Solution()
s = sol.encode(["Hello", "World", "!!!"])
print(sol.decode(s))