class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        r = [0] * len(temperatures)
        mono_stack = []
        for i, t in enumerate(temperatures):
            while mono_stack and t > mono_stack[-1][1]: # top t
                past_i, past_t = mono_stack.pop()
                r[past_i] = i - past_i # current - past
            mono_stack.append((i, t))
        return r