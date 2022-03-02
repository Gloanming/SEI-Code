

def logo_play():
    """write your code in method"""
    map1010 = [[0 for i in range(15)] for j in range(15)]
    x = 0
    y = 0
    eye = 1
    position = [x,y]
    times = int(input())
    for i in range(0,times):
        command = input().split(' ')
        if len(command) == 3:
            if command[0] == 'R':
                for j in range(1,int(command[1])+1):
                    map1010[y][x + j] = (command[2])
                x = x + int(command[1])
            elif command[0] == 'L':
                for j in range(1,int(command[1])+1):
                    map1010[y][x - j] = (command[2])
                x = x - int(command[1])
            elif command[0] == 'D':
                for j in range(1,int(command[1])+1):
                    map1010[y + j][x] = (command[2])
                y = y + int(command[1])
            elif command[0] == 'U':
                for j in range(1,int(command[1])+1):
                    map1010[y - j][x] = (command[2])
                y = y - int(command[1])
            if x > 9 or y > 9 or x < 0 or y < 0:
                eye = 0
            command = []
        elif len(command) == 2:
            sign = map1010[y][x]
            if command[0] == 'R':
                for j in range(1,int(command[1])+1):
                    map1010[y][x + j] = (sign)
                x = x + int(command[1])
            elif command[0] == 'L':
                for j in range(1,int(command[1])+1):
                    map1010[y][x - j] = (sign)
                x = x - int(command[1])
            elif command[0] == 'D':
                for j in range(1,int(command[1])+1):
                    map1010[y + j][x] = (sign)
                y = y + int(command[1])
            elif command[0] == 'U':
                for j in range(1,int(command[1])+1):
                    map1010[y - j][x] = (sign)
                y = y - int(command[1])
            if x > 9 or y > 9 or x < 0 or y < 0:
                eye = 0
    if eye == 0:
        print('Error!')
        return
    for i in range(0,10):
        for j in range(0,10):
            if map1010[i][j] != 0:
                print(map1010[i][j],end='')
            else:
                print(' ',end='')
        print('\n',end='')
    return
logo_play()