class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        temp_dict = {}
        temp_list = []

        for item in arr:
            if item in temp_dict:
                temp_dict[item] += 1
            else:
                temp_dict[item] = 1
        
        for x in temp_dict.values():
            if x in temp_list:
                return False
            else:
                temp_list.append(x)

        return True
            

s = Solution()

print(s.uniqueOccurrences([1,2,2,2,1,1,3]))