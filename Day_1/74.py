# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1
            while right >= left:
                mid = (left + right) // 2
                if nums[mid] == target: return True
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        
        top, bot = 0, len(matrix) - 1
        while bot > top:
            mid = (top + bot + 1) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid
        return binarySearch(matrix[top], target)