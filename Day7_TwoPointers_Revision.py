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
#---------------------------------------------
# Problem 2: Valid Palindrome
# def palindrome(string):
#     left = 0
#     right = len(string)-1
#     while left < right:
#         if string[left] != string[right]:
#             return False
#         else:
#             left += 1
#             right -= 1
#     return True
# print(palindrome("madam"))
# print(palindrome("python"))
# print(palindrome("racecar"))
#---------------------------------------------
# Problem 3: Move Zeroes
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
# print(move_zeroes([0,2,4,6,0,8,0,10]))
#---------------------------------------------
# Problem 4: Remove Duplicates from Sorted Array
# def remove_duplicate(nums):
#     write = 1
#     for read in range(write, len(nums)):
#         if nums[read] != nums[read-1]:
#             nums[write] = nums[read]
#             write += 1
#     return nums[0:write]
# print(remove_duplicate([1,1,2,2,3,4,4]))
#------------------------------------------------
# Problem 5: Two Sum II (Sorted Array)
# def two_sum(nums,target):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         result = nums[left]+nums[right]
#         if result > target:
#             right -= 1
#         if result < target:
#             left += 1
#         if result == target:
#            return [left,right]
# print(two_sum([2,7,11,15],26))
#-----------------------------------------------
# Problem 6: Count Pairs With Target Sum
# def count_pairs(nums,target):
#     left = 0
#     right = len(nums)-1
#     count = 0
#     while left < right:
#         result = nums[left]+nums[right]
#         if result > target:
#             right -= 1
#         elif result < target:
#             left += 1
#         else:
#             count += 1
#             left += 1
#             right -= 1
#     return count
# print(count_pairs([1,2,3,4,5,6],7))
#------------------------------------------------
# Problem 7: Remove Element
# def remove_element(nums,val):
#     write = 0
#     for read in range(len(nums)):
#         if nums[read] != val:
#             nums[write] = nums[read]
#             write += 1
#     return nums[0:write]
# print(remove_element([3,2,2,3],3))
# print(remove_element([0,1,2,2,3,0,4,2],2))
#-------------------------------------------------
# Problem 8: Merge Two Sorted Arrays
# def merge_lists(num1,num2):
#     result = []
#     i = 0
#     j = 0
#     while len(num1)>i and len(num2)>j:
#         if num1[i]>num2[j]:
#             result.append(num2[j])
#             j+=1
#         else:
#             result.append(num1[i])
#             i+=1
#     while i < len(num1):
#         result.append(num1[i])
#         i+=1
#     while j < len(num2):
#         result.append(num2[j])
#         j+=1
#     return result
# print(merge_lists([1,3,5],[2,4,6]))
# print(merge_lists([1,3,5],[1,2,4]))
#-------------------------------------------------



    
