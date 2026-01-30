class Solution:
    def isVowel(self, ch):
        return ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"

    def beautifulSubstrings(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            con = 0
            vow = 0
            for j in range(i, len(s)):
                if self.isVowel(s[j]):
                    vow += 1
                else:
                    con += 1

                if con == vow and (vow * con) % k == 0:
                    res += 1

        return res
