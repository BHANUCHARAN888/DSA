# problem 9: Squares of a Sorted Array
# def squares_sorted_array(nums):
#     left = 0
#     right = len(nums)-1
#     write = len(nums)-1
#     result = [0]*len(nums)
#     while left <= right:
#         square_l = nums[left]**2
#         square_r = nums[right]**2
#         if square_l < square_r:
#             result[write] = square_r
#             write -= 1
#             right -= 1
#         else:
#             result[write] = square_l
#             write -= 1
#             left += 1
#     return result
# print(squares_sorted_array([-4,-1,0,3,10]))
#---------------------------------------------
# Revision square of sorted array
# def square_sorted_arr(num):
#     left = 0
#     right = len(num)-1
#     write = len(num)-1
#     result = [0]*len(num)
#     while left <= right:
#         square_l = num[left]**2
#         square_r = num[right]**2
#         if square_l < square_r:
#             result[write] = square_r
#             write -= 1
#             right -= 1
#         else:
#             result[write] = square_l
#             write -= 1
#             left += 1
#     return result
# print(square_sorted_arr([-7,-3,2,3,11]))
#--------------------------------------------
# Problem 10: Container With Most Water
# def max_water(height):
#     left = 0
#     right = len(height)-1
#     width = 0
#     max_area = 0
#     while left < right:
#         width = right - left
#         area = width * min(height[left],height[right])
#         max_area = max(max_area, area)
#         if height[left]<height[right]:
#             left += 1
#         else:
#             right -= 1
#     return max_area
# print(max_water([1,8,6,2,5,4,8,3,7]))
# print(max_water([1,1]))  
# print(max_water([4,3,2,1,4]))  
# print(max_water([1,2,1]))
# print(max_water([2,3,4,5,18,17,6]))
# print(max_water([5,5,5,5]))
# print(max_water([10,1]))
#-----------------------------------------------------