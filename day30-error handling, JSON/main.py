# fruits = ["Apple", "Pear", "Orange"]
#
#
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
# try:
#     make_pie(2)
# except IndexError:
#     print("Fruit pie")


#------------------------------------------------------#

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']

    except KeyError:
        pass

print(total_likes)


