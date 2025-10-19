from itertools import count

text = input('Введите текст')

maxx=0
count=0

low_char = "abcdefghijklmnopqrstuvwxyz"
high_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for a in text:
    if a != " ":
        count += 1
    else:
        if count > maxx:
            maxx = count
        count = 0

if count > maxx:
    maxx = count

new_text = ''

for ch in text:
    if ch in low_char:
        for i in range(26):
            if ch == low_char[i]:
                new_text += low_char[(i + maxx) % 26]

    elif ch in high_char:
        for i in range(26):
            if ch == high_char[i]:
                new_text += high_char[(i + maxx) % 26]

    else:
        new_text += ch

print(maxx)
print(new_text)


