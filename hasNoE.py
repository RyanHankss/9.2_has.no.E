total = 0.0
no_e = 0.0


def has_no_e(w):
    for e in word:
        if e == 'e':
            return False
    return True

fin = open('words.txt')


for line in fin:
    word = line.strip()
    total += 1
    result = has_no_e(word)
    if result is True:
        print word
        no_e += 1

percent = round(no_e/total, 2)

print("The amount of words that are spelt without the letter 'e' is " + str(no_e) + ", out of " + str(total) + " words")

print("The percent of words spelt without 'e' is " + str(percent) + "%")
