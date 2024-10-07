n = list(input())
if n[0] == 'F':
    print('0.0')
else:
    n[0] = 69 - ord(n[0])
    if n[1] == '0':
        print(f'{n[0]}.0')
    elif n[1] == '+':
        print(f'{n[0]}.3')
    else:
        print(n[0]-0.3)