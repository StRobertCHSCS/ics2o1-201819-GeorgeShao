import arcade 
 
WIDTH = 800 
HEIGHT = 800 
 
 
def on_update(delta_time): 
    pass 
 
 
def on_draw(): 
    arcade.start_render() 
    # Drawing code here 
    arcade.draw_circle_filled(171, 552, -485, (255, 0, 0))
    arcade.draw_arc_filled(319, 515, 423, 212, (0, 0, 255), 180, 360)

 
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
