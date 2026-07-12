class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two checks need to be done to ensure it is an anagram. 
        # 1. Ensure the length is the same for both. Trivial check.
        # 2. Ensure that the number of each of the letters in the strings are the same. 
        # We can just do #2 and it would actaully work, but to improve the performance with a trivial 
        # len() check would be nice. Another performance evaluation that we can do is use sets for each
        # letter and ensure that both sets have the same letters. If they do then we conduct a final check\
        # of the letters in each of the strings.
        
        # if len(s) != len(t):
        #     return False

        s_letters = list(s)
        s_letters.sort()
        t_letters = list(t)
        t_letters.sort()

        print(s_letters)
        print(t_letters)
        
        if s_letters == t_letters:
            return True

        return False