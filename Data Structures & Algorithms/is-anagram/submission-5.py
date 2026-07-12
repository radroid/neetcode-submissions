class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = list(s)
        s_letters.sort()
        t_letters = list(t)
        t_letters.sort()
        
        if s_letters == t_letters:
            return True

        return False