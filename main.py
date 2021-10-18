import wrap

wrap.world.create_world(1920, 1080)
wrap.world.set_title('2 player game')
wrap.world.set_back_color(25, 150, 237)
# ground
ground = wrap.sprite.add('mario-scenery', 500, 10, 'ground')
wrap.sprite.set_size(ground, 1920, 200)
wrap.sprite.move_left_to(ground, 0)
wrap.sprite.move_bottom_to(ground,1080)
groundup=wrap.sprite.get_top(ground)

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
@wrap.on_key_up(wrap.K_DOWN)
def set2s():
    wrap.sprite.set_costume(player2,'stand')

@wrap.on_key_down(wrap.K_s)
def sit1():
    wrap.sprite.set_costume(player1, 'duck')

@wrap.on_key_always(wrap.K_UP)
def jump2():
    global speedy2
    wrap.sprite.set_costume(player2,'jump')
    player2y = wrap.sprite.get_bottom(player2)
    if player2y == groundup:
        speedy2 = -4

@wrap.on_key_down(wrap.K_w)
def jump1():
    global speedy1
    player1y = wrap.sprite.get_bottom(player1)
    if player1y == groundup:
        speedy1 = -4

@wrap.on_key_up(wrap.K_w)
def jump1s():
    wrap.sprite.set_costume(player1,'stand')

@wrap.always(25)
def down():
    global speedy2, speedy1
    speedy2 += 0.1
    wrap.sprite.move(player2, 0, speedy2)
    if wrap.sprite.is_collide_sprite(player2, ground):
        speedy2 = 0
        wrap.sprite.move_bottom_to(player2,groundup)
        wrap.sprite.set_costume(player2,'stand')
    speedy1 += 0.1
    wrap.sprite.move(player1, 0, speedy1)
    if wrap.sprite.is_collide_sprite(player1, ground):
        speedy1 = 0
        wrap.sprite.move_bottom_to(player1,groundup)
        wrap.sprite.set_costume(player1,'stand')


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
@wrap.on_key_up(wrap.K_RIGHT, wrap.K_LEFT)
def hodba2s():
    wrap.sprite.set_costume(player2,'stand')

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

@wrap.on_key_up(wrap.K_a,wrap.K_d)
def hodba1s():
    wrap.sprite.set_costume(player1, 'stand')
