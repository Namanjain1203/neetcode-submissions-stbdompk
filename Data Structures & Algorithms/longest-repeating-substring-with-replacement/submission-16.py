class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i = 0
        freq = 0
        result = 0
        for j in range(len(s)):
            if s[j] in count:
                count[s[j]] +=1
            else:
                count[s[j]] =1
            if count[s[j]] > freq:
                freq = count[s[j]]
            if (j-i+1) - freq > k:
                count[s[i]] -=1
                i+=1
            if j-i+1>result:
                result = j-i+1
        return result