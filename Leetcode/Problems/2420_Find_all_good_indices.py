class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        for index in range(len(nums)):
            pass

s = Solution()

res = s.goodIndices([2,1,1,1,3,4,1])
exp = [2,3]

if exp != res:
    print("nopes u are bad")
else:
    print(True)