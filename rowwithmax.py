class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])

        def first_one(row):
            l, r = 0, m - 1
            ans = m

            while l <= r:
                mid = (l + r) // 2
                if row[mid] == 1:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1

            return ans

        max_ones = 0
        res = -1

        for i in range(n):
            idx = first_one(arr[i])
            ones = m - idx

            if ones > max_ones:
                max_ones = ones
                res = i

        return res if max_ones > 0 else -1
