import arcade


WIDTH = 800
HEIGHT = 800


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(371, 438, -307, (255, 255, 0))
    arcade.draw_circle_filled(252, 581, 47, (255, 255, 255))
    arcade.draw_circle_filled(475, 589, -50, (255, 255, 255))
    arcade.draw_circle_filled(253, 584, 13, (255, 255, 255))
    arcade.draw_circle_filled(245, 585, 18, (0, 0, 0))
    arcade.draw_circle_filled(475, 595, 22, (0, 0, 0))
    arcade.draw_ellipse_filled(365, 363, 215, 69, (255, 0, 0))
    arcade.draw_arc_filled(356, 658, 264, 91, (0, 0, 0), 0, 180)


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
