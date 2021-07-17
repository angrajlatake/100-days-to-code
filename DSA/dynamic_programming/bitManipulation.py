
# i = 0
# while (i < (1 << 4)):
#
#     seq = []
#     x = 8
#     while x >= 0:
#         if (i & (1 << x)) > 0:
#             seq.append(1)
#         else:
#             seq.append(0)
#         x += -1
#     i += 1
#     print(seq)


list = [1,2,3,4,5,6,5,4,3,2,1,1,1,6,4]

ans = 0

print (5^5)
for num in list:
    ans ^= num

print(ans)


