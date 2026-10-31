class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        if len(s) != len(t):
            return False
        for c in s:
            hashS[c] = hashS.get(c, 0) + 1
        for c in t:
            hashT[c] = hashT.get(c, 0) + 1
        for key, value in hashS.items():
            if hashT.get(key, 0) != value:
                return False
        return True
