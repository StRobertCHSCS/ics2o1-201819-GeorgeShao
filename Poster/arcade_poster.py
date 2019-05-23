import arcade

WIDTH = 405
HEIGHT = 720


def on_update(delta_time):
    pass


class TextBubble():
    def __init__(self, text, side, y, w, h):
        self.text = text
        self.side = side
        self.y = y
        self.w = w
        self.h = h


bubbles = []

bubble_left_x = 50
bubble_right_x = 305
bubble_height = 30

bubbles.append(TextBubble("Hey, what's up?", "left", 50, 175, bubble_height))
bubbles.append(TextBubble("Nothing much...", "right", -25, 175, bubble_height))
bubbles.append(TextBubble("EXCEPT MY COMPUTER", "right", -50, 175, bubble_height))
bubbles.append(TextBubble("WAS HACKED!!!", "right", -75, 175, bubble_height))
bubbles.append(TextBubble("aw, that must suck", "left", -150, 175, bubble_height))
bubbles.append(TextBubble(":( yeah", "right", -225, 175, bubble_height))
bubbles.append(TextBubble("how'd u get the virus?", "left", -300, 175, bubble_height))
bubbles.append(TextBubble("well i was watching", "right", -375, 175, bubble_height))
bubbles.append(TextBubble("youtube, and there", "right", -400, 175, bubble_height))
bubbles.append(TextBubble("was an ad.", "right", -425, 175, bubble_height))
bubbles.append(TextBubble("And?", "left", -500, 175, bubble_height))
bubbles.append(TextBubble("The ad was for", "right", -575, 175, bubble_height))
bubbles.append(TextBubble("a free Minecraft account!", "right", -600, 175, bubble_height))
bubbles.append(TextBubble("Woah really?", "left", -675, 175, bubble_height))
bubbles.append(TextBubble("Well yes...", "right", -750, 175, bubble_height))
bubbles.append(TextBubble("but actually no.", "right", -775, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -800, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -825, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -850, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -875, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -900, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -925, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -950, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -975, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -1000, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -1025, 175, bubble_height))
bubbles.append(TextBubble(":(", "right", -1050, 175, bubble_height))

def on_draw():
    arcade.start_render()

    global bubbles

    for i in range(len(bubbles)):
        if bubbles[i].y > 20 and bubbles[i].y < 700:
            if bubbles[i].side == "left":
                arcade.draw_rectangle_filled(100, bubbles[i].y, bubbles[i].w, bubbles[i].h, (0, 118, 255))
                arcade.draw_text(bubbles[i].text, 25, bubbles[i].y - 5, arcade.color.WHITE, 12)
            elif bubbles[i].side == "right":
                arcade.draw_rectangle_filled(305, bubbles[i].y, bubbles[i].w, bubbles[i].h, (0, 118, 255))
                arcade.draw_text(bubbles[i].text, 230, bubbles[i].y - 5, arcade.color.WHITE, 12)
        bubbles[i].y += 5


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Malware Prevention Poster - George Shao")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/120)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
