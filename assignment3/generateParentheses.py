from collections import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #use dynamic programming method
        #el(n pairs) = "(" + p + ")" + q
        #(p+q=n-1)
        if n == 0:
            return []
        total_l = []
        total_l.append([None])# when pairs of parentheses == 0
        total_l.append(["()"])# when pairs of parentheses == 1
        for i in range(2,n+1):
            l = []#record every possible combination when pairs == i   
            for j in range(i):
                now_list1 = total_l[j]# p = j
                now_list2 = total_l[i-1-j]# q = (i-1) - j
                for k1 in now_list1:  
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)
            total_l.append(l)
        return total_l[n]