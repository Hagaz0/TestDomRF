def nvl(val1, val2):
    return val2 if val1 is None else val1


print(nvl(5, 9))
print(nvl(None, 6))
print(nvl(8, None))