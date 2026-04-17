class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen  = {}
        maxf = 0
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] in seen:
                seen[s[j]] +=1
            else:
                seen[s[j]] = 1
            if seen[s[j]] > maxf:
                maxf = seen[s[j]]
            if (j-i+1) - maxf > k:
                seen[s[i]]-=1
                i+=1
            if j-i+1 > res:
                res = j-i+1
        return res