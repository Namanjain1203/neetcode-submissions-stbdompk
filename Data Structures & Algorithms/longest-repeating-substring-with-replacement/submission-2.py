class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxf = 0
        res = 0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            if count[s[right]] > maxf:
                maxf = count[s[right]]

            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            if (right - left + 1) > res:
                res = right - left + 1

        return res