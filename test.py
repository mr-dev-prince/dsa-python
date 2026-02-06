
def countSetBits(n):
    count = 0

    while n:
        bit = n & 1
        if bit:
            count += 1
        n = n >> 1

    return count

print(countSetBits(2147483645))