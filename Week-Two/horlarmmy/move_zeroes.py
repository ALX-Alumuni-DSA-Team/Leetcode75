class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        zero_count = 0
        while 0 in nums:
            nums.remove(0)
            zero_count += 1
        nums.extend(zero_count*[0])

result = Solution()
nums = [0,1,0,3,12]
output = result.moveZeroes(nums)
nums = [0,0,1]
output = result.moveZeroes(nums)
