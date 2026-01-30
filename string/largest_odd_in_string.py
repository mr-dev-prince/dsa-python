
def largest_odd(str):
    if int(str) % 2 == 1:
        return str
    
    ans = ""
    arr = [ch for ch in str]
    
    ws = 0
    cur = []
    for we in range(len(arr)):
        cur.append(arr[we])

        curNum = int("".join(cur))
        while curNum % 2 != 1 and len(cur) > 0:
            cur.pop()
            ws += 1
        
        if curNum % 2 == 1:
            ans = "".join(cur)

    return ans

print(largest_odd("35427"))