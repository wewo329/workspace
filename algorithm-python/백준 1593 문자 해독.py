import sys
w_len, s_len = map(int, sys.stdin.readline().split())
w = "".join(sorted(list(input())))
s = input()
result = []
for i in range(s_len-(w_len-1)):
    if "".join(sorted(list(s[i:i+w_len]))) == w:
        result.append(s[i:i+w_len])
print(len(set(result)))
