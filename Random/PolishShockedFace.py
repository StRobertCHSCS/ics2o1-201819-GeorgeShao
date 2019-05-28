import arcade


WIDTH = 800
HEIGHT = 800


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_lrtb_rectangle_filled(2, 797, 793, 402, (245, 245, 245))
    arcade.draw_lrtb_rectangle_filled(1, 796, 403, 4, (255, 0, 0))
    arcade.draw_circle_filled(268, 502, -275, (255, 255, 0))
    arcade.draw_circle_filled(191, 587, -32, (0, 0, 0))
    arcade.draw_circle_filled(375, 585, 29, (0, 0, 0))
    arcade.draw_ellipse_filled(256, 406, 161, 74, (255, 0, 0))


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
