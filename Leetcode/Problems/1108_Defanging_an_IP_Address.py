class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace(".", "[.]")
        return address
    
s = Solution()

print(s.defangIPaddr("1.1.1.1"))