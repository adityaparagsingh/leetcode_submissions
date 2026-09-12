import bisect
class Solution:
    def maximumWeight(self, a):
        original_index = {}
        for i, (l, r, w) in enumerate(a):
            key = (l, r, w)
            if key not in original_index:
                original_index[key] = i

        intervals = sorted(original_index.keys())
        n = len(intervals)

        next_index = [0] * n
        for i in range(n):
            l, r, w = intervals[i]
            next_index[i] = bisect.bisect_right(
                intervals, (r, float('inf'), float('inf'))
            )

        dp = {}

        def solve(i, k):
            if i == n or k == 0:
                return (0, [])
            if (i, k) in dp:
                return dp[(i, k)]

            skip = solve(i + 1, k)

            l, r, w = intervals[i]
            take_score, take_idx = solve(next_index[i], k - 1)
            take_score -= w
            take_idx = sorted(take_idx + [original_index[(l, r, w)]])
            take = (take_score, take_idx)

            # Python tuples/lists compare lexicographically,
            # exactly like C++ pair<long long, vector<int>>
            result = min(skip, take)
            dp[(i, k)] = result
            return result

        return solve(0, 4)[1]