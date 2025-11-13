import random  

apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25

total_volume = apple_juice + orange_juice + grape_juice
print("Total volume of juice sold:", total_volume, "liters")

total_volume_int = int(total_volume)
print("Total volume (integer):", total_volume_int, "liters")

total_volume_str = str(total_volume)
print("The shop sold a total of " + total_volume_str + " liters of juice today.")

bonus = random.randint(5, 10)
final_total = total_volume + bonus
print("After adding bonus liters (" + str(bonus) + "):", final_total, "liters")
