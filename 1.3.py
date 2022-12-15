"""
# O(n^3)
def max_subarray_sum(arr):
    n = len(arr)
    max_sum = 0
    for start in range(n):
        for end in range(start+2, n+1):
            s = sum(arr[start:end])
            if s > max_sum:
                max_sum = s
    return max_sum
"""

def max_subarray_sum(arr):
    max_ending_here = 0
    max_so_far = 0
    for x in arr:
        max_ending_here = max(x, max_ending_here+x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print(max_subarray_sum([34, -50, 42, 14, -5, 86])) #137
print(max_subarray_sum([-34, -50, -42, -14, -5, -86])) #0
print(max_subarray_sum([34, -50, 42, 14, -5, 86, -10, -4, 11])) #137
print(max_subarray_sum([-101, 43, -89, -4, -6, 85, 85, -87, 92])) #175
