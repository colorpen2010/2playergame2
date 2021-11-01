import wrap, random


def changecostume(sprite, costume):
    spritebotom = wrap.sprite.get_bottom(sprite)
    wrap.sprite.set_costume(sprite, costume)
    wrap.sprite.move_bottom_to(sprite, spritebotom)


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


def hodba(p, storona):
    wrap.sprite.move(p, storona, 0)
    walk(p)
    if storona<0:
        wrap.sprite.set_reverse_x(p,True)
    if storona>0:
        wrap.sprite.set_reverse_x(p,False)