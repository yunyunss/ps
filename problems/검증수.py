n = list(map(int, input().split()))
k = 0
for v in n:
    k += v**2
print(k % 10)