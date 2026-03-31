class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s)
        y = sorted(t)
        if len(s) == len(t) and x == y:
            return True
        else:
            return False