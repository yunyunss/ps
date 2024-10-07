num_of_participant = int(input())
num_of_shirts_by_size = list(map(int, input().split()))
num_of_bundles_of_shirts, num_of_bundles_of_pens = map(int, input().split())

count = 0

for i in num_of_shirts_by_size:
    q = int(i / num_of_bundles_of_shirts)
    r = i % num_of_bundles_of_shirts
    if r == 0:
        pass
    else:
        r = 1
    count += q + r

print(count)
print(int(num_of_participant / num_of_bundles_of_pens), num_of_participant % num_of_bundles_of_pens)