def is_balanced(string):
    stack = []
    open_set = "[{("
    close_set = "]})"
    for c in string:
        if c in open_set:
            stack.append(c)
        elif c in close_set:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if open_set.index(top) != close_set.index(c):
                return False
    return len(stack) == 0


print(is_balanced("[{()}]"))
print(is_balanced("[]"))
print(is_balanced("(([{()}]()))"))
print(is_balanced("{}()[]"))

print(is_balanced("[{()(})]"))
print(is_balanced("[}"))
print(is_balanced("[{}"))
print(is_balanced("{[}]"))
print(is_balanced("{[}"))
print(is_balanced("}{"))
