from collections import List, dict
#arr = [0,0,0,0,0,1,1,1,1,2,2,5,5,5,8,9,10,11] arr is already sorted
#values = [1,4,5,10]
#output = [5, -1, 12, 17]
class Solution:
    def findEarlestIndex(self, arr: List[int], values: List[int]) -> List[int]:
        res = []
        #use hashmap to record the earliest index
        hm = dict()
        for i, num in enumerate(arr):
            if num not in hm:
                hm[num] = i
        for k in values:
            if k not in hm:#the value did not appeared in arr
                res.append(-1)
            else:
                res.append(hm[k])
        return res