class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = False
        if s[-1] in '{[(':
            return False
        for paren in s:
            if paren == '(':
                stack.append(paren)
            elif paren == ')' and len(stack) != 0 and stack[-1] == '(':
                valid = True
                stack.pop()
            elif paren == '[':
                stack.append(paren)
            elif paren == ']' and len(stack) != 0 and stack[-1] == '[':
                valid = True
                stack.pop()
            elif paren == '{':
                stack.append(paren)
            elif paren == '}' and len(stack) != 0 and stack[-1] == '{':
                valid = True
                stack.pop()
            else:
                return False
            
        if len(stack) != 0:
            return False

        return valid

s = Solution()

print(s.isValid('(())()'))
print(s.isValid('()[{}]'))
print(s.isValid('(]()'))