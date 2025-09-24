from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # buckets is a dictionary where the key is the first letter of each word in words
        # and the value is a list of the words themselves:
        # buckets[a] = {"a", "acd", "ace"}
        # buckets[b] = {"bb"}

        # okaayyyy buuuut what if I want to return the original subsequences?
        # idea: the arrays could be a tuple and include the subseq's index from original array?
        buckets = defaultdict(list)
        for i in range(len(words)):
            buckets[words[i][0]].append([words[i], i])

        result_array = []
        i = 0

        # let's match lol
        while i < len(s):
            curr_char = s[i]
            # for example, if curr_char = a
            # get buckets[a] = {"a", "acd", "ace"}
            # check if any of these elements have a length of 1, if so, increment the result
            #                   (pattern has been matched entirely)
            # then, place the remaining patterns in their appropriate buckets:
            # = buckets[c].append("cd", "ce")
            curr_list = buckets[curr_char]
            buckets[curr_char] = []
            for word in curr_list:
                if len(word[0]) == 1:
                    # append the index of the subsequences in words
                    result_array.append(words[word[1]])
                else:
                    buckets[word[0][1]].append([word[0][1:], word[1]])
            i += 1
        # now we get both the number and the subsequences themselves
        print(result_array)
        return len(result_array)