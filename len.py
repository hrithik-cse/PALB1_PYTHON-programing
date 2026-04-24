class Solution:
    def spirallyTraverse(self, mat):
        n = len(mat)
        m = len(mat[0])

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        res = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(mat[top][i])
            top += 1

            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1

        return res
