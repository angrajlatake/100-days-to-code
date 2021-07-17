def busyman(list, activities):
    list.sort(key=lambda x: x[1])
    count = 0
    time = 0
    print(list)

    for activity in list:
        if activity[0] >= time:
            time = activity[1]
            count += 1

    return count


    # while i < activities:
    #     while j < activities:
    #         if list[i][1] <= list[j][0]:
    #             count += 1
    #         j += 1
    #     i += 1
    # return count

list = []

num_of_activities = int(input())
for i in range(num_of_activities):
    start, end = map(int, input().split())
    list.append((start, end))

print(busyman(list, num_of_activities))
