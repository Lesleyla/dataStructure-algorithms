from collections import List, deque
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # BFS solution(can also use dfs)
        res = []
        q = deque((1, d) for d in range(1, 10))
        
        while q:
            pos, num = q.pop()
            if pos == n:# check if we meet the length we want
                res.append(num)
            else:
                for j in range(10): # loop through 0~9
                    if abs(num % 10 - j) == k:  # check if the difference between two digits is k
                        q.append((pos + 1, num * 10 + j))      
        return res