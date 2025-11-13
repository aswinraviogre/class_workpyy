fruits = ["Apple", "Banana", "Mango"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Juice", "Soda", "Water"]

fruits.append("Orange")
vegetables.insert(1, "Onion")
beverages.pop()

inventory = [fruits, vegetables, beverages]

print("First two fruits:", fruits[:2])
print("Last vegetable:", vegetables[-1])
fruit_lengths = [len(item) for item in fruits]

