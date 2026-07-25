#A palindrome is a string that reads the same from left to right and right to lef

text = "madam"

reverse = ""

for i in range(len(text)-1,-1,-1):
    reverse=reverse +text[i]

if reverse==text:
    print("palindrome")
else:
    print("Not palindrome")
