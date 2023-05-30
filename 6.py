def exp_filter(lst, alpha):
    a = [lst[0]] + [0] * (len(lst) - 1)
    for i in range(1, len(a)):
        a[i] = alpha * lst[i] + (1 - alpha) * a[i - 1]
    return a
a = [1, 3, 5, 6, 8, 10, 12, 13, 15]
print(a, exp_filter(a, 0.5) ,sep = '\n')   