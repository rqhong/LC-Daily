class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        hashmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        """
        depth: 
        max_depth: len(digits)
        comb: len(digits)
        """
        def collect_combination(depth, max_depth, comb, ans):
            if depth == max_depth:
                ans.append(''.join(comb))
                return
            
            number = digits[depth]
            for c in hashmap[number]:
                comb[depth] = c
                collect_combination(depth+1, max_depth, comb, ans)

        ans = []
        comb = [''] * len(digits)
        collect_combination(0, len(digits), comb, ans)

        return ans