header = "\tBookstore Receipt\n\t-------------------\n"
book1 = "Python Basics"
price1 = 450
book2 = "Data Science Intro"
price2 = 600

line1 = "Book: {}\tPrice: ₹{}".format(book1, price1)
line2 = "Book: {}\tPrice: ₹{}".format(book2, price2)

total = price1 + price2
total_line = "Total:\t\t₹{}".format(total)

thank_you = "\n\tThank you for shopping with us!"

receipt = header + line1 + "\n" + line2 + "\n" + total_line + thank_you

print(receipt.upper())

