
def move_step(dir : str, ppos, area, speed, dt):

    if dir == "up":
        if ppos.y <= area[1]:
            ppos.y -= round(speed*dt, -1)
        if ppos.y < 0:
            ppos.y = area[1]
        if ppos.y > area[1]:
            ppos.y = 0
    if dir == "down":
        if ppos.y <= area[1]:
            ppos.y += round(speed*dt, -1)
        if ppos.y < 0:
            ppos.y = area[1]
        if ppos.y > area[1]:
            ppos.y = 0
    if dir == "left":
        if ppos.x <= area[0]:
            ppos.x -= round(speed*dt, -1)
        if ppos.x < 0:
            ppos.x = area[0]
        if ppos.x > area[0]:
            ppos.x = 0
    if dir == "right":
        if ppos.x <= area[0]:
            ppos.x += round(speed*dt, -1)
        if ppos.x < 0:
            ppos.x = area[0]
        if ppos.x > area[0]:
            ppos.x = 0
    
    return ppos
        
def random_coord(max : int):
    import random
    return (round(random.randint(0, max),-1), round(random.randint(0, max),-1))
    
