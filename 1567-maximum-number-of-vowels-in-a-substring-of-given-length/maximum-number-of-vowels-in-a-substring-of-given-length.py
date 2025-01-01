class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}

        window = sum(1 for char in s[:k] if char in vowels)
        max_v = window

        for i in range(1, len(s)-k+1):
            if s[i-1] in vowels:
                window -= 1
            
            if s[i+k-1] in vowels:
                window += 1
            max_v = max(max_v, window)
        return max_v