lines = []

while True:
    lines = list(map(int, input().split()))
    lines.sort()
    if lines == [0 , 0, 0]:
        break
    if lines[0] ** 2 + lines[1] ** 2 != lines[2] ** 2:
        print("wrong")
    else:
        print("right")