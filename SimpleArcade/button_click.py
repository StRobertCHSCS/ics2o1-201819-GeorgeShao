"""
Button Click

1. Figure out how you want to represent a button. Create global variable(s) for it.
2. Draw the button using the information stored in the button's variable(s).
3. In the on_mouse_press function, compare the mouse x and mouse y values to the
   values of the button to determine if there was a click or not.
"""

import arcade


WIDTH = 640
HEIGHT = 480

# There are better ways to represent buttons
my_button = [100, 200, 150, 50]  # x, y, width, height
button_pressed = False

def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    if button_pressed:
        color = arcade.color.ASH_GREY
    else:
        color = arcade.color.BLACK
    # Draw in here...
    arcade.draw_xywh_rectangle_filled(my_button[0],
                                      my_button[1],
                                      my_button[2],
                                      my_button[3],
                                      color)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    # unpack the button list into readable? variables.
    my_button_x, my_button_y, my_button_w, my_button_h = my_button
    global button_pressed

    # Need to check all four limits of the button.
    if (x > my_button_x and x < my_button_x + my_button_w and
            y > my_button_y and y < my_button_y + my_button_h):
        print("Clicked!!!")
        button_pressed = True
    else:
        print("not clicked")
        button_pressed = False

def on_mouse_release(x, y, button, modifiers):
    my_button_x, my_button_y, my_button_w, my_button_h = my_button
    global button_pressed

    if (x > my_button_x and x < my_button_x + my_button_w and
            y > my_button_y and y < my_button_y + my_button_h):
        print("Released!!!")
        button_pressed = False
    else:
        print("not clicked")
        button_pressed = False


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
    window.on_mouse_release = on_mouse_release

    arcade.run()


if __name__ == '__main__':
    setup()
