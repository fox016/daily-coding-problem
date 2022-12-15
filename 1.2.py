def window(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")
    for i in range(n):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i
    for i in range(n-1, -1, -1):
        min_seen = min(min_seen, array[i])
        if array[i] > min_seen:
            left = i
    return left, right

print(window([3,5,9,8,6,11]))
print(window([3,5,9,8,6,11,15,2,13]))
print(window([3,7,15,22,5,29]))
