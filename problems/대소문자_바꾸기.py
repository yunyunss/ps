text = input()

for i in text:
    if ord(i) >= 97:
        i = chr(ord(i) - 32)
    else:
        i = chr(ord(i) + 32)
    print(i, end='')