def find_missing_number(arr):
    n = len(arr)
    count = [0] * (n + 1)
    for i in arr:
        if 0 <= i <= n:
            count[i] += 1
    for i in range(1, n + 1):
        if count[i] == 0:
            return i
    return n + 1

arr = [1, 3, 5, 6, 7, 9]
print('Массив',*arr, '\nМинималььно пропущенно число', find_missing_number(arr))