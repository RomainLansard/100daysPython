def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    score1 = 0
    score2 = 0
    for letter in combined_names:
        if letter in "true":
            score1 += 1
    for letter in combined_names:
        if letter in "love":
            score2 += 1
    score = str(score1) + str(score2)
    print(f"Your love score is: {score}")


calculate_love_score("Kanye West", "Kim Kardashian")