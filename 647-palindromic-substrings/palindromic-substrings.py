class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def count_palindrome(l, r):
            c = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c

        count = 0
        for i in range(len(s)):
            count += count_palindrome(i,i)
            count += count_palindrome(i,i+1)
        return count
        