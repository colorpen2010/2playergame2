import wrap

wrap.world.create_world(1000, 1000)
wrap.world.set_title('2 player game')
wrap.world.set_back_color(25, 150, 237)
# ground
ground = wrap.sprite.add('mario-scenery', 500, 10, 'ground')
wrap.sprite.set_size(ground, 700, 470)
wrap.sprite.move_bottom_to(ground, 1000)

# player1
player1 = wrap.sprite.add('mario-1-big', 500, 500, 'stand')
# player2
player2 = wrap.sprite.add('mario-2-big', 550, 500, 'stand')
wrap.sprite.set_reverse_x(player2, True)
speedy2 = -0
wrap.sprite.set_reverse_x(player1, True)
speedy1 = -0


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

@wrap.on_key_down(wrap.K_DOWN)
def sit2():
    wrap.sprite.set_costume(player2, 'duck')

@wrap.on_key_down(wrap.K_UP)
def jump2():
    global speedy2
    player2y = wrap.sprite.get_y(player2)
    if player2y == 500:
        speedy2 = -4


@wrap.on_key_down(wrap.K_w)
def jump1():
    global speedy1
    player1y = wrap.sprite.get_y(player1)
    if player1y == 500:
        speedy1 = -4


@wrap.always(25)
def down():
    global speedy2, speedy1
    print(speedy1, speedy2)
    speedy2 += 0.1
    wrap.sprite.move(player2, 0, speedy2)
    if wrap.sprite.is_collide_sprite(player2, ground):
        speedy2 = 0
        wrap.sprite.move_to(player2, wrap.sprite.get_x(player2), 500)
    speedy1 += 0.1
    wrap.sprite.move(player1, 0, speedy1)
    if wrap.sprite.is_collide_sprite(player1, ground):
        speedy1 = 0
        wrap.sprite.move_to(player1, wrap.sprite.get_x(player1), 500)


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
