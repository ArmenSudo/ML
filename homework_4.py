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
