class Solution:
    def heightChecker(self, heights: list[int]) -> int: 
        count = 0
        expect = sorted(heights)
        for x in range(len(heights)):
            if heights[x] != expect[x]:
                count += 1
        return count
        

    

s = Solution()

print(s.heightChecker([5,1,2,3,4]))
