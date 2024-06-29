string = "My Name Is Josh"
substring = "Name"

for word in string.split():
    if substring == word:
        print("Match Found")