import arcade


WIDTH = 800
HEIGHT = 800


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_lrtb_rectangle_filled(1, 402, 798, 10, (255, 0, 0))
    arcade.draw_lrtb_rectangle_filled(407, 798, 794, 4, (0, 0, 255))


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
