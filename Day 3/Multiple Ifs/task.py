print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want to have a photo taken° Type Y for yes and n for No.")
    if wants_photo == "y":
        bill += 3
    else:
        bill

    print(f"Your final bill is ${bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")
