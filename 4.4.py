"""
Reconstruct a list of 0-N given a list of + - signs that denote if the next entry is bigger or smaller
"""

def reconstruct(arr):
    stack = []
    solution = []
    n = len(arr)-1
    for i in range(n):
        if arr[i+1] == "-":
            stack.append(i)
        else:
            solution.append(i)
            while stack:
                solution.append(stack.pop())
    stack.append(n)
    while stack:
        solution.append(stack.pop())
    return solution

print(reconstruct([None, "+", "-", "+", "-"]))
print(reconstruct([None, "-", "-", "-", "-"]))
print(reconstruct([None, "+", "+", "+", "+"]))
print(reconstruct([None, "-", "+", "-", "+"]))
print(reconstruct([None, "-", "-", "+", "+", "-", "-", "-", "+", "-", "+", "+", "-"]))
