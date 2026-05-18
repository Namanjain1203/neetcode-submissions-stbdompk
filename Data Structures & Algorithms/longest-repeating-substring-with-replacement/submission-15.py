class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i = 0
        max_f = 0
        res = 0
        for j in range(len(s)):
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]] = 1
            if count[s[j]] > max_f:
                max_f = count[s[j]]
            if (j-i+1) - max_f > k:
                count[s[i]] -= 1
                i+=1
            if j-i+1 > res:
                res = j-i+1
        return res
        