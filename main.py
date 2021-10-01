import wrap

wrap.world.create_world(1000, 1000)
wrap.world.set_title('2 player game')
wrap.world.set_back_color(25, 150, 237)
# player1
player1 = wrap.sprite.add('mario-1-big', 500, 500, 'stand')
# player2
player2 = wrap.sprite.add('mario-2-big', 550, 500, 'stand')
wrap.sprite.set_reverse_x(player2, True)
# ground
ground = wrap.sprite.add('mario-scenery', 500, 10, 'ground')
wrap.sprite.set_size(ground, 1000, 470)
wrap.sprite.move_bottom_to(ground, 1000)


# hodba2
@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT)
def hodba2(keys):
    cos2 = wrap.sprite.get_costume(player2)
    if wrap.K_RIGHT in keys:
        wrap.sprite.move(player2, 5, 0)
        wrap.sprite.set_reverse_x(player2, False)
        if cos2 == 'stand':
            wrap.sprite.set_costume(player2, 'walk1')
        elif cos2 == 'walk1':
            wrap.sprite.set_costume(player2, 'walk2')
        elif cos2 == 'walk2':
            wrap.sprite.set_costume(player2, 'walk3')
        elif cos2 == 'walk3':
            wrap.sprite.set_costume(player2, 'walk1')

    if wrap.K_LEFT in keys:
        wrap.sprite.move(player2, -5, 0)
        wrap.sprite.set_reverse_x(player2, True)
        if cos2 == 'stand':
            wrap.sprite.set_costume(player2, 'walk1')
        elif cos2 == 'walk1':
            wrap.sprite.set_costume(player2, 'walk2')
        elif cos2 == 'walk2':
            wrap.sprite.set_costume(player2, 'walk3')
        elif cos2 == 'walk3':
            wrap.sprite.set_costume(player2, 'walk1')


# hodba1
@wrap.on_key_always(wrap.K_d, wrap.K_a)
def hodba1(keys):
    cos2 = wrap.sprite.get_costume(player1)
    if wrap.K_d in keys:
        wrap.sprite.move(player1, 5, 0)
        wrap.sprite.set_reverse_x(player1, False)
        if cos2 == 'stand':
            wrap.sprite.set_costume(player1, 'walk1')
        elif cos2 == 'walk1':
            wrap.sprite.set_costume(player1, 'walk2')
        elif cos2 == 'walk2':
            wrap.sprite.set_costume(player1, 'walk3')
        elif cos2 == 'walk3':
            wrap.sprite.set_costume(player1, 'walk1')

    if wrap.K_a in keys:
        wrap.sprite.move(player1, -5, 0)
        wrap.sprite.set_reverse_x(player1, True)
        if cos2 == 'stand':
            wrap.sprite.set_costume(player1, 'walk1')
        elif cos2 == 'walk1':
            wrap.sprite.set_costume(player1, 'walk2')
        elif cos2 == 'walk2':
            wrap.sprite.set_costume(player1, 'walk3')
        elif cos2 == 'walk3':
            wrap.sprite.set_costume(player1, 'walk1')
