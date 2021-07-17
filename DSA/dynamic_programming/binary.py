def findBinary(x, seq):
    if x == 0:
        print(seq)
        return

    seq.append(0)
    findBinary(x-1,seq)
    seq.pop(len(seq)-1)

    seq.append(1)
    findBinary(x-1, seq)
    seq.pop(len(seq)-1)



findBinary(5, [])