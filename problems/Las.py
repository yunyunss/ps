n = int(input())
trees = dict()
result = 0

for i in range(n):
    g, r = map(int, input().split())
    if r not in trees.keys():
        trees[r] = [0, 0]
    if trees[r][0] < g:
        trees[r][0] = g
        trees[r][1] = 1
    elif trees[r][0] == g:
        trees[r][1] += 1

for key, value in trees.items():
    result += value[1]

print(result)