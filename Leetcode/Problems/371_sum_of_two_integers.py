class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]

        longer = len(a) if len(a) > len(b) else len(b) # Choose the longer binary number

        ret_numer = ""

        for x in range(longer):
            if a[x] == "0" and b[x] == "0":
                ret_numer += "0"
            elif a[x] == "0" and b[x] == "1" or a[x] == "1" and b[x] == "0":
                ret_numer += "1"

        return longer
    

s = Solution()

print(s.getSum(1, 2))