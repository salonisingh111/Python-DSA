text = "Python123@#"

alphabets = 0
digits = 0
special = 0

for ch in text:

    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        alphabets += 1

    elif '0' <= ch <= '9':
        digits += 1

    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special Characters:", special)
