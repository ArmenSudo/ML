# # Palindrome numbers
#
# a = int(input())
# b = int(input())
# for x in range(a, b + 1):
#     if str(x) == str(x)[::-1]:
#         print(x, end=' ')
#
# # Tree
#
# n = int(input())
#
# c = 1
# for x in range(n // 2, -1, -1):
#     print(' ' * x, end='')
#     print('*' * c)
#     c += 2
#
# # Suffix Sums
#
# a = list(map(float, (input().split(" "))))
# b = []
# for x in range(len(a)):
#     b.append(sum(a[x:]))
# print(b)
#
#
# # Cyclic shift
#
# def new(arr, step):
#     arri = []
#     if not step % len(arr):
#         return arr
#     if step > len(arr):
#         step = step % len(arr)
#     arri.extend(arr[-step::])
#     arri.extend(arr[:-step])
#     return arri
#
#
# count = int(input())
# step1 = int(input())
# a = [int(input()) for _ in range(count)]
# print(new(a, step1))
#
#
#
# import math
#
#
# def check_prime(a):
#     if a == 1:
#         return False
#     b = round(math.sqrt(a))
#     for i in range(2, b + 1):
#         if a % i == 0:
#             return False
#     else:
#         return True
#
#
# def goldbach_conjecture(numb):
#     for i in range(2, numb // 2 + 1):
#         if check_prime(i) and check_prime(numb - i):
#             return i, numb - i
#
#
# number = int(input())
# print(goldbach_conjecture(number))
