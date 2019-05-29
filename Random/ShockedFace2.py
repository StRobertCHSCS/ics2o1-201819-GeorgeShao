import arcade


WIDTH = 800
HEIGHT = 800


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(385, 426, -298, (255, 255, 0))
    arcade.draw_circle_filled(293, 535, 32, (255, 255, 255))
    arcade.draw_circle_filled(524, 534, -19, (255, 255, 255))
    arcade.draw_circle_filled(292, 532, -10, (0, 0, 0))
    arcade.draw_circle_filled(518, 537, 14, (0, 0, 0))
    arcade.draw_ellipse_filled(369, 334, 199, 79, (255, 0, 0))


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
