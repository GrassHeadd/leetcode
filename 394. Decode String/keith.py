from common_imports import *

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack.append([[], 1]) # [str, count]
        num  = []
        for c in s:
            if c.isdigit():
                num.append(c)
            elif c == '[':
                stack.append([[], int("".join(num))])
                num = []
            elif c == ']':
                st, k = stack.pop()
                stack[-1][0].extend(st * k)
            else:
                stack[-1][0].append(c)
        
        return "".join(stack[0][0])


            