def dfs(s, n, result, n_open, n_close):
    if(n == 0):
        return
    if len(s) == n*2:
        result.append(s)
        return

    if n_open < n:
        dfs(s + "(", n, result, n_open+1, n_close)
    if n_close < n_open:
        dfs(s + ")", n, result, n_open, n_close+1)

class Solution:    
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        dfs("", n, result, 0, 0)
        return result

def validate(s):
    # validate using stack
    stack = []
    for c in s:
        if c == ")":
            if len(stack) == 0 or stack.pop(-1) != "(":
                return False
        if c == "(":
            stack.append(c)
    if(len(stack) > 0):
        return False
    return True

# def dfs(s, n, result):
#     if(n == 0):
#         return
#     if len(s) == n*2:
#         # base case, and validate 
#         if validate(s):
#             result.append(s)
#         return
#     # abandon invalid strings from the start
#     if len(s) > 0:
#         stack = []
#         for c in s:
#             if c == ")":
#                 if len(stack) == 0 or stack.pop(-1) != "(":
#                     return
#             if c == "(":
#                 stack.append(c)
#     dfs(s + "(", n, result)
#     dfs(s + ")", n, result)

# class Solution:    
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = []
#         dfs("", n, result)
#         return result