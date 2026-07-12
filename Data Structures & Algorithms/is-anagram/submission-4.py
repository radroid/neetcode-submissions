class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = sorted(list(s))
        t_letters = sorted(list(t))
        
        if s_letters == t_letters:
            return True

        return False