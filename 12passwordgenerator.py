import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cap_Letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','*','&']
print("Welcome the Python Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_Caps= int(input("How many Capital Letters would you like in your password?\n"))
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_Caps):
    password_list.append(random.choice(cap_Letters))


random.shuffle(password_list)

password = ""
for char in password_list:
    password+=char

print(f"Your password is: {password}")