# __ 1 __ # Unique Email Addresses
#
# emails = eval(input())
# n_emails = set()
# for email_name in emails:
#     n = (email_name.find('@'))
#     print(n)
#     string = ''
#     for x in email_name:
#         if x == '+' or x == '@':
#             string += email_name[n:]
#             break
#         if x == '.':
#             continue
#         else:
#             string += x
#     n_emails.add(string)
# print(len(n_emails))
# #########################################################################################################
# __ 2 __ # Jewels and Stones
#
# jewels = input()
# stones = input()
# count = 0
# for x in jewels:
#     count += stones.count(x)
# print(count)
# #########################################################################################################
# __ 3 __ # String power
#
# string = input()
# number = int(input())
#
# if number >= 0:
#     print(string * number)
#
# if number <= 0:
#     if len(string) % -number == 0 and string[0:len(string)//-number] * -number == string:
#         print(string[0:len(string)//-number])
#     else:
#         print('Undefined')
# #########################################################################################################
# __ 4 __ # Beautiful Binary String
# def beautifulBinaryString(b):
#     count = 0
#     while '010' in b:
#         count += 1
#         b = b.replace('010', '011', 1)
#     return count
#
#
# length = int(input())
# binary = input()
# print(beautifulBinaryString(binary))
# #########################################################################################################
#  __ 5 __ # findAndReplacePattern
# words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
# pattern = "abb"
#
# output = []
# for word in words:
#     dic = {}
#     rev_dic = {}
#     if len(word) != len(pattern):
#         continue
#     flag = True
#     for i, x in enumerate(word):
#         if not dic.get(x):
#             dic[x] = pattern[i]
#         elif dic[x] != pattern[i]:
#             flag = False
#         if not rev_dic.get(pattern[i]):
#             rev_dic[pattern[i]] = x
#         elif rev_dic[pattern[i]] != x:
#             flag = False
#     if flag:
#         output.append(word)
# print(output)
# #########################################################################################################
#  __ 6 __ # findingUsersActiveMinutes
# logs = [[1, 1], [2, 2], [2, 3]]
# k = 4
# logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
# k = 5
# logs = [[305589003, 4136], [305589004, 4139], [305589004, 4141], [305589004, 4137], [305589001, 4139],
#         [305589001, 4139]]
# k = 6
# output = []
# dic1 = {}
# for _ in range(k):
#     output.append(0)
# for x in logs:
#     if not dic1.get(x[0]):
#         dic1[x[0]] = [x[1]]
#     else:
#         if not x[1] in dic1[x[0]]:
#             dic1[x[0]].append(x[1])
# for key, value in dic1.items():
#     output[len(value) - 1] += 1
# print(output)
