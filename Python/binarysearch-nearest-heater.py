class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # returns min distance
        def binary_search(ls, target):
            low = 0
            high = len(ls)-1
            middle = sys.maxsize
            while(low <= high):
                middle = floor((high + low)/2)
                if target == ls[middle]:
                    break

                if target > ls[middle]:
                    low  = middle + 1
                elif target < ls[middle]:
                    high = middle - 1

            # lets just return the closest value
            left = sys.maxsize
            right = sys.maxsize

            if middle > 0:
                left = ls[middle-1]

            if middle < len(ls)-1:
                right = ls[middle+1]

            return min(min(abs(target-right), abs(target-ls[middle])), abs(target-left))

        heaters = list(set(heaters))
        heaters.sort()
        max_min_dist = -1

        for house in houses:
            min_dist = binary_search(heaters, house)
            if min_dist > max_min_dist:
                max_min_dist = min_dist

        return max_min_dist
