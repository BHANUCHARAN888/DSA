# ---SLIDING WINDOW---
# Problem 1: Maximum Sum Subarray of Size K 
# def max_sum_subarray(nums, k):
#     left = 0
#     right = k-1
#     window_sum = sum(nums[:k])
#     # print(window_sum)
#     max_sum = window_sum
#     # print(max_sum)
#     while right < len(nums):
#         right = right + 1
#         if right >= len(nums):
#             break
#         window_sum = window_sum - nums[left] + nums[right]
#         max_sum = max(max_sum, window_sum)
#         left = left + 1
#     return max_sum
# print(max_sum_subarray([2,1,5,1,3,2],2))
#----------------------------------------------------------------
# Problem 2: Average of All Subarrays of Size K
# def avg_sum_subarray(nums,k):
#     left = 0
#     right = k-1
#     sum_subarray = sum(nums[:k])
#     window_avg = sum(nums[:k])/k
#     result = []
#     while right < len(nums):
#         right += 1
#         result.append(window_avg)
#         if right >= len(nums):
#             break
#         sum_subarray = sum_subarray-nums[left]+nums[right]
#         window_avg = sum_subarray/k
#         left = left + 1
#     return result
# print(avg_sum_subarray([1,3,2,6,-1,4,1,8,2],5))
#----------------------------------------------------------------
# Problem 3: Maximum Number of Vowels in a Substring of Size K
# def max_vowel_subarray(s,k):
#     left = 0
#     right = k
#     max_count = 0
#     vowels = "aeiou"
#     window_subarray = s[left:right]
#     count = 0
#     for ch in window_subarray:
#         if ch in vowels:
#            count += 1
#     while right < len(s):
#         max_count = max(max_count, count)
#         if s[left] in vowels:
#             count -= 1
#         if s[right] in vowels:
#             count += 1
#         left += 1
#         right += 1
#     return max_count
# print(max_vowel_subarray("abciiidef",3))
#--------------------------------------------------
# retension check:
# def max_vowel_subarray(s,k):
#     window_subarray = s[:k]
#     count = 0
#     vowels = "aeiou"
#     for i in window_subarray:
#         if i in vowels:
#             count += 1
#     left = 0
#     right = k
#     max_count = count
#     while right < len(s):
#         if s[left] in vowels:
#             count -= 1
#         if s[right] in vowels:
#             count += 1
#         max_count = max(max_count,count)
#         left += 1
#         right += 1
#     return max_count
# print(max_vowel_subarray("abciiidef",3))
#----------------------------------------------------
# (643) LEETCODE-MAXIMUM AVERAGE SUBARRAY 1
# Problem 4:
# def max_avg_subarray(nums,k):
#     left = 0
#     right = k-1
#     sum_window_nums = sum(nums[:k])
#     max_sum = sum_window_nums
#     while right+1 < len(nums):
#         max_sum = max(max_sum, sum_window_nums)
#         right += 1
#         sum_window_nums = sum_window_nums - nums[left] + nums[right]
#         left += 1
#     return max_sum/k
# print(max_avg_subarray([1,12,-5,-6,50,3],4))
#-----------------------------------------------------
# (1456)
# Problem 5: Find Maximum Number of Occurrences of a Digit in Any Window of Size K
# def max_occur(nums,target,k):
#     left = 0
#     right = k-1
#     window = nums[:k]
#     count = 0
#     for i in window:
#         if i == target:
#             count += 1
#     max_count = count
#     while right+1 < len(nums):
#         max_count = max(max_count,count)
#         right += 1
#         if nums[left] == target:
#             count -= 1
#         if nums[right] == target:
#             count += 1
#         left += 1
#     return max_count
# print(max_occur([1,2,1,1,3,1,4],1,3))
#----------------------------------------------------