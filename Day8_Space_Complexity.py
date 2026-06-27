# ___Space Complexity: how much extra memory is used?
# --> O(1) fixed memory
# --> O(n) extra array grows with input size

# Complexity n -> 2n
# O(1)       same
# O(log n)   slightly big
# O(n)       2x
# O(n^2)     4x
# O(n^3)     8x
#-----------------------------------------------------

# Example 1: O(1) space
# def find_max(arr):
#     max_num = arr[0]
#     for num in arr:
#         if num > max_num:
#             max_num = num
#     return max_num

# if array contains 1, 1000 or 1M it does not matter just stores in one variable not extra space generating

# Example 2: O(n) space 
# def copy_array(arr):
#     result = []
#     for num in arr:
#         result.append(num)
#     return result
