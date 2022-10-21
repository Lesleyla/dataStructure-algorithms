class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(i + 1, tmp + [nums[j]])#the next el appended in tmp must not appeared in tmp
        helper(0, [])
        return res