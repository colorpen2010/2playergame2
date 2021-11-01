import wrap, player

wrap.add_sprite_dir('2playergame_sprites')

wrap.world.create_world(1920, 1080)
wrap.world.set_title('2 player game')
wrap.world.set_back_color(25, 150, 237)
# ground
ground = wrap.sprite.add('mario-scenery', 500, 10, 'ground')
wrap.sprite.set_size(ground, 1920, 200)
wrap.sprite.move_left_to(ground, 0)
wrap.sprite.move_bottom_to(ground, 1080)
groundup = wrap.sprite.get_top(ground)

bottle1 = wrap.sprite.add('bottles', 1920 / 2, 863, 'bottle1')

bottle1_2 = wrap.sprite.add('bottles', 100, 863, 'bottle1')
# player1
player1 = wrap.sprite.add('mario-1-big', 500, 500, 'stand')
# player2
player2 = wrap.sprite.add('mario-2-big', 550, 500, 'stand')
speedy2 = -0
speedy1 = -0


@wrap.on_key_down(wrap.K_DOWN)
def sit2():
    player.changecostume(player2, 'duck')


@wrap.on_key_down(wrap.K_s)
def sit1():
    player.changecostume(player1, 'duck')


def gopbutilka1():
    www1 = wrap.sprite.is_collide_sprite(player1, bottle1)
    if www1 == True:
        wrap.sprite.move_to(player1, 1920 / 2, -500)


def gopbutilka2():
    www2 = wrap.sprite.is_collide_sprite(player2, bottle1)
    if www2 == True:
        wrap.sprite.move_to(player2, 1920 / 2, -500)


@wrap.on_key_up(wrap.K_s)
def set1s():
    player.changecostume(player1, 'stand')


@wrap.on_key_always(wrap.K_UP)
def jump2():
    global speedy2
    player2y = wrap.sprite.get_bottom(player2)
    if player2y == groundup:
        speedy2 = -100
        player.changecostume(player2, 'jump')


@wrap.on_key_down(wrap.K_w)
def jump1():
    global speedy1
    player1y = wrap.sprite.get_bottom(player1)
    if player1y == groundup:
        speedy1 = -4
        player.changecostume(player1, 'jump')


@wrap.always(25)
def down(keys):
    global speedy2, speedy1
    player2botom = wrap.sprite.get_bottom(player2)
    wrap.sprite.move(player2, 0, speedy2)
    if player2botom != groundup:
        if wrap.K_UP in keys and wrap.K_DOWN in keys:
            speedy2 += 50
        else:
            speedy2 += 0.1
        if wrap.sprite.is_collide_sprite(player2, ground) or player2botom > groundup:
            speedy2 = 0
            wrap.sprite.move_bottom_to(player2, groundup)
            player.changecostume(player2, 'stand')
    gopbutilka1()
    gopbutilka2()

    player1botom = wrap.sprite.get_bottom(player1)
    wrap.sprite.move(player1, 0, speedy1)
    if player1botom != groundup:
        speedy1 += 0.1
        if wrap.sprite.is_collide_sprite(player1, ground):
            speedy1 = 0
            wrap.sprite.move_bottom_to(player1, groundup)
            player.changecostume(player1, 'stand')


# hodba2
@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT)
def hodba2(keys):
    if wrap.K_RIGHT in keys:
        player.hodba(player2,6)
    if wrap.K_LEFT in keys:
        player.hodba(player2,-5)


@wrap.on_key_up(wrap.K_RIGHT, wrap.K_LEFT)
def hodba2s():
    player.changecostume(player2, 'stand')


# hodba1
@wrap.on_key_always(wrap.K_d, wrap.K_a)
def hodba1(keys):
    if wrap.K_d in keys:
        player.hodba(player1,5)

    if wrap.K_a in keys:
        player.hodba(player1,-5)

@wrap.on_key_up(wrap.K_a, wrap.K_d)
def hodba1s():
    player.changecostume(player1, 'stand')
