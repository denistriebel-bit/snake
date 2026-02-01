
def move_step(dir : str, ppos, area, speed, dt):

    if dir == "up":
        if ppos.y <= area[1]:
            ppos.y -= speed*dt
        if ppos.y < 0:
            ppos.y = area[1]
        if ppos.y > area[1]:
            ppos.y = 0
    if dir == "down":
        if ppos.y <= area[1]:
            ppos.y += speed*dt
        if ppos.y < 0:
            ppos.y = area[1]
        if ppos.y > area[1]:
            ppos.y = 0
    if dir == "left":
        if ppos.x <= area[0]:
            ppos.x -= speed*dt
        if ppos.x < 0:
            ppos.x = area[0]
        if ppos.x > area[0]:
            ppos.x = 0
    if dir == "right":
        if ppos.x <= area[0]:
            ppos.x += speed*dt
        if ppos.x < 0:
            ppos.x = area[0]
        if ppos.x > area[0]:
            ppos.x = 0
    
    return ppos
        
        