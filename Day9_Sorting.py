# ___Sorting___

## Bubble sorting
#
# [5*,4,1,2,3]
# 5---4 swap 4---5
# [4,5*,1,2,3]
# 5---1 swap 1---5
# [4,1,5*,2,3]
# 5---2 swap 2---5
# [4,1,2,5*,3]
# 5---3 swap 3---5
# [4,1,2,3,5*]
# def bubble(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 print("-------------")
#                 print(arr)
#                 print(arr[j])
#                 print(arr[j+1])
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#     return arr
# print(bubble([5,4,1,2,3]))
#-----------------------------------------------
# Retension check:
# def bubble_sort(arr):
#     n = len(arr) 
#     for i in range(n):
#         swapped = False
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j] 
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp 
#                 swapped = True
#         if not swapped:
#             break
#     return arr
# print(bubble_sort([1,2,3,4,5,6]))
#-----------------------------------------------

# Selection sorting
# def selection(arr):
#     n = len(arr)
#     for i in range(n):
#         min = i
#         for j in range(i+1, n):
#             if arr[min] > arr[j]:
#                 min = j
#         arr[i], arr[min] = arr[min], arr[i]
#     return arr
# print(selection([13,46,24,52,20,9]))
#------------------------------------------------



