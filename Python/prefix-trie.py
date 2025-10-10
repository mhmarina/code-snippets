# longest common prefix
class TrieNode:
    def __init__(self):
        # children is a dictionary with a character key
        # and another treenode for each character
        self.children = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # let's create a prefix tree for every string in arr1:
        trie = TrieNode()
        for s in arr1:
            pointer = trie
            for i in str(s):
                if i not in pointer.children:
                    # new node here
                    pointer.children[i] = TrieNode()  
                pointer = pointer.children[i]   

        max_len = 0
        # traverse tree
        for s in arr2:
            pointer = trie
            curr_len = 0
            for i in str(s):
                if i in pointer.children:
                    curr_len += 1
                    pointer = pointer.children[i]
                else:
                    break
            if curr_len > max_len:
                max_len = curr_len

        
        return max_len

