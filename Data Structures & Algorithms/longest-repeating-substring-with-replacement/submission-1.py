class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count = {}
            maxf= 0
            for j in range(i,len(s)):
                if s[j] in count:
                    count[s[j]]+=1
                else:
                    count[s[j]]=1
                if count[s[j]] > maxf:
                    maxf=count[s[j]]
                if (j-i+1) - maxf<=k:
                    if (j - i + 1) > res:
                        res = j - i + 1

        return res