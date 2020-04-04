import sys

testCases, length = map(int, input().split(" "))
for test in range(testCases):
    bits = [0] * length
    spots = [int(x) for x in range(1, length + 1)]
    bitpos = 1
    sameValIndex = 1
    DiffValIndex1 = 1
    DiffValIndex2 = length
    for i in range(5):
        print(bitpos)
        sys.stdout.flush()
        bits[bitpos-1] = int(input())
        spots.remove(bitpos)
        print(length - bitpos + 1)
        sys.stdout.flush()
        bits[length - bitpos] = int(input())
        spots.remove(length - bitpos + 1)
        if bits[bitpos-1] != bits[length - bitpos]:
            DiffValIndex1 = bitpos
            DiffValIndex2 = length - bitpos + 1
        else:
            sameValIndex = bitpos
        bitpos += 1
    if length == 10:
        print(''.join(str(x) for x in bits))
        sys.stdout.flush()
        if input() == 'N':
            sys.exit(0)
        continue
    for i in range(14):
        newbits = [0] * length
        for position in range(1, length + 1):
            newbits[position-1] = 0
        print(DiffValIndex1)
        sys.stdout.flush()
        newbits[DiffValIndex1-1] = int(input())
        print(DiffValIndex2)
        sys.stdout.flush()
        newbits[DiffValIndex2-1] = int(input())
        print(sameValIndex)
        sys.stdout.flush()
        newbits[sameValIndex-1] = int(input())
        complementAndReverse = bits[sameValIndex-1] != newbits[sameValIndex-1]
        complement = bits[sameValIndex-1] != newbits[sameValIndex-1] and bits[DiffValIndex1-1] != newbits[DiffValIndex1-1] and \
                     bits[DiffValIndex2-1] != newbits[DiffValIndex2-1]
        reverse = bits[DiffValIndex1-1] != newbits[DiffValIndex1-1] and bits[DiffValIndex2-1] != newbits[DiffValIndex2-1]
        if complement:
            for position in range(1, length + 1):
                newbits[position-1] = bits[position-1]
                if newbits[position-1] == 0:
                    newbits[position-1] = 1
                else:
                    newbits[position-1] = 0
        elif complementAndReverse:
            for position in range(1, length + 1):
                newbits[position-1] = bits[length - position]
                if newbits[position-1] == 0:
                    newbits[position-1] = 1
                else:
                    newbits[position-1] = 0
            
            spots2 = []
            for spot in spots:
                spots2.append(length + 1 - spot)
            spots = spots2
            
        elif reverse:
            for position in range(1, length + 1):
                newbits[position-1] = bits[length - position]
            spots2 = []
            
            for spot in spots:
                spots2.append(length + 1 - spot)
            spots = spots2
            
        else:
            for position in range(1, length + 1):
                newbits[position-1] = bits[position-1]
        bits = newbits
        count = 0
        spots3 = []
        for spot in spots:
            print(spot)
            sys.stdout.flush()
            bits[spot-1] = int(input())
            bitpos += 1
            count += 1
            spots3.append(spot)
            if count == 7:
                break
        spots = [x for x in spots if x not in spots3]
        if bitpos > length - 5:
            print(''.join(str(x) for x in bits))
            sys.stdout.flush()
            if(input()=='N'):
                sys.exit(0)
            break

