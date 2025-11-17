import random
import math

names_input = input("Enter the names of invited guests (comma-separated): ")

names_list = [name.strip() for name in names_input.split(",")]

unique_names = list(set(names_list))

selected_name = random.choice(unique_names)

reversed_name = selected_name[::-1]

count_unique = len(unique_names)

sqrt_value = round(math.sqrt(count_unique))

print("Unique Names:", unique_names)
print("Selected Name:", selected_name)
print("Reversed Selected Name:", reversed_name)
print("Total Unique Names:", count_unique)
print("Rounded Square Root:", sqrt_value)
