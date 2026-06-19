# Retention check
# Revision
# ~ Squares of sorted array
# def square_sorted_array(num):
#     left = 0
#     right = len(num)-1
#     write = len(num)-1
#     result = [0]*len(num)
#     while left <= right:
#         sq_l = num[left]**2
#         sq_r = num[right]**2
#         if sq_l < sq_r:
#             result[write] = sq_r
#             write -= 1
#             right -= 1
#         else:
#             result[write] = sq_l
#             write -= 1
#             left += 1
#     return result
# print(square_sorted_array([-5,-2,0,1,4]))
#---------------------------------------------------------
# ~ Container With Most Water
# def max_water(height):
#     left = 0
#     right = len(height)-1
#     width = 0
#     max_area = 0
#     while left < right:
#         width = right - left
#         area = width * min(height[left], height[right])
#         max_area = max(max_area, area)
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#     return max_area
# print(max_water([1,8,6,2,5,4,8,3,7]))
#-------------------------------------------------------------
# ---Next Pattern: Fast & Slow Pointer---
# Problem 11: Find Middle of a List
# def middle_number(nums):
#     slow = 0
#     fast = 0
#     while fast+1 < len(nums)-1:
#         slow += 1
#         fast += 2
#     return nums[slow]
# print(middle_number([1,2,3,4,5]))
# print(middle_number([1,2,3,4,5,6]))
#-------------------------------------------------------------
# Problem 12: Happy Number
# def square_sum(total):
#     square = 0
#     while total > 0:
#         digit = total % 10
#         square += digit**2
#         total = total // 10
#     return square
# def happy_num(n):
#     seen = set()
#     while n != 1:
#         if n in seen:
#             return False
#         else:
#             seen.add(n)
#             n = square_sum(n)
#     return True
# print(happy_num(19))  
# print(happy_num(4))
#--------------------------------------------------------------
# Problem 13: Detect cycle
# def has_cycle(nums):
#     slow = 0
#     fast = 0
#     while fast < len(nums):
#         slow = nums[slow]
#         fast = nums[nums[fast]]
#         if slow == fast:
#             return True
#     return False
# print(has_cycle([1,2,3,4,2]))
#----------------------------------------------------------------

## LEETCODE
# TODO:(344) REVERSE ARRAY (IN PLACE)
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         left = 0
#         right = len(s)-1
#         while left < right:
#             temp = s[left]
#             s[left] = s[right]
#             s[right] = temp
#             left+=1
#             right-=1
#         return s
#---------------------------------
# TODO:(283) MOVE ZEROES
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         left = 0
#         right = len(nums)-1
#         write = 0
#         while left <= right:
#             if nums[left] != 0:
#                 nums[write] = nums[left]
#                 write += 1
#             left += 1
#         for i in range(write, len(nums)):
#             nums[i] = 0
#         return nums
#-----------------------------------
# TODO:(27) REMOVE ELEMENT
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         left = 0
#         right = len(nums)-1
#         write = 0
#         while left < right:
#             if nums[left] != val:
#                 nums[write] = nums[left]
#                 write += 1
#             left += 1
#         return write
#------------------------------------
# TODO:(28) REMOVE DUPLICATE
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         write = 1
#         read = 1
#         for read in range(read,len(nums)):
#             if nums[read] != nums[read-1]:
#                 nums[write] = nums[read]
#                 write += 1
#         return write
#------------------------------------
# TODO:(977) SQUARE OF SORTED ARRAY
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         left = 0
#         right = len(nums)-1
#         write = len(nums)-1
#         result = [0]*len(nums)
#         while left <= right:
#             square_left = nums[left]**2
#             square_right = nums[right]**2
#             if square_left < square_right:
#                 result[write] = square_right
#                 write -= 1
#                 right -= 1
#             else:
#                 result[write] = square_left
#                 write -= 1
#                 left += 1
#         return result
#-------------------------------------
# TODO:(167) TWO SUM 2
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left = 0
#         right = len(numbers)-1
#         result = 0
#         while left < right:
#             result = numbers[left]+numbers[right]
#             if result > target:
#                 right -= 1
#             elif result < target:
#                 left += 1
#             else:
#                 return [left+1, right+1]
#---------------------------------------
# TODO:(11) CONTAINER WITH MOST WATER
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left = 0
#         right = len(height)-1
#         width = 0
#         max_area = 0
#         while left < right:
#             width = right - left
#             area = width * min(height[left], height[right])
#             max_area = max(max_area, area)
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return max_area
#---------------------------------------