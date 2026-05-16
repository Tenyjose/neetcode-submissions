class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        S_to_T = {}
        T_to_S = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in S_to_T:
                if S_to_T[char_s] != char_t:
                    return False
            else:
                S_to_T[char_s] = char_t

            
            if char_t in T_to_S:
                if T_to_S[char_t] != char_s:
                    return False
            else:
                 T_to_S[char_t] = char_s

        return True





        