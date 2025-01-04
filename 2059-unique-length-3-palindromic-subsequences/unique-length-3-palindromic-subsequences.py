class Solution(object):
    def __init__(self):
        self.sub_s = []
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """

        # def sub_palindrome(pivot):
            
        #     for left in range(pivot-1, -1, -1):
        #         for right in range(pivot + 1, len(s)):
        #             if s[left] == s[right]:
        #                 substr = s[left]+s[pivot]+s[right]
        #                 self.sub_s.append(substr)
        
        # for i in range(1, len(s)-1):
        #     sub_palindrome(i)

        # return len(set(self.sub_s))
        # Track unique palindromic subsequences
        unique_palindromes = set()
        
        # Precompute first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}
        
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
        
        # Iterate through each character as a potential pivot
        for pivot in set(s):
            if pivot in first_occurrence and pivot in last_occurrence:
                left = first_occurrence[pivot]
                right = last_occurrence[pivot]
                
                # If there is a valid range between the leftmost and rightmost occurrences
                if right - left > 1:
                    # Collect all unique characters between the range
                    middle_chars = set(s[left + 1:right])
                    for char in middle_chars:
                        unique_palindromes.add(pivot + char + pivot)
        
        return len(unique_palindromes)