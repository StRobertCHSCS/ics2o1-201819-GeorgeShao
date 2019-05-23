import arcade

WIDTH = 405
HEIGHT = 720

continue_messages = True

def on_update(delta_time):
    pass


class TextBubble():
    def __init__(self, text, side, y):
        self.text = text
        self.side = side
        self.y = y


bubbles = []

bubbles.append(TextBubble("Hey, what's up?", "left", 50))
bubbles.append(TextBubble("Nothing much...", "right", -25))
bubbles.append(TextBubble("EXCEPT MY COMPUTER", "right", -50))
bubbles.append(TextBubble("WAS HACKED!!!", "right", -75))
bubbles.append(TextBubble("aw, that must suck", "left", -150))
bubbles.append(TextBubble(":( yeah", "right", -225))
bubbles.append(TextBubble("how'd u get the virus?", "left", -300))
bubbles.append(TextBubble("well i was watching", "right", -375))
bubbles.append(TextBubble("youtube, and there", "right", -400))
bubbles.append(TextBubble("was an ad.", "right", -425))
bubbles.append(TextBubble("And?", "left", -500))
bubbles.append(TextBubble("The ad was for", "right", -575))
bubbles.append(TextBubble("a free Minecraft account!", "right", -600))
bubbles.append(TextBubble("Woah really?", "left", -675))
bubbles.append(TextBubble("Well yes...", "right", -750))
bubbles.append(TextBubble("but actually no.", "right", -775))
bubbles.append(TextBubble(":(", "right", -800))
bubbles.append(TextBubble(":(", "right", -825))
bubbles.append(TextBubble(":(", "right", -850))
bubbles.append(TextBubble(":(", "right", -875))
bubbles.append(TextBubble("ok, ok", "left", -950))
bubbles.append(TextBubble("STOP SPAMMING!", "left", -975))
bubbles.append(TextBubble("fine", "right", -1050))
bubbles.append(TextBubble("anyways...", "right", -1075))
bubbles.append(TextBubble("so I clicked", "right", -1100))
bubbles.append(TextBubble("on the ad.", "right", -1125))
bubbles.append(TextBubble("k", "left", -1200))
bubbles.append(TextBubble("it downloaded a file", "right", -1275))
bubbles.append(TextBubble("it was called:", "right", -1300))
bubbles.append(TextBubble("RealMinecraftNoBS.exe", "right", -1325))
bubbles.append(TextBubble("well, there's your", "left", -1400))
bubbles.append(TextBubble("problem", "left", -1425))
bubbles.append(TextBubble("what?!?!", "right", -1500))
bubbles.append(TextBubble("u downloaded malware!", "left", -1575))
bubbles.append(TextBubble("SH*T!", "right", -1650))
bubbles.append(TextBubble("wait, what's malware?", "right", -1675))
bubbles.append(TextBubble("malware is software", "left", -1750))
bubbles.append(TextBubble("that intentionally", "left", -1775))
bubbles.append(TextBubble("causes damage to", "left", -1800))
bubbles.append(TextBubble("your computer!", "left", -1825))
bubbles.append(TextBubble("k", "right", -1900))
bubbles.append(TextBubble("but how do i get", "right", -1925))
bubbles.append(TextBubble("rid of it?", "right", -1950))
bubbles.append(TextBubble("Well, the best way to", "left", -2025))
bubbles.append(TextBubble("remove malware from", "left", -2050))
bubbles.append(TextBubble("ur computer is to", "left", -2075))
bubbles.append(TextBubble("install an antivirus", "left", -2100))
bubbles.append(TextBubble("Ok, i'll do that", "right", -2175))
bubbles.append(TextBubble("but how do i stop", "right", -2200))
bubbles.append(TextBubble("myself from getting", "right", -2225))
bubbles.append(TextBubble("malware later?", "right", -2250))
bubbles.append(TextBubble("just dont go to", "left", -2325))
bubbles.append(TextBubble("sketchy websites", "left", -2350))
bubbles.append(TextBubble("k yea?", "right", -2425))
bubbles.append(TextBubble("and dont download", "left", -2500))
bubbles.append(TextBubble("random stuff u see", "left", -2525))
bubbles.append(TextBubble("on the internet", "left", -2550))
bubbles.append(TextBubble("kk aight", "right", -2625))
bubbles.append(TextBubble("REMEMBER:", "left", -2700))
bubbles.append(TextBubble("Antiviruses... ", "left", -2725))
bubbles.append(TextBubble("he detecc,", "left", -2750))
bubbles.append(TextBubble("he protecc", "left", -2775))
bubbles.append(TextBubble("but most importantly", "left", -2800))
bubbles.append(TextBubble("he make sure u no infecc!", "left", -2825))
bubbles.append(TextBubble("lol ok, gud meme", "right", -2900))
bubbles.append(TextBubble("well cya", "left", -2975))
bubbles.append(TextBubble("gl on getting rid", "left", -3000))
bubbles.append(TextBubble("of that malware", "left", -3025))
bubbles.append(TextBubble("kthx bye", "right", -3075))


def on_draw():
    arcade.start_render()

    global bubbles, continue_messages

    arcade.draw_rectangle_filled(WIDTH/2, HEIGHT - 25, WIDTH, 50, (230, 230, 230))
    arcade.draw_text("Mr. Thanos", WIDTH/2 - 50, HEIGHT - 35, arcade.color.BLACK, font_size=20)
    profile_pic = arcade.load_texture("Thanos.jpg")
    arcade.draw_texture_rectangle(WIDTH/2 - 80, HEIGHT - 25, 30, 35, profile_pic)

    for i in range(len(bubbles)):
        if 20 < bubbles[i].y < 650:
            if bubbles[i].side == "left":
                arcade.draw_rectangle_filled(100, bubbles[i].y, 175, 30, (229, 229, 229))
                arcade.draw_text(bubbles[i].text, 25, bubbles[i].y - 5, arcade.color.BLACK, 12)
            elif bubbles[i].side == "right":
                arcade.draw_rectangle_filled(305, bubbles[i].y, 175, 30, (0, 118, 255))
                arcade.draw_text(bubbles[i].text, 230, bubbles[i].y - 5, arcade.color.WHITE, 12)
                if bubbles[i].text == "kthx bye":
                    continue_messages = False

        if continue_messages:
            bubbles[i].y += 5


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Malware Prevention Poster - George Shao")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/120)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw

    arcade.run()


if __name__ == '__main__':
    setup()
