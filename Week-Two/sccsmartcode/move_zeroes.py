from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = []
        while 0 in nums:
            nums.remove(0)
            nums1.append(0)
        nums.extend(nums1)


if __name__ == '__main__':
    obj = Solution()
    my_list = [0,1,0,3,12]
    obj.moveZeroes(my_list)
    print(my_list)
