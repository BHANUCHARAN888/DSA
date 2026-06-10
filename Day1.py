## Problem 1: Sum of Elements
# def Sum_Elements(nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     return sum
# print(Sum_Elements([10,20,30,40,50]))
#----------------------------------------
## Problem 2: Largest Element
# def Largest_Elements(nums):
#     largest = 0
#     for i in nums:
#         if i > largest:
#             largest = i
#     return largest
# print(Largest_Elements([12,45,7,89,23]))
#----------------------------------------
## Problem 3: Smallest Element
# def Smallest_Elements(nums):
#     Smallest = nums[0]
#     for i in nums:
#         if i < Smallest:
#             Smallest = i
#     return Smallest
# print(Smallest_Elements([12,45,7,89,23]))
#----------------------------------------
## Problem 4: Count Even Numbers
# def Even_Num(nums):
#     count = 0
#     for i in nums:
#         if i % 2 == 0:
#             count += 1
#     return count
# print(Even_Num([1, 2, 3, 4, 5, 6, 7, 8]))
#----------------------------------------
## Problem 5: Reverse a List
# def Reverse_List(nums):
#     rev = []
#     for i in range(len(nums)-1,-1,-1):
#         rev.append(nums[i])
#     return rev
# print(Reverse_List([1, 2, 3, 4, 5]))
#----------------------------------------
## Problem 6: Find Second Largest
# def SecondLargest(nums):
#     L = nums[0]
#     SL = nums[0]
#     for i in nums:
#         if i > L:
#             SL = L
#             L = i
#         if i > SL and i != L:
#             SL = i
#     return SL
# print(SecondLargest([10, 20, 4, 45, 99]))
#-------------------------------------------
## Problem 7: Remove Duplicates
# def R_Duplicate(nums):
#     new = []
#     for i in nums:
#         if i not in new:
#             new.append(i)
#     return new
# print(R_Duplicate([1, 2, 2, 3, 4, 4, 5]))
#--------------------------------------------
## Problem 8: Count Occurrences
# def CountOccur(nums, target):
#     count = 0
#     for i in nums:
#         if i == target:
#             count += 1
#     return count
# print(CountOccur([1, 2, 3, 2, 4, 2, 5],2))
#--------------------------------------------
## Problem 9: Search an Element
# def SearchElement(nums, target):
#     for i in nums:
#         if i == target:
#             return "Found"
#     return "Not Found"
# print(SearchElement([10, 20, 30, 40, 50],30))
#----------------------------------------------
## Problem 10: Merge Two Lists
# def Merge(a,b):
#     new = a.copy()
#     for i in b:
#         new.append(i)
#     return new
# print(Merge([1, 2, 3],[4, 5, 6])) 
#----------------------------------------------
# Problem 11: Find All Odd Numbers
# def OddNumbers(num):
#     new = []
#     for i in num:
#         if i % 2 != 0:
#             new.append(i)
#     return new
# print(OddNumbers([1,2,3,4,5,6,7]))
#----------------------------------------------
# Problem 12: Positive Numbers Only
# def PositiveNumbers(num):
#     new = []
#     for i in num:
#         if i >= 0:
#             new.append(i)
#     return new
# print(PositiveNumbers([-2,5,-1,8,0]))
#----------------------------------------------
# Problem 13: Difference Between Largest and Smallest
# def Diff_L_S(num):
#     largest = num[0]
#     smallest = num[0]
#     for i in num:
#         if i > largest:
#             largest = i
#         if i < smallest:
#             smallest = i
#     return largest - smallest
# print(Diff_L_S([10,4,20,7]))
#----------------------------------------------
# Problem 14: Check Sorted List
# def Sorted_list(num):
#     for i in range(len(num)-1):
#         if num[i] > num[i+1]:
#             return "Not Sorted"
#     return "Sorted"
# print(Sorted_list([1, 2, 3, 4, 5]))
# print(Sorted_list([1, 5, 2, 4]))
#----------------------------------------------
# Problem 15: Find Common Elements
# def CommonElements(a,b):
#     a = set(a)
#     b = set(b)
#     return list(a.intersection(b))
# print(CommonElements([1, 2, 3, 4, 5],[4, 5, 6, 7]))
#------------------------------------------------------