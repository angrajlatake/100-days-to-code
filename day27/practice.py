def add(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum



print(add(4,5,6,7,8,9))

def calculate(**kwargs):
