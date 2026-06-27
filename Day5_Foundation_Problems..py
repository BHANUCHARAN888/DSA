# Problem 51: Longest Unique Word
# def longest_unique_word(sentence):
#     words = sentence.split()
#     answer = ""
#     longest = 0
#     for word in words:
#         if len(word)>longest:
#            longest = len(word)
#            answer = word
#     return answer
# sentence = "I love python pythonic programming"
# print(longest_unique_word(sentence))
#----------------------------------------------------
# Problem 52: Count Unique Words
# sentence = "apple banana apple mango banana orange"
# def count_unique_word(sentence):
#     words = sentence.split()
#     seen = {}
#     count = 0
#     for word in words:
#         if word in seen:
#             seen[word] += 1
#         else:
#             seen[word] = 1
#     for word in seen:
#         if seen[word] == 1:
#             count += 1
#     return count
# print(count_unique_word(sentence))
#--------------------------------------------------
# Problem 53: First Repeating Word
# sentence = "apple banana mango apple orange"
# def first_repeat_word(sentence):
#     words = sentence.split()
#     seen = {}
#     for word in words:
#         if word in seen:
#             seen[word] += 1
#             break
#         else:
#             seen[word] = 1
#     return word
# print(first_repeat_word(sentence))
#-----------------------------------------------------
# Problem 54: Word With Highest Frequency
# sentence = "apple banana apple mango banana apple"
# def highest_freq(sentence):
#     words = sentence.split()
#     seen = {}
#     highest = 0
#     highest_w = ""
#     for word in words:
#         if word in seen:
#             seen[word] += 1
#         else:
#             seen[word] = 1
#         if seen[word] > highest:
#             highest = seen[word]
#             highest_w = word
#     return highest_w
# print(highest_freq(sentence))
#-------------------------------------------------------------------
# Problem 55: Second Most Frequent Word
# sentence = "apple banana apple mango banana apple orange banana"
# def highest_freq(sentence):
#     words = sentence.split()
#     seen = {}
#     highest = 0
#     highest_w = ""
#     second_highest = 0
#     second_highest_w = ""
#     for word in words:
#         if word in seen:
#             seen[word] += 1
#         else:
#             seen[word] = 1
#     for w,freq in seen.items():
#         if freq > highest:
#             second_highest = highest
#             second_highest_w = highest_w
#             highest = freq
#             highest_w = w
#         elif highest > freq > second_highest:
#             second_highest = freq
#             second_highest_w = w
#     return second_highest_w
# print(highest_freq(sentence))
#--------------------------------------------------------------------
# Problem 56: Two Sum
# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i]+nums[j] == target:
#                 return f"[{i},{j}]"
#     return "no such numbers"
# print(two_sum([2, 7, 11, 15],26))
#---------------------------------------------------------------------
# Problem 57:
# def check_list(nums):
#     seen = {}
#     for i in nums:
#         if i not in seen:
#            seen[i] = 1
#         else:
#             seen[i] += 1
#             return True
#     return False
# print(check_list([1,2,3,4])) 
# print(check_list([1,2,3,1])) 
#---------------------------------------------------------------------
# Problem 58: Valid Anagram
# def anagram(str1, str2):
#     freq1 = {}
#     freq2 = {}
#     for i in str1:
#         if i in freq1:
#             freq1[i] += 1
#         else:
#             freq1[i] = 1
#     for i in str2:
#         if i in freq2:
#             freq2[i] += 1
#         else:
#             freq2[i] = 1
#     if freq1 == freq2:
#         return True
#     return False
# print(anagram("listen","silent"))
# print(anagram("evil","live"))
# print(anagram("helo","hello"))
#---------------------------------------------------------------------
# Problem 59: Intersection of two arrays
# def Intersection(num1,num2):
#     num1 = set(num1)
#     num2 = set(num2)
#     num3 = []
#     for i in num1:
#         if i in num2:
#             num3.append(i)
#     return num3
# print(Intersection([1,2,2,1],[2,2]))
#-----------------------------------------------------------------
# problem 60: Majority Element
# def most_repeated(nums):
#     seen = {}
#     highest = 0
#     highest_key = 0
#     for i in nums:
#         if i in seen:
#             seen[i] += 1
#         else:
#             seen[i] = 1
#     for key,value in seen.items():
#         if value > highest:
#             highest = value
#             highest_key = key
#     return highest_key
# print(most_repeated([3,2,3]))
#------------------------------------------------------------------

 




    
