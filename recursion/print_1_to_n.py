def print_num(n):
    if n == 0: return
    print_num(n-1)
    print(n)

def print_rev(n):
    if n == 0: return
    print(n)
    print_rev(n-1)

