text = input('Введите текст:')
word = ''

for i in range(len(text) - 1, -1, -1):
    word += text[i]

w = []
words = ''

for i in text:
    if i == ' ':
        w.append(words)
        words = ''
    else:
        words += i

if words:
    w.append(words)

m = ''

for i in range(len(w) - 1, -1, -1):
    m += w[i] + (' ' if i != 0 else '')

print("Зеркальный порядок: ", m)
print("Отзеркаленная строка: ", word)




