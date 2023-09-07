"""
https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
Sliding Window Maximum (Maximum of all subarrays of size K)
Given an array and an integer K, find the maximum for each and every contiguous subarray of size K.
"""

# O(n*k) time
# O(1) auxiliary space
def print_sliding_window_max_naive(arr, k):
    for i in range(len(arr)-k+1):
        print(max(arr[i:i+k]))

# O(n) time
# O(k) auxiliary space
from collections import deque
def print_sliding_window_max(arr, k):
    print(arr, "k =", k)
    dq = deque()
    for i in range(k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    for i in range(k, len(arr)):
        print(arr[dq[0]])
        if dq and dq[0] <= i-k:
            dq.popleft()
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    print(arr[dq[0]])
    print()

print_sliding_window_max([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)
print_sliding_window_max([4, 7, 2, 9, 1, 8, 3, 6, 5, 2], 3)
print_sliding_window_max([4, 7, 2, 9, 1, 8, 3, 6, 5, 2], 5)
print_sliding_window_max([4, 7, 2, 9, 1, 8, 3, 6, 5, 2], 2)
