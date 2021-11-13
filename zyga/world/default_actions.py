def move_left():
    print('moved left')

def move_right():
    print('moved right')

def move_up():
    print('moved up')

# def move_down():
#     print('moved down')

def get_default_action_methods():
    return {
        'move_left': move_left, 
        'move_right': move_right, 
        'move_up': move_up
        }
