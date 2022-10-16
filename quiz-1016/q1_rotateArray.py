from collections import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n#if k > len(nums), array was devide into two parts of subarray
        p = n-k#set a pointer to traverse the right subarray
        sub = nums[:n-k]#use sub to store the left subarray
        idx = 0
        #put the right sub array into the former position
        while p < n:
            nums[idx] = nums[p]
            idx += 1
            p += 1
        #put the left sub array into the former position
        for i in range(len(sub)):
            nums[idx] = sub[i]
            idx += 1