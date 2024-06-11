class Solution:
    """
    Sort the arrays 
    The "sorted" array is arr2, so the elements in arr2 determine the ordering
    Any values that are in arr1 but not in arr2 get added to the back

    we do this using a hash map

    """
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        pos_map = {} # Create a map for the positions


a = [2,3,1,3,2,4,6,7,9,2,19]
b = [2,1,4,3,9,6]
exp = [2,2,2,1,4,3,3,9,6,7,19]

s = Solution()
res = s.relativeSortArray(a, b)

if res != exp:
    print("Not the same, error")
else:
    print(True)

