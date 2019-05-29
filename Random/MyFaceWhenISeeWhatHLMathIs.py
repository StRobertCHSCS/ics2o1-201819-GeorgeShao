import arcade


WIDTH = 800
HEIGHT = 800


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(387, 441, -357, (255, 255, 0))
    arcade.draw_circle_filled(266, 589, 24, (255, 255, 255))
    arcade.draw_circle_filled(263, 589, 37, (255, 255, 255))
    arcade.draw_circle_filled(519, 590, 35, (255, 255, 255))
    arcade.draw_circle_filled(261, 592, -12, (0, 0, 0))
    arcade.draw_circle_filled(517, 591, -12, (0, 0, 0))
    arcade.draw_ellipse_filled(383, 334, 227, 77, (255, 0, 0))


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
