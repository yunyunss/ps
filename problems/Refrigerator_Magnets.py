text = ""
letters = []
acceptable = True

while True:
    text = input()
    if text == "END":
        break
    for letter in list(text):
        if letter in letters:
            acceptable = False
            break
        letters.append(letter) if letter != ' ' else None
    if acceptable:
        print(text)
    letters = []
    acceptable = True