n, m = map(int, input().split(" "))
sets = []
for i in range(n+1):
    sets.append(set([i]))
for i in range(m):
    mode, a, b = map(int, input().split(" "))
    if mode == 0:
        temp = set()
        delete = []
        for j in range(len(sets)):
            if a in sets[j] or b in sets[j]:
                temp.add(once)
                delete.append(j)
        sets.append(temp)
        for j in delete:
            del sets[j]
    if mode == 1:
        pass
print(sets)