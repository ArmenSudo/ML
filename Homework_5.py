# # __ 1 __ findDisappearedNumbers
#
# nums = [4,3,2,7,8,2,3,1]
# set_1 = set()
# set_2 = set()
# for x in range(len(nums)):
#     set_1.add(x+1)
# for x in nums:
#     set_2.add(x)
# print(list(set_1 - set_2))


# # __ 2 __ findWords
# words = ["Hello", "Alaska", "Dad", "Peace"]
# first_row = "qwertyuiop"
# second_row = "asdfghjkl"
# third_row = "zxcvbnm"
#
# new_words = []
# for x in words:
#     first, second, third = True, True, True
#     for y in x.lower():
#         if y in first_row and first:
#             second, third = False, False
#         elif y in second_row and second:
#             first, third = False, False
#         elif y in third_row and third:
#             second, first = False, False
#         else:
#             break
#     else:
#         new_words.append(x)
# print(new_words)


# # __ 3 __ transpose
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# i = 0
# dic = {}
# lis = []
# for i, value1 in enumerate(matrix):
#     for j, value2 in enumerate(value1):
#         if dic.get(j):
#             dic[j].append(value2)
#         else:
#             dic[j] = [value2]
# for key, value in dic.items():
#     lis.append(value)
# print(lis)

# # __ 4 __
#
# mat = [[1, 2], [3, 4]]
#
#
# def res(r, c):
#     new_mat = []
#     result = []
#     for x in mat:
#         for y in x:
#             new_mat.append(y)
#     if r * c != len(new_mat):
#         return mat
#
#     i = 0
#     for x in range(r):
#         lst = []
#         for y in range(c):
#             lst.append(new_mat[i])
#             i += 1
#         result.append(lst)
#     return result
#
#
# print(res(r=2, c=4))

# # __ 5 __
# board1 = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
#
#
# def countBattleships(board):
#     total = 0
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 'X':
#                 total += 1
#                 if i < len(board) - 1:
#                     if board[i + 1][j] == 'X':
#                         total -= 1
#                 if j < len(board[0]) - 1:
#                     if board[i][j + 1] == 'X':
#                         total -= 1
#     return total
#
#
# print(countBattleships(board1))
