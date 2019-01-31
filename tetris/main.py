from microbit import *
import random

item_list = [
  [['10', '11'], ['11', '10'], ['11', '01'], ['01', '11']],
  [['10', '10'], ['11', '00']],
  [['01', '10'], ['10', '01']]
]
min_y = 0
min_x = 0
max_y = 4
max_x = 4
pause_ms = 2000
pause_step = 100
graveyard = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

def item_save(item, x, y, brightness, zone):
    for inc_y, row in enumerate(item):
        for inc_x, column in enumerate(row):
            if x+inc_x >= min_x and x+inc_x <= max_x and y+inc_y >= min_y and y+inc_y <= max_y:
                if column == '1':
                    if zone in ['screen', 'both']:
                        display.set_pixel(x+inc_x, y+inc_y, brightness)
                    if zone in ['graveyard', 'both']: 
                        graveyard[x+inc_x][y+inc_y] = brightness

def item_plot(item, x, y, zone='screen'):
    item_save(item, x, y, 9, zone)

def item_unplot(item, x, y, zone='screen'):
    item_save(item, x, y, 0, zone)

def item_rotate(item_piece, item_pos, mod, x, y):
    item = item_piece[item_pos]
    item_unplot(item, x, y)
    item_pos_tmp = item_pos + mod
    if item_pos_tmp >= len(item_piece):
        item_pos_tmp = 0
    item = item_piece[item_pos_tmp]
    for inc_y, row in enumerate(item):
        for inc_x, column in enumerate(row):
            if column == '1':
                if graveyard[x+inc_x][y+inc_y] == 9:
                    return item_pos
    
    item_plot(item, x, y)
    return item_pos_tmp
    
def move_horizontal(item, x, y, mod):
    for inc_y, row in enumerate(item):
        for inc_x, column in enumerate(row):
            if column == '1':
                if x+inc_x+mod < min_x or x+inc_x+mod > max_x:
                    return x
                if graveyard[x+inc_x+mod][y+inc_y] == 9:
                    return x
    item_unplot(item, x, y)
    x = x+mod
    item_plot(item, x, y)
    return x

def check_limit_vertical(item, x, y, mod):
    for inc_y, row in enumerate(item):
        for inc_x, column in enumerate(row):
            if column == '1':
                if y+inc_y+mod > max_y:
                    return True
                if graveyard[x+inc_x][y+inc_y+mod] == 9:
                    return True
    return False
    
def check_line_graveyard():
    for inc_y in range(0, max_y+1):
        for inc_x in range(0, max_x):
            if graveyard[inc_x][inc_y] != 9:
                break
        else:
            animation_line(inc_y)
            
def animation_line(y):
    line = ['1'*5]
    for rep in range(8, -1, -1):
        item_save(line, 0, y, rep, 'both')
        sleep(rep*10)

while True:
    x = random.randint(min_x, max_x)
    item_piece = random.choice(item_list)
    item_pos = random.randint(0, len(item_piece))-1
    item = item_piece[item_pos]
    
    for y in range(-1, max_y+1):
        item_unplot(item_piece[item_pos], x, y-1)
        item_plot(item_piece[item_pos], x, y)
        for pause in range(0, pause_ms, pause_step):
            (a, b) = (button_a.was_pressed(), button_b.was_pressed())
            if a and b:
                item_pos = item_rotate(item_piece, item_pos, +1, x, y)
            if a:
                x = move_horizontal(item_piece[item_pos], x, y, -1)
            if b:
                x = move_horizontal(item_piece[item_pos], x, y, +1)
            sleep(pause_step)
        if check_limit_vertical(item_piece[item_pos], x, y, +1):
            item_plot(item_piece[item_pos], x, y, 'graveyard')
            check_line_graveyard()
            break
