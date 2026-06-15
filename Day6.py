###### Top 20 Revision ######
#1 Move Zeroes to End
# def move_zeroes_end(nums):
#     non_zero = []
#     zero_count = 0
#     for i in nums:
#         if i != 0:
#             non_zero.append(i)
#         else:
#             zero_count += 1
#     zeroes = [0]*zero_count
#     for i in zeroes:
#         non_zero.append(i)
#     return non_zero
# print(move_zeroes_end([1,0,2,0,3,0,4]))
#-----------------------------------------
#2 Rotate List Right by One
# def rotate_list_one(nums):
#     last = nums[len(nums)-1]
#     for i in range(len(nums)-1,-1,-1):
#         nums[i] = nums[i-1]
#     nums[0] = last
#     return nums
# print(rotate_list_one([1,2,3,4,5]))
#-----------------------------------------
#3 Second Most Frequent Character
# def second_max_freq(str):
#     seen = {}
#     for i in str:
#         if i in seen:
#             seen[i] += 1
#         else:
#             seen[i] = 1
#     highest = 0
#     highest_key = ""
#     second_highest = 0
#     second_highest_key = ""
#     for key,freq in seen.items():
#         if freq > highest:
#             second_highest = highest
#             highest = freq
#             second_highest_key = highest_key
#             highest_key = key
#         if highest > freq > second_highest:
#             second_highest = freq
#             second_highest_key = key
#     return second_highest_key
# print(second_max_freq("banana"))
#------------------------------------------------
#4 Valid Anagram
# def valid_anagram(str1,str2):
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
# print(valid_anagram("spot","pots"))    
# print(valid_anagram("spot","stop"))    
# print(valid_anagram("plate","pots"))      
#--------------------------------------------------
#5 Two Sum 
# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                return f"[{i},{j}]"
#     return "no such numbers"        
# print(two_sum([2,7,11,15],9))
# print(two_sum([2,7,11,15],19))
#---------------------------------------------------
#6 Reverse Each Word in a Sentence
# def rev_each_word(sentence):
#     words = sentence.split()
#     new = ""
#     for word in words:
#         for i in range(len(word)-1,-1,-1):
#             new += word[i]
#         new += " "
#     return new
# sentence = "I love python"
# print(rev_each_word(sentence))
#---------------------------------------------------
#7 First Non-Repeating Character
# def first_non_repeat_char(str):
#     seen = {}
#     for i in str:
#         if i in seen:
#             seen[i] += 1
#         else:
#             seen[i] = 1
#     for key, freq in seen.items():
#         if freq == 1:
#            return key
# print(first_non_repeat_char("swiss"))
# print(first_non_repeat_char("qqqirsss"))
#---------------------------------------------------
#8 First Duplicate Character
# def first_duplicate_char(str):
#     seen = {}
#     for i in str:
#         if i in seen:
#            return i
#         else:
#             seen[i] = 1
# print(first_duplicate_char("programming"))
#-------------------------------------------------
#9 Are All Characters Unique? 
# def unique_check(str):
#     seen = {}
#     for i in str:
#         if i not in seen:
#             seen[i] = 1
#         else:
#             return False
#     return True
# print(unique_check("bhanu"))
# print(unique_check("charan"))
#------------------------------------------------
#10 Least Frequent Character
# def Least_freq_char(str):
#     seen = {}
#     for i in str:
#         if i in seen:
#            seen[i] += 1
#         else:
#             seen[i] = 1
#     least = len(str)
#     least_key = ""
#     for key,value in seen.items():
#         if value < least:
#             least = value
#             least_key = key
#     return least_key
# print(Least_freq_char("banana"))
# print(Least_freq_char("aabbccddd"))
#------------------------------------------------
#11 Most frequent word
# def most_freq_word(sentence):
#     words = sentence.split()
#     seen = {}
#     for word in words:
#         if word not in seen:
#             seen[word] = 1
#         else:
#             seen[word] += 1
#     high_freq = 0
#     high_freq_key = ""
#     for key,value in seen.items():
#         if value > high_freq:
#             high_freq = value
#             high_freq_key = key
#     return high_freq_key
# sentence = "apple banana apple mango banana apple"
# print(most_freq_word(sentence))
#---------------------------------------------------
#12 Second most frquent
# def second_max_freq(sentence):
#     words = sentence.split()
#     seen = {}
#     for word in words:
#         if word not in seen:
#             seen[word] = 1
#         else:
#             seen[word] += 1
#     high_freq = 0
#     second_hign_freq = 0
#     high_freq_key = ""
#     second_hign_key = ""
#     for key,value in seen.items():
#         if value > high_freq:
#             second_hign_freq = high_freq
#             high_freq = value
#             second_hign_key = high_freq_key
#             high_freq_key = key
#         elif high_freq > value > second_hign_freq:
#             second_hign_freq = value
#             second_hign_key = key
#     return second_hign_key
# sentence = "apple banana apple mango banana apple"
# print(second_max_freq(sentence))
#-----------------------------------------------------
#13 Majority Element
# def major_element(nums):
#     seen = {}
#     for i in nums:
#         if i not in seen:
#             seen[i] = 1
#         else:
#             seen[i] += 1
#     high_value = 0 
#     high_key = 0
#     for key,value in seen.items():
#         if value > high_value:
#             high_value = value
#             high_key = key
#     return high_key
# print(major_element([3,2,3]))
# print(major_element([2,2,1,1,1,2,2]))
#----------------------------------------------------
#14 Contain duplicate
# def check_duplicate(nums):
#     seen = {}
#     for i in nums:
#         if i not in seen:
#             seen[i] = 1
#         else:
#             return True
#     return False
# print(check_duplicate([1,2,3,1]))
# print(check_duplicate([1,2,3,4]))
#---------------------------------------------------
#15 Intersection of Two Arrays
# def intersection(num1, num2):
#     num1 = set(num1)
#     num2 = set(num2)
#     new = []
#     for i in num1:
#         if i in num2:
#             new.append(i)
#     return new 
# print(intersection([1,2,2,1],[2,2]))
#----------------------------------------------------
#16 count digits in string
# def count_digits(str):
#     count = 0
#     for i in str:
#         if i.isdigit():
#             count += 1
#     return count
# print(count_digits("abc123xyz45"))
#-----------------------------------------------------
#17 Separate letter and digits
# def separate(str):
#     letter = ""
#     digits = ""
#     for i in str:
#         if i.isdigit():
#             digits += i
#         if i.isalpha():
#             letter += i
#     return f"Letters: {letter}\nDigits: {digits}\n"
# print(separate("abc123xyz45"))
#----------------------------------------------------
#18 Count Special Characters
# def count_special_char(str):
#     count = 0
#     for i in str:
#         if not i.isalnum():
#             count += 1
#     return count
# print(count_special_char("Py@Th#On!123"))
#---------------------------------------------------
#19 Remove Digits from a String
# def remove_digit(str):
#     digit = ""
#     new = ""
#     for i in str:
#         if i.isdigit():
#             digit += i
#         else:
#             new += i
#     return new
# print(remove_digit("abc123xyz45"))
#---------------------------------------------------
#20 Remove Special Characters
# def remove_special_char(str):
#     new = ""
#     for i in str:
#         if i.isalnum():
#             new += i
#     return new
# print(remove_special_char("Py@Th#On!123"))
#---------------------------------------------------