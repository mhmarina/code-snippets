class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        intervals.sort(key=lambda i: i[0])
        i = 0
        results = []
        while i < len(intervals):
            interval = intervals[i]
            j = i + 1
            while j < len(intervals):
                right, left = interval
                next_ = intervals[j]
                if(next_[0] >= right and next_[0] <= left):
                    interval[1] = max(left, next_[1])
                    j += 1
                else:
                    break
            results.append(interval)
            i = j 
        return results