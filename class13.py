item = input("Enter the name of a new item: ")

try:
    with open("items.txt", "r") as f:
        pass
    file_exists = True
except FileNotFoundError:
    file_exists = False

if not file_exists:
    with open("items.txt", "w") as f:
        f.write(item + "\n")
else:
    with open("items.txt", "a") as f:
        f.write(item + "\n")

print("\nFull list of items:")
with open("items.txt", "r") as f:
    for line in f:
        print(line.strip())
