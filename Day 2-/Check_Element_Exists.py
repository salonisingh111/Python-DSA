nums = [5, 8, 2, 9, 1]

target = 9

found = False

for i in nums:
    if i == target:
        found = True

if found:
    print("Found")
else:
    print("Not Found")