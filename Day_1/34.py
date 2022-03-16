# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1, -1]
        
        def binarySearchL():
            right = len(nums) - 1
            left = 0
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binarySearchR():
            right = len(nums) - 1
            left = 0
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            return left
                
        l = binarySearchL()
        if nums[l] != target:
            return [-1, -1]
        r = binarySearchR()

        return [l, r]