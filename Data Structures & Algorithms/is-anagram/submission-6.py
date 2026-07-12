class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## SOLUTION 1.
        # s_letters = list(s)
        # s_letters.sort()
        # t_letters = list(t)
        # t_letters.sort()
        
        # if s_letters == t_letters:
        #     return True

        # return False

        ## SOLUTION 2.
        if len(s) != len(t):
            return False

        if set(s) != set(t):
            return False
        
        for char in set(s):
            if char not in t:
                return False
            
            char_count_s = sum([1 for c in s if c == char])
            char_count_t = sum([1 for c in t if c == char])

            if char_count_s == char_count_t:
                return True

        return False
            