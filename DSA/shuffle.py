s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
list = []

for i in s:
    list.append(i)

new_list = []
for i in indices:
    new_list[indices[i]] = list [i]

print(new_list)