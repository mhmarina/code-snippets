class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # strat:
        # if we find the first letter, search for second, etc
        # there may be cases where we find 2 instances of the same letter
        # this is why we need a recursive / backtracking algorithm

        # board: char matrix
        # word: word to find
        # index: current index in word
        # x: x pos in board
        # y: y pos in board
        def find(board, word, index, x, y, visited):
            
            curr_board = board[x][y]
            curr_word = word[index]

            if(curr_board == curr_word):
                # base case
                if index == len(word) - 1:
                    return True
                
                visited.add((x, y))

                up = False
                down = False
                right = False
                left = False

                if x > 0 and (x-1, y) not in visited:
                    down = find(board, word, index + 1, x - 1, y, visited)

                if x < len(board)-1 and (x+1, y) not in visited:
                    up = find(board, word, index + 1, x + 1, y, visited)

                if y > 0 and (x, y-1) not in visited:
                    left = find(board, word, index + 1, x, y - 1, visited)

                if y < len(board[0])-1 and (x, y+1) not in visited:
                    right = find(board, word, index + 1, x, y + 1, visited)

                # backtrack
                visited.remove((x,y))
                
                ret_val = up or down or right or left
                return ret_val

            else:
                return False

        # I need a mechanism to keep track of visited nodes
        # hashmap: [[x, y] : bool]
        # 1 = visited, 0 = not visited
        # OR visited set
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if find(board, word, 0, i, j, visited):
                        return True
        
        return False