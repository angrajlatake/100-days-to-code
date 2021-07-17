arrey = [1,2,3,-100,10,2]


def max_sum_sub_arrey(n ,list):
    if n == 0:
        return list[n]
    return max(max_sum_sub_arrey(n-1,list)+list[n], list[n])

print(max_sum_sub_arrey(len(arrey)-1, arrey))

