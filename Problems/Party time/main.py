stop = False
res = []
while not stop:
    val = input()
    if val == '.':
        break
    else:
        res.append(val)
print(res)
print(len(res))
