class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       	left, right = 0, len(nums) - 1

       	while left < right:
       		mid = (left + right) /2
       		if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid -1]:
       			return mid

       		if nums[mid] < nums[mid + 1]:
       			left = mid + 1
       		else:
       			right = mid - 1

       	return left
