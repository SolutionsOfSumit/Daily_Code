#https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=false

# def Valid(n):
#     s = n[:]
#     n = n.split("-")
#     n="".join(n)
#     n = int(n)
#     v = "Invalid"

#     if n[0] == 4 or 5 or 6:
#         if len(n) == 16:
#             if len(s) == 3:
#                 for i in range(len(s) + 1):
#                     if len(s[i]) != 4:
#                         break
#                 else:
#                     v = "Valid"


#     print(v)
list1 = input()
list1 = list1.split("\n")
print(list1)

# for n in range(list1):
#     v = "Invalid"

#     n = "5122-2368-7954-3214"
#     n = n.split("-")
#     s = n[:]
#     n="".join(n)
#     l = len(n)
#     n = int(n) 

#     if s[0][0] == 4 or 5 or 6:
#         if l == 16:
#             if len(s) == 4:
#                 for i in range(len(s)):
#                     if len(s[i]) != 4:
#                         break
#                 else:
#                     v = "Valid"
#     print(v)