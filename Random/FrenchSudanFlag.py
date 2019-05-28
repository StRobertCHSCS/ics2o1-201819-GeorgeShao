import arcade


WIDTH = 900
HEIGHT = 800


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_lrtb_rectangle_filled(103, 339, 796, 3, (0, 0, 255))
    arcade.draw_lrtb_rectangle_filled(700, 895, 791, 6, (255, 0, 0))
    arcade.draw_lrtb_rectangle_filled(397, 675, 212, 187, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(519, 536, 453, 196, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(520, 668, 453, 438, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(402, 520, 453, 439, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(397, 417, 209, 72, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(647, 669, 212, 87, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(404, 419, 575, 446, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(642, 665, 568, 444, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(519, 533, 475, 445, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(384, 428, 593, 530, (255, 255, 255))
    arcade.draw_lrtb_rectangle_filled(623, 673, 590, 539, (255, 255, 255))
    arcade.draw_lrtb_rectangle_filled(632, 673, 556, 533, (255, 255, 255))
    arcade.draw_circle_filled(525, 517, 30, (0, 0, 0))
    arcade.draw_circle_filled(523, 517, 36, (0, 0, 0))
    arcade.draw_circle_filled(522, 523, 56, (0, 0, 0))


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
