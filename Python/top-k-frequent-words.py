class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hm = {}
        for i, word in enumerate(words):
            if word not in hm:
                hm[word] = 0
            hm[word] += 1
        
        # add neg to number to sort by descending
        # sorted defaults to descending (small - large)
        # sorted accepts a tuple for a key, so item[0] is a tiebreaker!
        sort = sorted(hm.items(), key=lambda item: (-item[1], item[0]))

        res = []
        for i in range(k):
            res.append(sort[i][0])

        return res