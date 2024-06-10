class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0: # is even
            return n
        else:
            return n * 2
    
    def _smallestEvenMultiple(self, n: int) -> int:       
        return n if n % 2 == 0 else n * 2

