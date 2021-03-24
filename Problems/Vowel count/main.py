string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = list('aeiou')
count = 0
for char in string:
    if char in vowels:
        count += 1
print(count)
