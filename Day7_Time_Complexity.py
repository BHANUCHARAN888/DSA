# ___Time Complexity: It tells how does run-time grow as input size grows?
# --> It measures in Big - O notation
# --> Constant time O(1)
# --> Linear time(single loop) O(n)
# --> Quadratic time(multi loop) O(n^2)
# --> Logarithmic time O(log n) --- Each step cuts search space in half
# --> O(n log n) used for merge and heap sort, better than O(n^2)
#----
# Ignore constants: O(2n) -> O(n)
# Ignore lower order terms: O(n^2 + n) -> O(n^2)
# Nested loops: O(n * n) -> O(n^2)
# Different input variables stays separate: O(n + m)
#-------------------------------------------------------------------------------

# ___PRACTICE PROQBLEMS

# Q1) for i in range(n):
#         print(i)
# Time Complexity: O(n)

# Q2) for i in range(50):
#         print(i)
# Time Complexity: O(1)

# Q3) for i in range(n):
#         for j in range(n):
#             print(i, j)
# Time Complexity: O(n*n) = O(n^2)

# Q4) for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j) 
# Time Complexity: O(n+n) = O(2n) = O(n)

# Q5) for i in range(n):
#         print(i)
#     for j in range(m):
#         print(j) 
# Time Complexity: O(n+m)

# Q6) for i in range(n):
#         print(i)
#     for j in range(100):
#         print(j)
# Time Complexity: O(n+100) = O(n)

# Q7) for i in range(n):
#         for j in range(100):
#             print(i, j)
# Time Complexity: O(n*100) = O(n)

# Q8) for i in range(n):
#         for j in range(m):
# Time Complexity: O(n*m)

# Q9) i = 1
#     while i < n:
#         i = i * 2
# Time Complexity: O(log n)
# ---> i = i + 1 => O(n)
# ---> i = i * 2 => O(log n)
# ---> i = i / 2 => O(log n)

# Q10) for i in range(n):
#          for j in range(n):
#              for k in range(n):
# Time Complexity: O(n^3)
