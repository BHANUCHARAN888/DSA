#1 Reverse a string
# def reverse_str(s):
#     left = 0
#     right = len(s)-1
#     while left < right:
#         temp = s[left]
#         s[left] = s[right]
#         s[right] = temp
#         left += 1
#         right -= 1
#     return s
# print(reverse_str(['b','h','a','n','u']))
# print(reverse_str(['H','a','n','n','a','h']))
#--------------------------------------------------
#2 Move zeroes
# def move_zeroes(nums):
#     write = 0
#     for read in range(len(nums)):
#         if nums[read] != 0:
#             nums[write] = nums[read] 
#             write += 1
#     for write in range(write, len(nums)):
#         nums[write] = 0
#     return nums
# print(move_zeroes([0,1,0,3,12]))
# print(move_zeroes([0,0,1]))
#---------------------------------------------------
#3 Remove elements
# def remove_elements(nums,vals):
#     write = 0
#     for read in range(len(nums)):
#         if nums[read] != vals:
#             nums[write] = nums[read]
#             write += 1
#     return len(nums[:write])
# print(remove_elements([3,2,2,3],3))
# print(remove_elements([0,1,2,2,3,0,4,2],2))
#---------------------------------------------------
#4 Remove duplicates from sorted array
# def remove_duplicate(nums):
#     write = 1
#     read = 1
#     for read in range(read,len(nums)):
#         if nums[read] != nums[read-1]:
#             nums[write] = nums[read]
#             write += 1
#     return len(nums[:write])
# print(remove_duplicate([1,1,2]))
# print(remove_duplicate([0,0,1,1,1,2,2,3,3,4]))
#---------------------------------------------------
#5 Square of sorted array
# def square_sorted_arr(num):
#     left = 0
#     right = len(num)-1
#     write = right
#     result = [0]*len(num)
#     while left <= right:
#         square_l = num[left]**2
#         square_r = num[right]**2
#         if square_l < square_r:
#             result[write] = square_r
#             right -= 1
#             write -= 1
#         else:
#             result[write] = square_l
#             left += 1
#             write -= 1
#     return result  
# print(square_sorted_arr([-4,-1,0,3,10]))
#----------------------------------------------------
#6 Two sum
# def two_sum(nums, target):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         result = nums[left] + nums[right]
#         if target > result:
#             left += 1
#         elif target < result:
#             right -= 1
#         else:
#             return [left+1,right+1]
# print(two_sum([2,7,11,15],9))
#-----------------------------------------------------
#7 Container with most water
# def most_water(nums):
#     left = 0
#     right = len(nums)-1
#     max_area = 0
#     while left < right:
#         width = right - left
#         area = width * min(nums[left],nums[right])
#         max_area = max(max_area, area)
#         if nums[left] < nums[right]:
#             left += 1
#         else:
#             right -= 1
#     return max_area
# print(most_water([1,8,6,2,5,4,8,3,7]))
#-----------------------------------------------------
#8 Happy number
# def square(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit**2
#         n = n // 10
#     return total
# def happy_number(n):
#     seen = set()
#     while n != 1:
#         if n in seen:
#             return False
#         else:
#             seen.add(n)
#             n = square(n)
#     return True
# print(happy_number(19))
# print(happy_number(18))
# print(happy_number(4))
#-----------------------------------------------------

