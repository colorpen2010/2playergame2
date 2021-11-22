import wrap


def changecostume(sprite, costume):
    spritebotom = wrap.sprite.get_bottom(sprite)
    wrap.sprite.set_costume(sprite, costume)
    wrap.sprite.move_bottom_to(sprite, spritebotom)

def semla(sprite,ostrowa,ground):
    groundup = wrap.sprite.get_top(ground)
    ostrowacopy=list(ostrowa)
    if sprite in ostrowacopy:
        ostrowacopy.remove(sprite)

    for o in list(ostrowacopy):
        ostrowdown = wrap.sprite.get_bottom(o)
        ostrowleft = wrap.sprite.get_left(o)
        ostrowRight = wrap.sprite.get_right(o)
        playerLeft = wrap.sprite.get_left(sprite)
        playerright = wrap.sprite.get_right(sprite)
        playerdown = wrap.sprite.get_bottom(sprite)
        if playerLeft >= ostrowRight:
            ostrowacopy.remove(o)
        elif playerright <= ostrowleft:
            ostrowacopy.remove(o)
        elif playerdown>= ostrowdown:
            ostrowacopy.remove(o)

    minh = groundup
    ground2 = ground
    for o in ostrowacopy:
        ostrowup = wrap.sprite.get_top(o)
        if ostrowup < minh:
            minh = ostrowup
            ground2 = o
    return ground2

def speeddow(sprite, speed, ground, costume):
    groundup = wrap.sprite.get_top(ground)
    spritebotom = wrap.sprite.get_bottom(sprite)
    wrap.sprite.move(sprite, 0, speed)
    if spritebotom != groundup:
        speed += 0.1
        if wrap.sprite.is_collide_sprite(sprite, ground):
            speed = 0
            wrap.sprite.move_bottom_to(sprite, groundup)
            changecostume(sprite, costume)
    return speed


def walk(p):
    cos2 = wrap.sprite.get_costume(p)
    if cos2 == 'stand':
        changecostume(p, 'walk1')
    elif cos2 == 'walk1':
        changecostume(p, 'walk2')
    elif cos2 == 'walk2':
        changecostume(p, 'walk3')
    elif cos2 == 'walk3':
        changecostume(p, 'walk1')


def hodba(p, storona, stena):
    wrap.sprite.move(p, storona, 0)
    walk(p)
    if wrap.sprite.is_collide_sprite(stena, p):
        wrap.sprite.move(stena,storona,0)

    if storona < 0:
        wrap.sprite.set_reverse_x(p, True)
    if storona > 0:
        wrap.sprite.set_reverse_x(p, False)
