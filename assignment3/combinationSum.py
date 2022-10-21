from collections import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, path, res):
            if target == 0:
                res.append(path)
                return
            for i,c in enumerate(candidates):
                remain = target - c
                if remain < 0:
                    break
                dfs(candidates[i:], remain, path + [c], res)
            return []
            
        candidates.sort()
        res = []
        dfs(candidates, target, [], res)
        return res