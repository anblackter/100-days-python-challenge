# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def face_up():
    while not is_facing_north():
        turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
initial_position = True
while not at_goal():
    if initial_position:
        face_up()
        initial_position = False
        
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()