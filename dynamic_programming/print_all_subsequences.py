class Solution:
    def solve(self, i, n, v, t, ans):
        if i >= n:
            ans.append(t[:])  # Append a copy of t to ans
            return
        
        t.append(v[i])
        self.solve(i + 1, n, v, t, ans)
        t.pop()  # Remove the last element from t
        self.solve(i + 1, n, v, t, ans)
        

    def subsets(self, nums):
        tmp = []
        ans = []
        n = len(nums)
        self.solve(0, n, nums, tmp, ans)
        return ans
