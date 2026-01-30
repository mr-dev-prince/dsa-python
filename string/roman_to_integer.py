class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman.get(s[i]) < roman.get(s[i + 1]):
                res -= roman.get(s[i])
            else:
                res += roman.get(s[i])

        return res
