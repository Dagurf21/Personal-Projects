"""class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 1:
            return ord(s)
        ret_value = 0
        for index in range(len(s)):
            if index != 0:
                ret_value += abs(ord(s[index - 1]) - ord(s[index]))
                print(abs(ord(s[index - 1]) - ord(s[index])))

        return ret_value
        
    
"""
class Solution: # Not mine but best
    def scoreOfString(self, s: str) -> int:
        score =0
        for i in range(len(s)-1):
            score+=abs(ord(s[i])-ord(s[i+1]))
        return score    

s = Solution()


st = "hello"
exp = 13
if s.scoreOfString(st) == exp:
    print(True)
else:
    print(False, f"{exp} not", s.scoreOfString(st))