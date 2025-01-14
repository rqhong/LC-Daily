class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # [3, [, a, 2, [, c]

        current_string = ""
        stack = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == "[":
                stack.append((num, current_string))
                current_string = ""
                num = 0
            elif c == "]":
                last_num, last_str = stack.pop()
                current_string = last_str + current_string * int(last_num)
            else:
                current_string += c
        return current_string