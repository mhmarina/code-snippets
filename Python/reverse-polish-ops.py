import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            if t in ["*", "/", "+", "-"]:
                # order matters here
                # LIFO means first popped is the rightmost operand
                op_2 = stack.pop()
                op_1 = stack.pop()
                result = ""
                if t == "*":
                    result = op_1 * op_2
                if t == "+":
                    result = op_1 + op_2
                if t == "/":  
                    # handle division by 0 
                    if op_2 == 0:
                        result = 0
                    else:                     
                        result = op_1 / op_2
                if t == "-":
                    result = op_1 - op_2
                stack.append(int(result))
            else:
                stack.append(int(t))
        return stack.pop()
