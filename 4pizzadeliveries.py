print("Welcome to the Python Pizza deliveries!")
size = input("What will be  the size of your pizza? S , M or L.")
bill = 0
add_pepperoni = input("Do you want to add pepperoni? Y or N.")
extra_cheese = input("Do you want extra cheese? Y or N.")
if size == "S":
    bill +=15
elif size == "M":
    bill +=20
else:
    bill +=25
if add_pepperoni =="Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
if extra_cheese =="Y":
    bill +=1
print(f"Yout final amount is: ${bill}.")