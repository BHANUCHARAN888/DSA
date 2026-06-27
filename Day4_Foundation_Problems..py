# # Problem 41: Longest Word
# def longest_word(sentence):
#     words = sentence.split()
#     longest = 0
#     longest_w = ""
#     for w in words:
#         if len(w) > longest:
#             longest = len(w)
#             longest_w = w
#     return longest_w
# sentence = "I love solving python problems"
# print(longest_word(sentence))
#--------------------------------------------
# Problem 42: Shortest Word
# def shortest_word(sentence):
#     words = sentence.split()
#     shortest = len(words[0])
#     shortest_w = words[0]
#     for w in words:
#         if len(w) < shortest:
#             shortest = len(w)
#             shortest_w = w
#     return shortest_w
# sentence = "I love solving python problems"
# print(shortest_word(sentence))
#--------------------------------------------
# Problem 43: Count Words in a Sentence
# def count_words(sentence):
#     words = sentence.split()
#     count = 0
#     for w in words:
#         count += 1
#     return count
# sentence = "I love solving python problems"
# print(count_words(sentence))
#---------------------------------------------
# Problem 44: Reverse Each Word
# def rev_Sentence(sentence):
#     words = sentence.split()
#     new_sentense = ""
#     for w in words:
#         for i in range(len(w)-1, -1, -1):
#             new_sentense += w[i]
#         new_sentense += " "
#     return new_sentense
# sentence = "I love python"
# print(rev_Sentence(sentence))
#--------------------------------------------
# Problem 45: Capitalize First Letter of Each Word
# def capitalizer(sentence):
#     words = sentence.split()
#     new_sentence = ""
#     for w in words:
#         word = w[0].upper() + w[1:]
#         new_sentence += word
#         new_sentence += " "
#     return new_sentence
# sentence = "i love python"
# print(capitalizer(sentence))
#-----------------------------------------------
# Problem 46: Count Uppercase Letters
# def count_uppercase(string):
#     count = 0
#     for ch in string:
#         if ch.isupper():
#             count += 1
#     return count
# print(count_uppercase("PyThOn123"))
#-----------------------------------------------
# Problem 47: Count Lowercase Letters
# def count_lowercase(string):
#     count = 0
#     for ch in string:
#         if ch.islower():
#             count += 1
#     return count
# print(count_lowercase("PyThOn123"))
#----------------------------------------
# Problem 48: Count Special Characters
# def count_special_char(string):
#     count = 0
#     for i in string:
#         if not i.isalnum():
#             count += 1
#     return count
# print(count_special_char("Py@Th#On!123"))
#-------------------------------------------
# Problem 49: Remove Digits From String
# def remove_digits(string):
#     letter = ""
#     for i in string:
#         if i.isalpha():
#             letter += i
#     return letter
# print(remove_digits("abc123xyz45"))
#------------------------------------
# Problem 50: Remove Special Characters
# def remove_special_char(str):
#     new_str = ""
#     for i in str:
#         if i.isalnum():
#             new_str += i
#     return new_str
# print(remove_special_char("Py@Th#On!123"))
#-------------------------------------------