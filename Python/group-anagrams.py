class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmaps = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in hashmaps.keys():
                hashmaps[key] = [s]
            else:
                hashmaps[key].append(s)
        return list(hashmaps.values())