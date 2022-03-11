
def logo_play_rect():
    global x
    global y
    global eye
    global sign

    if len(order) == 4:
        sign = order[3]
        wide = int(order[1])
        length = int(order[2])
        for i in range(0,(wide)):
            map1010[y][x+i] = order[3]
            map1010[y+length-1][x+i] = order[3]
        for i in range(0,(length)):
            map1010[y+i][x] = order[3]
            map1010[y+i][x+wide-1] = order[3]
        if x + wide - 1 > 9 or y + length - 1 > 9:
            eye = 0
    if len(order) == 3:
        wide = int(order[1])
        length = int(order[2])

        for i in range(0,(wide)):
            map1010[y][x+i] = sign
            map1010[y+length-1][x+i] = sign
        for i in range(0,(length)):
            map1010[y+i][x] = sign
            map1010[y+i][x+wide-1] = sign
        if x + wide - 1 > 9 or y + length - 1 > 9:
            eye = 0
    return
def logo_play_rect_f():

    global x
    global y
    global eye
    global sign
    if len(order) == 4:
        sign = order[3]
        wide = int(order[1])
        length = int(order[2])
        for i in range(0,length):
            for j in range(0,wide):
                map1010[y+i][x+j] = order[3]
        if x + wide - 1 > 9 or y + length - 1 > 9:
            eye = 0
    if len(order) == 3:
        wide = order[1]
        length = order[2]
        for i in range(0,length):
            for j in range(0,wide):
                map1010[y+i][x+j] = sign
        if x + wide - 1 > 9 or y + length - 1 > 9:
            eye = 0
    return

def logo_play_move():
    """write your code in method"""
    global x
    global y
    global eye
    global sign
    if len(order) == 4:
        sign = order[3]
        if order[1] == 'R':
            for j in range(1,int(order[2])+1):
                if can_draw == 1:
                    map1010[y][x + j] = (order[3])
            x = x + int(order[2])
        elif order[1] == 'L':
            for j in range(1,int(order[2])+1):
                if can_draw == 1:
                    map1010[y][x - j] = (order[3])
            x = x - int(order[2])
        elif order[1] == 'D':
            for j in range(1,int(order[2])+1):
                if can_draw == 1:
                    map1010[y + j][x] = (order[3])
            y = y + int(order[2])
        elif order[1] == 'U':
            for j in range(1,int(order[2])+1):
                if can_draw == 1:
                    map1010[y - j][x] = (order[3])
            y = y - int(order[2])
        if x > 9 or y > 9 or x < 0 or y < 0:
            eye = 0
    elif len(order) == 3:

        if order[1] == 'R':
            for j in range(1,int(order[2])+1):
                if can_draw == 1:
                    map1010[y][x + j] = (sign)
            x = x + int(order[2])
        elif order[1] == 'L':
            for j in range(1,int(order[2])+1):
                if can_draw == 1:
                    map1010[y][x - j] = (sign)
            x = x - int(order[2])
        elif order[1] == 'D':
            for j in range(1,int(order[2])+1):
                if can_draw == 1:
                    map1010[y + j][x] = (sign)
            y = y + int(order[2])
        elif order[1] == 'U':
            for j in range(1,int(order[2])+1):
                if can_draw == 1:
                    map1010[y - j][x] = (sign)
            y = y - int(order[2])
        if x > 9 or y > 9 or x < 0 or y < 0:
            eye = 0
    if eye == 0:
        print('Error!')
        return
def logo_play_cross():
    global x
    global y
    global eye
    global sign
    if len(order) == 3:
        sign = order[2]
        for i in range(0,int (order[1])+1):
            map1010[y][x+i] = order[2]
            map1010[y][x-i] = order[2]
            map1010[y+i][x] = order[2]
            map1010[y-i][x] = order[2]
        if x + int(order[1]) > 9 or x - int(order[1]) < 0 or y - int(order[1]) < 0 or y + int(order[1]) > 9:
            eye = 0
    if len(order) == 2:
        for i in range(0 , int(order[1]) + 1):
            map1010[y][x+i] = sign
            map1010[y][x-i] = sign
            map1010[y+i][x] = sign
            map1010[y-i][x] = sign
        if x + int(order[1]) > 9 or x - int(order[1]) < 0 or y - int(order[1]) < 0 or y + int(order[1]) > 9:
            eye = 0

def logo_play():
    """write your code here :)"""
    global map1010
    global x
    global y
    global eye
    global sign
    x = 0
    y = 0
    eye = 1
    map1010 = [[0 for i in range(15) ] for j in range(15)]
    global can_draw
    can_draw = 1
    while 1:
        global order
        order = list(input().split())

        #print(order)
        if order[0] == 'pen_up':
            can_draw = 0
        if order[0] == 'pen_down':
            can_draw = 1
        elif order[0] == 'move':
            logo_play_move()
        elif order[0] == 'cross':
            logo_play_cross()
        elif order[0] == 'rect':
            logo_play_rect()
        elif order[0] == 'rect_f':
            logo_play_rect_f()
        if order[0] == 'end':
            if eye == 1:
                for i in range(0,10):
                    for j in range(0,10):
                        if map1010[i][j] != 0:
                            print(map1010[i][j],end='')
                        else:
                            print(' ',end='')
                    print('\n',end='')
                break
            if eye == 0:
                print('Error!')
                break

    return
logo_play()