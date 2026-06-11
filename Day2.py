# Problem 16: Find Missing Number
# def missing_num(num):
#     for i in range(len(num)-1):
#         if num[i]+1 != num[i+1]:
#             return num[i]+1
# print(missing_num([1,2,3,5]))
#---------------------------------
# Problem 17: Move Zeros to End
# def move_zero_end(num):
#     for i in range(len(num)):
#         for j in range(len(num)-1):
#             if num[j] == 0:
#                 temp = num[j]
#                 num[j] = num[j+1]
#                 num[j+1] = temp
#     return num
# print(move_zero_end([1, 0, 2, 0, 3, 0, 4]))
#----------------------------------------------
# Problem 18: Rotate List Right by 1
# def rotate_list_right_one(num):
#     for i in range(len(num)-1,0,-1):
#         temp = num[i]
#         num[i] = num[i-1]
#         num[i-1] = temp
#     return num  
# print(rotate_list_right_one([1,2,3,4,5]))
#----------------------------------------------
# Problem 19: Find Duplicate Numbers
# def duplicate_number(num):
#     seen = []
#     duplicate = []
#     for i in num:
#         if i in seen:
#             duplicate.append(i)
#         else:
#             seen.append(i)
#     return duplicate
# print(duplicate_number([1, 2, 3, 2, 4, 5, 4]))
#------------------------------------------------
# Problem 20: Character Frequency
# def Character_freq(word):
#     seen = {}
#     for i in word:
#         if i in seen:
#             seen[i] += 1
#         else:
#             seen[i] = 1
#     return seen
# print(Character_freq("Banana"))
#------------------------------------------------
# Problem 21: Highest Scoring Student
# students = {
#     "Ram": 85,
#     "John": 92,
#     "Sara": 88
# }
# def highest_scoring(students):
#     max = 0
#     student = ""
#     for key,value in students.items():
#         if value > max:
#             max = value
#             student = key
#     return student
# print(highest_scoring(students))
#-----------------------------------------------
# Problem 22:TODO: Invert Dictionary
# data = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }
# def invert_dict(data):
#     new_data = {}
#     for key,value in data.items():
#         new_data[value] = key
#     return new_data
# print(invert_dict(data))

# Bonus problem
# words = ["cat", "dog", "apple", "bat", "sun", "mango"]
# def word_arrangement(word):
#     result = {}
#     a = []
#     b = []
#     for i in word:
#         if len(i) == 3:
#             a.append(i)
#             result[3] = a
#         else:
#             b.append(i)
#             result[5] = b
#     return result
# print(word_arrangement(words))

# Bonus problem
# words = ["hi", "cat", "apple", "elephant", "sun"]
# def word_arrangement(word):
#     result = {}
#     for i in word:
#         if len(i) not in result:
#             result[len(i)] = [i]
#         else:
#             result[len(i)].append(i)
#     return result
# print(word_arrangement(words))

# Bonus problem:
# students = [
#     ("John", "Python"),
#     ("Sara", "Java"),
#     ("John", "DSA"),
#     ("Mike", "Python"),
#     ("Sara", "DSA"),
#     ("John", "AI"),
# ]
# def course(s):
#     dictionary = {}
#     for i in s:
#         if i[0] not in dictionary:
#             dictionary[i[0]] = [i[1]]
#         else:
#             dictionary[i[0]].append(i[1])
#     return dictionary
# print(course(students))

# Bonus problem:
# student = {
#     "John": ["Python", "DSA", "AI"],
#     "Sara": ["Java", "DSA"],
#     "Mike": ["Python"]
# }
# def count_courses(s):
#     result = {}
#     for key,value in s.items():
#         if key not in result:
#             result[key] = len(value)
#     return result
# print(count_courses(student))

# Bonus problem:
# student = {
#     "John": ["Python", "DSA", "AI"],
#     "Sara": ["Java", "DSA"],
#     "Mike": ["Python"]
# }
# def more_course_registered(s):
#     max = 0
#     string = ""
#     for key,value in s.items():
#         if len(value) > max:
#             max = len(value)
#             string = key
#     return string
# print(more_course_registered(student))
#-----------------------------------------------------
# Problem 23: Merge Student Marks
# d1 = {
#     "John": 85,
#     "Sara": 90
# }
# d2 = {
#     "Mike": 88,
#     "David": 92
# }
# def merge_dict(d1,d2):
#     d3 = {}
#     for key,value in d1.items():
#         d3[key] = value
#     for key,value in d2.items():
#         d3[key] = value
#     return d3
# print(merge_dict(d1,d2))
#-------------------------------------------
# Problem 24: Unique Words
# sentence = "apple banana apple mango banana"
# def unique(s):
#     seen = []
#     a = s.split()
#     for w in a:
#         if w not in seen:
#             seen.append(w)
#     return seen
# print(unique(sentence))
#-------------------------------------------
# Problem 25: Common Students
# math = {"Ram", "John", "Sara"}
# science = {"John", "Sara", "Mike"}
# def common_stu(m, s):
#     return math.intersection(science)
# print(common_stu(math,science))
#-------------------------------------------
# Problem 26: Students in Only One Subject
# math = {"Ram", "John", "Sara"}
# science = {"John", "Sara", "Mike"}
# def only_one(m, s):
#     a, b = m.difference(s), s.difference(m)
#     return b.union(a)              # Same as symmetric_difference()
# print(only_one(math,science))
#-------------------------------------------
# Problem 27: Count Vowels
# def count_vowel(word):
#     vowels = "AEIOUaeiou"
#     count = 0
#     for ch in word:
#         if ch in vowels:
#             count += 1
#     return count
# print(count_vowel("programming"))
#-------------------------------------------
# Problem 28: Palindrome Checker
# def palindrome(string):
#     og = string
#     rev = ""
#     for i in range(len(string)-1,-1,-1):
#         rev += string[i]
#     if rev == og:
#         return True
#     return False
# print(palindrome("madam"))
#-------------------------------------------
# Problem 29: Anagram Checker
# def anagram_checker(w1, w2):
#     freq1 = {}
#     freq2 = {}
#     for ch in w1:
#         if ch not in freq1:
#             freq1[ch] = 1
#         freq1[ch] += 1
#     for ch in w2:
#         if ch not in freq2:
#             freq2[ch] = 1
#         freq2[ch] += 1
#     if freq1 == freq2:
#         return True
#     return False
# print(anagram_checker("listen", "silent"))
# print(anagram_checker("liste", "silent"))
#--------------------------------------------
# Problem 30: Word Counter
# sentence = "I love python and python loves me"
# def word_counter(s):
#     a = s.split()
#     count = 0
#     for i in a:
#         count += 1
#     return count
# print(word_counter(sentence))
#--------------------------------------------