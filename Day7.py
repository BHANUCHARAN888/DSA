# <----------Two Pointers----------->
# Problem 1: Reverse List Using Two Pointers
# def rev_list(nums):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         temp = nums[left]
#         nums[left] = nums[right]
#         nums[right] = temp
#         left += 1
#         right -= 1
#     return nums
# print(rev_list([1,2,3,4,5]))
#--------------------------------------------
# Problem 2: Valid Palindrome
# def palindrome(string):
#     left = 0
#     right = len(string)-1
#     while left < right:
#         if string[left] != string[right]:
#             return False 
#         left += 1
#         right -= 1
#     return True
# print(palindrome("madam"))
# print(palindrome("racecar"))
# print(palindrome("python"))
#---------------------------------------------
# Problem 3: Move Zeroes In-Place
# def move_zeroes(nums):
#     write = 0
#     for read in range(len(nums)):
#         if nums[read] != 0:
#             nums[write] = nums[read]
#             write += 1
#     for i in range(write, len(nums)):
#         nums[i] = 0
#     return nums
# print(move_zeroes([1,0,2,0,3,0,4]))
#---------------------------------------------
# Problem 4: Remove Duplicates from Sorted Array
# def remove_duplicates(nums):
#     write = 1
#     for read in range(1,len(nums)):
#         if nums[read] != nums[read-1]:
#             nums[write] = nums[read]
#             write += 1
#     return nums[0:write]
# print(remove_duplicates([1,1,2,2,3,4,4]))
# print(remove_duplicates([1,1,1,1,1]))
#-------------------------------------------------
# Problem 5: Two Sum II (Sorted Array)
# def two_sum(nums,target):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         result = nums[left]+nums[right]
#         if result > target:
#             right -= 1
#         elif result < target:
#             left += 1
#         else:
#             return [left,right]
# print(two_sum([2,7,11,15],9))
#-------------------------------------------------