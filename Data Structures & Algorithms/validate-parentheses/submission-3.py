class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        seen = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack.pop()!=seen[ch]:
                    return False
        return len(stack) == 0