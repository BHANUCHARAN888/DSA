# Problem 31: First Non-Repeating Character
# def FirstNonRepeatingChar(string):
#     seen = {}
#     for ch in string:
#         if ch in seen:
#             seen[ch] += 1
#         else:
#             seen[ch] = 1
#     for ch in string:
#         if seen[ch] == 1:
#             return ch
# print(FirstNonRepeatingChar("swiss"))
# print(FirstNonRepeatingChar("aabbcde"))
#------------------------------------------
# Problem 32: Most Frequent Character
# def most_freq_char(string):
#     seen = {}
#     high_repeat = 0
#     char = ""
#     for ch in string:
#         if ch not in seen:
#             seen[ch] = 1
#         else:
#             seen[ch] += 1
#     for key,value in seen.items():
#         if seen[key] > high_repeat:
#             high_repeat = seen[key]
#             char = key
#     return char
# print(most_freq_char("banana"))
#------------------------------------------
# Problem 33: Second Most Frequent Character
# def sec_most_freq_char(string):
#     seen = {}
#     high_repeat = 0
#     sec_high = 0
#     char = ""
#     for ch in string:
#         if ch not in seen:
#             seen[ch] = 1
#         else:
#             seen[ch] += 1
#     for key,value in seen.items():
#         if seen[key] > high_repeat:
#             sec_high = high_repeat
#             high_repeat = seen[key]
#         if high_repeat > seen[key] and seen[key] > sec_high:
#             sec_high = seen[key]
#             char = key
#     return char
# print(sec_most_freq_char("banana"))
# print(sec_most_freq_char("aaabbbcc"))
#----------------------------------------------
# TODO:Problem 34: Character Frequency Sort
# def char_freq_sort(string):
#     seen = {}
#     for ch in string:
#         if ch in seen:
#             seen[ch] += 1
#         else:
#             seen[ch] = 1 
#             # dict created #
#     new_sort = {}
#     while len(seen) > 0:
#           highest_value = 0
#           highest_key = ""

#           for key,value in seen.items():
#               if value > highest_value:
#                   highest_value = value
#                   highest_key = key
#           new_sort[highest_key] = highest_value
#           del seen[highest_key]
#     return new_sort
# print(char_freq_sort("banana"))
#----------------------------------------------
# Problem 35: First Duplicate Character
# def first_duplicate_char(string):
#     seen = {}
#     for ch in string:
#         if ch in seen:
#             return ch
#         else:
#             seen[ch] = 1
# print(first_duplicate_char("programming"))
#----------------------------------------------
# Problem 36: Are All Characters Unique?
# def unique_check(string):
#     seen = {}
#     for ch in string:
#         if ch in seen:
#             seen[ch] += 1
#         else:
#             seen[ch] = 1
#     for key,value in seen.items():
#         if value != 1:
#             return False
#     return True
# print(unique_check("abcdef"))
#----------------------------------------------
# Problem 37: Character With Least Frequency
# def least_freq_char(string):
#     seen = {}
#     least = len(string)
#     char = ""
#     for ch in string:
#         if ch in seen:
#             seen[ch] += 1
#         else:
#             seen[ch] = 1
#     for key,value in seen.items():
#         if seen[key] < least:
#             least = seen[key]
#             char = key
#     return char
# print(least_freq_char("banana"))
#----------------------------------------------
# Problem 38: Count Digits in a String
# def count_digit(string):
#     digits = "1234567890" # we can also use ".isdigit()"
#     count = 0
#     for i in string:
#         if i in digits:
#             count += 1  
#     return count
# print(count_digit("abc123xyz45"))
#----------------------------------------------
# Problem 39: Count Alphabets in a String
# def count_alphabets(string):
#     count = 0
#     for i in string:
#         if i.isalpha():
#             count += 1  
#     return count
# print(count_alphabets("abc123xyz45"))
#----------------------------------------------
# Problem 40:
# def str_operation(string):
#     Letter = ""
#     Digits = ""
#     for i in string:
#         if i.isalpha():
#             Letter += i
#         if i.isdigit():
#             Digits += i
#     return f"Letter: {Letter}\nDigits: {Digits}\n"
# print(str_operation("abc123xyz45"))
#----------------------------------------------