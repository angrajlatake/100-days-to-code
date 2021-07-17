#
# def split(list):
#     mid = len(list)//2
#     left_list = list[:mid]
#     right_list = list[mid:]
#     return left_list, right_list
#
#
# def merge(left,right):
#     i = 0
#     j = 0
#     l = []
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             l.append(left[i])
#             i+=1
#         else:
#             l.append(right[j])
#             j+=1
#
#     while i <len(left):
#         l.append(left[i])
#         i+=1
#
#     while j < len(right):
#         l.append(right[j])
#         j+=1
#
#     return l
#
# def merge_sort(list):
#
#     """returns a sorted list
#     devide : devides a list from a midpoint
#     conquor : sorts the brokendown list
#     merge : the lists and sorts them while merging"""
#     if len(list) <=1:
#         return list
#     else:
#         left,right = split(list)
#         left_half = merge_sort(left)
#         right_half = merge_sort(right)
#         return merge(left_half,right_half)
#
# arr = [34,65,61,76,23,73,45,11,90,87,54,32]
#
# print(merge_sort(arr))
import random


def merge_sort(list):
    if len(list) <= 1:
        return list

    left, right = split(list)
    lefthalf = merge_sort(left)
    righthalf = merge_sort(right)
    return merge(lefthalf, righthalf)

def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    i = 0
    j = 0
    l =[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l


list = []

for i in range(10):
    numb = random.randint(0,100)
    list.append(numb)

print(list)
print(f"sorted list : {merge_sort(list)}")
