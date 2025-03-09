#pr1= float(input("what was the total bill? "))
#pr2= float(input("How much tip would you like to give? "))
#pr3= int(input("How many people to split the bill? "))
print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
split = int(input("How many people to split the bill?\nPeople:"))

total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))

print(f"Each person should pay: ${total}")
