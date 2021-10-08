import wrap

wrap.world.create_world(1000, 1000)
wrap.world.set_title('2 player game')
wrap.world.set_back_color(25, 150, 237)
# ground
ground = wrap.sprite.add('mario-scenery', 500, 10, 'ground')
wrap.sprite.set_size(ground, 1000, 470)
wrap.sprite.move_bottom_to(ground, 1000)
# player1
player1 = wrap.sprite.add('mario-1-big', 500, 500, 'stand')
# player2
player2 = wrap.sprite.add('mario-2-big', 550, 500, 'stand')
wrap.sprite.set_reverse_x(player2, True)
speedy = -4


def walk(p):
    cos2 = wrap.sprite.get_costume(p)
    if cos2 == 'stand':
        wrap.sprite.set_costume(p, 'walk1')
    elif cos2 == 'walk1':
        wrap.sprite.set_costume(p, 'walk2')
    elif cos2 == 'walk2':
        wrap.sprite.set_costume(p, 'walk3')
    elif cos2 == 'walk3':
        wrap.sprite.set_costume(p, 'walk1')
@wrap.on_key_down(wrap.K_UP)
def jump():

    global speedy
    speedy=-4

@wrap.always(25)
def down():
    global speedy
    speedy+=0.1
    wrap.sprite.move(player2, 0, speedy)


# hodba2
@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT)
def hodba2(keys):
    walk(player2)
    if wrap.K_RIGHT in keys:
        wrap.sprite.move(player2, 5, 0)
        wrap.sprite.set_reverse_x(player2, False)

    if wrap.K_LEFT in keys:
        wrap.sprite.move(player2, -5, 0)
        wrap.sprite.set_reverse_x(player2, True)


# hodba1
@wrap.on_key_always(wrap.K_d, wrap.K_a)
def hodba1(keys):
    walk(player1)
    if wrap.K_d in keys:
        wrap.sprite.move(player1, 5, 0)
        wrap.sprite.set_reverse_x(player1, False)

    if wrap.K_a in keys:
        wrap.sprite.move(player1, -5, 0)
        wrap.sprite.set_reverse_x(player1, True)
