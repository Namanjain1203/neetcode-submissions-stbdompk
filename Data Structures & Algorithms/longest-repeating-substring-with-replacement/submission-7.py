class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        i = 0
        res = 0
        for j in range(len(s)):
            if s[j] in count:
                count[s[j]] +=1
            else:
                count[s[j]] = 1
            if count[s[j]] > maxf:
                maxf = count[s[j]]
            if (j-i+1) - maxf > k :
                count[s[i]] -= 1
                i +=1
            if j-i+1 > res:
                res = j-i+1
        return res