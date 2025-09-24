class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # buckets is a dictionary where the key is the first letter of each word in words
        # and the value is a list of the words themselves:
        # buckets[a] = {"a", "acd", "ace"}
        # buckets[b] = {"bb"}
        buckets = defaultdict(list)
        print(buckets)
        for w in words:
            buckets[w[0]].append(w)

        result = 0
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
                if len(word) == 1:
                    print('found')
                    result += 1
                else:
                    buckets[word[1]].append(word[1:])
            i += 1
        return result