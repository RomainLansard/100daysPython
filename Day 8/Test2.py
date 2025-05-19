def life_in_weeks(weeks):
    weeks = (90 * 52) - (weeks * 52)
    print(f"You have {weeks} left.")

age = int(input("What's your age\n"))

life_in_weeks(age)