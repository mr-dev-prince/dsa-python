def ans(n):
    for i in range(n + 1):
        z = 1 << i
        print(z)
        if z > n:
            return z - 1
    return 0

print(ans(5))

# logic

# 2 ** 0 -> 1 : all set bits
# 2 ** 1 -> 2 -> 2 - 1 --> 1 : all set bits
# 2 ** 2 -> 4 -> 4 - 1 --> 3 : all set bits 
# 2 ** 3 -> 8 -> 8 - 1 --> 7 : all set bits
# 2 ** 4 -> 16 -> 16 - 1 --> 15 : all set bits
# 2 ** 5 -> 32 -> 32 - 1 --> 31 : all set bits
# and so on