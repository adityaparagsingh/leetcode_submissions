class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        nxt = [n] * (n + 1)
        for i in range(n - 1):
            pre[i + 1] = pre[i] + (1 if nums[i] > nums[i + 1] else 0)
        for i in range(n - 2, -1, -1):
            nxt[i] = i if nums[i] > nums[i + 1] else nxt[i + 1]
        ans = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            prev = 0
            ok = True
            for s in range(0, n, k):
                e = s + k - 1
                c = pre[e] - pre[s]
                if c > 1:
                    ok = False
                    break
                if c == 1:
                    if nums[e] > nums[s]:
                        ok = False
                        break
                    j = nxt[s]
                    mn = nums[j + 1]
                    mx = nums[j]
                else:
                    mn = nums[s]
                    mx = nums[e]
                if mn < prev:
                    ok = False
                    break
                prev = mx
            if ok:
                ans += k
        return ans