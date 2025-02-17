class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        pairs = []

        def combine_pair(depth, max_depth, pair, base_i):
            
            if depth == max_depth:
                if sum(pair) == n and len(set(pair)) == len(pair):
                    pairs.append(pair[:])   
                return 

            for i in range(base_i, 10):
                pair[depth] = i
                combine_pair(depth+1, max_depth, pair, i)

        depth, max_depth = 0, k
        pair = [0] * k
        combine_pair(depth, max_depth, pair, 1)
        return pairs

