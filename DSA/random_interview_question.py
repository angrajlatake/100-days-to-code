# # def print_star(n):
# #     star = "*"
# #     for i in range(n):
# #         print(star)
# #         star+="*"
# #
# # print_star(10)
#
# #
# # x = int(input("x = "))
# # y = int(input("y = "))
# # z = int(input("z = "))
# # n = int(input("n = "))
# #
# # list = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) ]
# #
# # for n in list:
# #     print(n)
#
# #
# # def factorial(n):
# #     if n==0:
# #         return 1
# #     else:
# #         return n*factorial(n-1)
# #
# #
# # print(factorial(4))
# #
# # def modulo(x,y):
# #     if x < y :
# #         return x
# #
# #     else:
# #         return modulo(x-y , y)
# #
# #
# # print(modulo(27, 4))
#
# # indirect recursion
# # def odd(n):
# #     if n <= 10:
# #         print(f"{n+1} ")
# #         n+=1
# #         even(n)
# #
# # def even(n):
# #     if n <= 10:
# #         print(f"{n-1} ")
# #         n+=1
# #         odd(n)
# #
# #
# # odd(1)
#
# # def prime(n):
# #     for i in range(2,n):
# #         if n % i == 0:
# #             return False
# #         else:
# #             return True
# #
# # numb = int(input("enter a number:"))
# #
# # for n in range(2,numb+1):
# #     if prime(n):
# #         print(n)

# new_list = []
# list = [[a,b,c] for a in range(4) for b in range(4) for c in range(4)]
# print(list)
# for n in list:
#     if 1 in n and 2 in n and 3 in n:
#         new_list.append(n)
#
# print(new_list)
#
# #
# # def binary_search(list, number):
# #     first = 0
# #     last = len(list) - 1
# #
# #     while first <= last:
# #         midpoint = (first+last)//2
# #         if list[midpoint] == number:
# #             return midpoint
# #         elif list[midpoint] < number:
# #             first = midpoint+1
# #         else:
# #             last = midpoint - 1
# #     return -1
# #
# # def recursive_binary_search(list, number):
# #     pass
# # arr = [1,2,3,4,5,6,7,8,9,10,11]
# #
# #
# # from typing import List
# #
# #
# # def countN(list: List[int]) -> int:
# #     count = 0
# #     first = 0
# #     last = len(list) - 1
# #     while first <= last:
# #         mid = (first + last) // 2
# #         if list[mid] < 0:
# #             count += last - mid + 1
# #             last = mid - 1
# #
# #
# #         else:
# #             first = mid + 1
# #     print(list)
# #     print(count)
# #     return count
# #
# #
# # def countNegatives(grid: List[List[int]]) -> int:
# #     count = 0
# #     for i in grid:
# #         count += countN(i)
# #     return count
# #
# # grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# #
# # countNegatives(grid)
# #
#
# def weakest_mat(list):
#     m = []
#     count = 0
#     for i in list:
#         for j in i:
#             for l in j:
#                 if l == 1:
#                     count+=1
#             m.append(count)
#             count = 0
#     print(return_index_list(m))
#     return m
#
# def return_index_list(list):
#     dict = {}
#     k = 0
#     for i in list:
#         dict[k] = i
#         k+=1
#     print(dict)
#     return {k:v for k,v in sorted(dict.items(),key=lambda item:item[1])}
#
#
#
#
#
# mat = [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
#
# print(weakest_mat(mat))
#

# list = [1,2,3]
# i = 0
# j = i+1
# count = 0
# proxy = [0]*101
# for numb in list:
#     count += proxy[numb]
#     proxy[numb]+=1
#     # while j < len(list):
#     #     if list[i] == list[j]:
#     #         count+=1
#     #         j+=1
#     #     else:
#     #         j+=1
#     # i+=1
#     # j = i+1

# def numJewelsInStones(jewels: str, stones: str):
#     count = 0
#     for jewel in jewels:
#         for stone in stones:
#
#             if jewel == stone:
#                 count += 1
#
#     return count
#
#
# jewels = "aA"
# stones = "aAAbbbb"
#
# print(numJewelsInStones(jewels,stones))
#
# def sum(i,list):
#     if i ==0:
#         return list[0]
#     return sum(i-1,list) + list[i]
#
#
#
# arr = [1,2,3,4,5,6,7,8,9]
#
#
# print(sum(6,arr))
#
# def solution(n, dp):
#     if n == 1:
#         print("returning 1")
#         return 1
#     # elif n == 2:
#     #     print("returning 2")
#     #     return 2
#
#     if n in dp.keys():
#
#         return dp[n]
#
#     max_value = n
#
#     for i in range(1,n):
#         max_value = max(max_value, i * solution(n-i, dp))
#
#     dp[n] = max_value
#     return max_value
#
# dp = {}
# print(solution(10, dp))

# def eko(required,height,list):
# total = 0
# for i in list:
#     total += i
#
# x = (total - n)//m
#
# flag = False
# for i in list:
#     if x > i :
#         flag = True
#         list.remove(i)
#         m -= 1
#
# if flag:
#     return eko(m, n, list)
#
#


def is_true(required, height, trees):
    count = 0

    for tree in trees:
        if tree > height:
            count += (tree - height)
    if count >= required:
        return True

    return False


def binary_search(l, r, trees, required):

    while (l+1 < r):
        mid = (l+r)// 2
        # print (l, r)
        if is_true(required, mid, trees):
            l = mid
        else:
            r = mid-1

    # l , l+1
    if is_true(required, l+1, trees):
       return l+1

    return l

def eko(required, trees):

    l = 0
    r = max(trees)

    return int (binary_search(l, r, trees, required))


# def eko(num_trees, required, trees):
#     count = 0
#     maxnumb = 0
#
#     for i in list:
#         if i > maxnumb:
#             maxnumb = i
#         count += (i - height)





num_trees, required = map(int, input().split())
trees = list(map(int, input().split()))

print(eko(required, trees))

