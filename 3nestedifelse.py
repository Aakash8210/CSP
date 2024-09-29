print("Welcome to the rollercoaster.")
height = int(input("What is your height in cm? "))
if height >=120:
    print("You can ride the rollecoaster.")
    age=int(input("What is your age? "))
    #agar 2 condition ho tab if elif else use karte hai.
    if age <12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You have to grow taller before you can ride.")