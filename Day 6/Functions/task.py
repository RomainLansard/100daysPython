#Reeborg's World Maze

def turn_right():
    for _ in range(3):
        turn_left()


while not at_goal():
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()