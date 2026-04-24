class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])

        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        req = (n * m) // 2

        while low <= high:
            mid = (low + high) // 2

            count = 0
            for row in mat:
                l, r = 0, m
                while l < r:
                    md = (l + r) // 2
                    if row[md] <= mid:
                        l = md + 1
                    else:
                        r = md
                count += l

            if count <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low
