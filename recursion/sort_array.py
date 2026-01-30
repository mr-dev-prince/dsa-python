def insert_at_correct_place(arr, key):
    if len(arr) == 0 or key >= arr[-1]:
        arr.append(key)
        return

    temp = arr[-1]
    arr.pop()
    insert_at_correct_place(arr, key)
    arr.append(temp)

def sort_arr(arr):
    if len(arr) == 0: return

    key = arr.pop()
    sort_arr(arr)
    insert_at_correct_place(arr, key)

arr = [1,3,10,4,2,7,5]
sort_arr(arr)
print(arr)