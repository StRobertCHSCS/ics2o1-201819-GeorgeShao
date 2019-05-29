import arcade
import pymsgbox

# Window width & height
WIDTH = 900
HEIGHT = 800

# Chosen color & shape row & column variables
chosen_color_row = 0
chosen_color_column = 0
chosen_shape_row = 0
chosen_shape_column = 0

# In-the-moment drawing variables
currently_drawing = False
start_x = 0
start_y = 0
end_x = 0
end_y = 0

# Shape object lists
rectangles_filled = []
rectangles_outline = []
circle_filled = []
circle_outline = []
ellipse_filled = []
ellipse_outline = []
triangle_filled = []
triangle_outline = []
arc_top_filled = []
arc_top_outline = []
arc_bottom_filled = []
arc_bottom_outline = []
line_thick = []
line_thin = []


# Shape objects
class RectangleFilled:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        if self.x <= self.x1:
            if self.y <= self.y1:
                arcade.draw_lrtb_rectangle_filled(self.x, self.x1, self.y1, self.y, self.color)
            elif self.y1 < self.y:
                arcade.draw_lrtb_rectangle_filled(self.x, self.x1, self.y, self.y1, self.color)
        elif self.x1 < self.x:
            if self.y <= self.y1:
                arcade.draw_lrtb_rectangle_filled(self.x1, self.x, self.y1, self.y, self.color)
            elif self.y1 < self.y:
                arcade.draw_lrtb_rectangle_filled(self.x1, self.x, self.y, self.y1, self.color)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        if self.x <= self.x1:
            if self.y <= self.y1:
                return "arcade.draw_lrtb_rectangle_filled(" + str(self.x)+ ", " + str(self.x1) + ", " + str(self.y1) + ", " + str(self.y) + ", " + str(self.color) + ")"
            elif self.y1 < self.y:
                return "arcade.draw_lrtb_rectangle_filled(" + str(self.x) + ", " + str(self.x1) + ", " + str(self.y) + ", " + str(self.y1) + ", " + str(self.color) + ")"
        elif self.x1 < self.x:
            if self.y <= self.y1:
                return "arcade.draw_lrtb_rectangle_filled(" + str(self.x1) + ", " + str(self.x) + ", " + str(self.y1) + ", " + str(self.y) + ", " + str(self.color) + ")"
            elif self.y1 < self.y:
                return "arcade.draw_lrtb_rectangle_filled(" + str(self.x1) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.y1) + ", " + str(self.color) + ")"


class RectangleOutline:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        if self.x <= self.x1:
            if self.y <= self.y1:
                arcade.draw_lrtb_rectangle_outline(self.x, self.x1, self.y1, self.y, self.color)
            elif self.y1 < self.y:
                arcade.draw_lrtb_rectangle_outline(self.x, self.x1, self.y, self.y1, self.color)
        elif self.x1 < self.x:
            if self.y <= self.y1:
                arcade.draw_lrtb_rectangle_outline(self.x1, self.x, self.y1, self.y, self.color)
            elif self.y1 < self.y:
                arcade.draw_lrtb_rectangle_outline(self.x1, self.x, self.y, self.y1, self.color)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        if self.x <= self.x1:
            if self.y <= self.y1:
                return "arcade.draw_lrtb_rectangle_outline(" + str(self.x)+ ", " + str(self.x1) + ", " + str(self.y1) + ", " + str(self.y) + ", " + str(self.color) + ")"
            elif self.y1 < self.y:
                return "arcade.draw_lrtb_rectangle_outline(" + str(self.x) + ", " + str(self.x1) + ", " + str(self.y) + ", " + str(self.y1) + ", " + str(self.color) + ")"
        elif self.x1 < self.x:
            if self.y <= self.y1:
                return "arcade.draw_lrtb_rectangle_outline(" + str(self.x1) + ", " + str(self.x) + ", " + str(self.y1) + ", " + str(self.y) + ", " + str(self.color) + ")"
            elif self.y1 < self.y:
                return "arcade.draw_lrtb_rectangle_outline(" + str(self.x1) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.y1) + ", " + str(self.color) + ")"


class CircleFilled:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        radius = 0
        if abs(self.x1 - self.x) >= abs(self.y1 - self.y):
            radius = self.x1 - self.x
        elif abs(self.x1 - self.x) < abs(self.y1 - self.y):
            radius = self.y1 - self.y
        arcade.draw_circle_filled(self.x, self.y, radius, self.color)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        radius = 0
        if abs(self.x1 - self.x) >= abs(self.y1 - self.y):
            radius = self.x1 - self.x
        elif abs(self.x1 - self.x) < abs(self.y1 - self.y):
            radius = self.y1 - self.y
        return "arcade.draw_circle_filled(" + str(self.x)+ ", " + str(self.y) + ", " + str(radius) + ", " + str(self.color) + ")"


class CircleOutline:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        radius = 0
        if abs(self.x1 - self.x) >= abs(self.y1 - self.y):
            radius = self.x1 - self.x
        elif abs(self.x1 - self.x) < abs(self.y1 - self.y):
            radius = self.y1 - self.y
        arcade.draw_circle_outline(self.x, self.y, radius, self.color)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        radius = 0
        if abs(self.x1 - self.x) >= abs(self.y1 - self.y):
            radius = self.x1 - self.x
        elif abs(self.x1 - self.x) < abs(self.y1 - self.y):
            radius = self.y1 - self.y
        return "arcade.draw_circle_outline(" + str(self.x)+ ", " + str(self.y) + ", " + str(radius) + ", " + str(self.color) + ")"


class EllipseFilled:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_ellipse_filled(self.x, self.y, int(abs(self.x1-self.x)), int(abs(self.y1-self.y)), self.color)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_ellipse_filled(" + str(self.x) + ", " + str(self.y) + ", " + str(int(abs(self.x1-self.x))) + ", " + str(int(abs(self.y1-self.y))) + ", " + str(self.color) + ")"


class EllipseOutline:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_ellipse_outline(self.x, self.y, int(abs(self.x1-self.x)), int(abs(self.y1-self.y)), self.color)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_ellipse_outline(" + str(self.x) + ", " + str(self.y) + ", " + str(int(abs(self.x1-self.x))) + ", " + str(int(abs(self.y1-self.y))) + ", " + str(self.color) + ")"


class TriangleFilled:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_triangle_filled(self.x, self.y, self.x1, self.y1, self.x - (self.x1 - self.x), self.y1, self.color)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_triangle_filled(" + str(self.x) + ", " + str(self.y) + ", " + str(self.x1) + ", " + str(self.y1) + ", " + str(int(self.x - (self.x1 - self.x))) + ", " + str(self.y1) + ", " + str(self.color) + ")"


class TriangleOutline:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_triangle_outline(self.x, self.y, self.x1, self.y1, self.x - (self.x1 - self.x), self.y1, self.color)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_triangle_outline(" + str(self.x) + ", " + str(self.y) + ", " + str(self.x1) + ", " + str(self.y1) + ", " + str(int(self.x - (self.x1 - self.x))) + ", " + str(self.y1) + ", " + str(self.color) + ")"


class ArcTopFilled:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_arc_filled(self.x, self.y, int(abs(self.x1 - self.x)), int(abs(self.y1 - self.y)), self.color, 0, 180)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_arc_filled(" + str(self.x) + ", " + str(self.y) + ", " + str(int(abs(self.x1 - self.x))) + ", " + str(int(abs(self.y1 - self.y))) + ", " + str(self.color) + ", 0, 180)"


class ArcTopOutline:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_arc_outline(self.x, self.y, int(abs(self.x1 - self.x)), int(abs(self.y1 - self.y)), self.color, 0, 180)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_arc_outline(" + str(self.x) + ", " + str(self.y) + ", " + str(int(abs(self.x1 - self.x))) + ", " + str(int(abs(self.y1 - self.y))) + ", " + str(self.color) + ", 0, 180)"


class ArcBottomFilled:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_arc_filled(self.x, self.y, int(abs(self.x1 - self.x)), int(abs(self.y1 - self.y)), self.color, 180, 360)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_arc_filled(" + str(self.x) + ", " + str(self.y) + ", " + str(int(abs(self.x1 - self.x))) + ", " + str(int(abs(self.y1 - self.y))) + ", " + str(self.color) + ", 180, 360)"


class ArcBottomOutline:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_arc_outline(self.x, self.y, int(abs(self.x1 - self.x)), int(abs(self.y1 - self.y)), self.color, 180, 360)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_arc_outline(" + str(self.x) + ", " + str(self.y) + ", " + str(int(abs(self.x1 - self.x))) + ", " + str(int(abs(self.y1 - self.y))) + ", " + str(self.color) + ", 180, 360)"


class LineThick:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_line(self.x, self.y, self.x1, self.y1, self.color, line_width=5)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_line(" + str(self.x) + ", " + str(self.y) + ", " + str(self.x1) + ", " + str(self.y1) + ", " + str(self.color) + ", line_width=5)"


class LineThin:
    def __init__(self, x, y, x1, y1, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw_shape(self):
        arcade.draw_line(self.x, self.y, self.x1, self.y1, self.color, line_width=2)

    def create_code(self):
        self.x -= 100
        self.x1 -= 100
        return "arcade.draw_line(" + str(self.x) + ", " + str(self.y) + ", " + str(self.x1) + ", " + str(self.y1) + ", " + str(self.color) + ", line_width=2)"


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()

    global rectangles_filled, rectangles_outline, circle_filled, circle_outline, ellipse_filled, ellipse_outline, triangle_filled, triangle_outline, arc_top_filled, arc_top_outline, arc_bottom_filled, arc_bottom_outline, line_thick, line_thin

    # Renders all the drawn shapes
    for i in range(len(rectangles_filled)):
        RectangleFilled.draw_shape(rectangles_filled[i])
    for i in range(len(rectangles_outline)):
        RectangleOutline.draw_shape(rectangles_outline[i])
    for i in range(len(circle_filled)):
        CircleFilled.draw_shape(circle_filled[i])
    for i in range(len(circle_outline)):
        CircleOutline.draw_shape(circle_outline[i])
    for i in range(len(ellipse_filled)):
        EllipseFilled.draw_shape(ellipse_filled[i])
    for i in range(len(ellipse_outline)):
        EllipseOutline.draw_shape(ellipse_outline[i])
    for i in range(len(triangle_filled)):
        TriangleFilled.draw_shape(triangle_filled[i])
    for i in range(len(triangle_outline)):
        TriangleOutline.draw_shape(triangle_outline[i])
    for i in range(len(arc_top_filled)):
        ArcTopFilled.draw_shape(arc_top_filled[i])
    for i in range(len(arc_top_outline)):
        ArcTopOutline.draw_shape(arc_top_outline[i])
    for i in range(len(arc_bottom_filled)):
        ArcBottomFilled.draw_shape(arc_bottom_filled[i])
    for i in range(len(arc_bottom_outline)):
        ArcBottomOutline.draw_shape(arc_bottom_outline[i])
    for i in range(len(line_thick)):
        LineThick.draw_shape(line_thick[i])
    for i in range(len(line_thin)):
        LineThin.draw_shape(line_thin[i])

    # Renders toolbar
    draw_toolbar_dividers()
    draw_toolbar_shapes()
    draw_toolbar_colors()


def draw_toolbar_dividers():
    # Draw toolbar outline
    arcade.draw_xywh_rectangle_filled(0, 0, 100, 800, arcade.color.TROLLEY_GREY)  # background
    arcade.draw_line(100, 0, 100, 800, arcade.color.BLACK)  # right border
    arcade.draw_line(1, 1, 1, 800, arcade.color.BLACK)  # left border
    arcade.draw_line(0, 0, 100, 0, arcade.color.BLACK)  # bottom border
    arcade.draw_line(1, 799, 100, 799, arcade.color.BLACK)  # top border

    # Draw toolbar divider
    arcade.draw_line(50, 0, 50, 750, arcade.color.BLACK)  # middle divider

    # Draw toolbar mini dividers
    for i in range(0, 800, 50):
        arcade.draw_line(0, i, 100, i, arcade.color.BLACK)


def draw_toolbar_shapes():
    # Export button
    arcade.draw_text("EXPORT", 15, 765, arcade.color.BLACK, font_size=18)

    # Draw rectangles
    arcade.draw_rectangle_filled(25, 725, 35, 15, arcade.color.BLUE)
    arcade.draw_rectangle_outline(75, 725, 35, 15, arcade.color.BLUE)

    # Draw circles
    arcade.draw_circle_filled(25, 675, 13, arcade.color.BLUE)
    arcade.draw_circle_outline(75, 675, 13, arcade.color.BLUE)

    # Draw ellipses
    arcade.draw_ellipse_filled(25, 625, 18, 8, arcade.color.BLUE)
    arcade.draw_ellipse_outline(75, 625, 18, 8, arcade.color.BLUE)

    # Draw triangles
    arcade.draw_triangle_filled(25, 590, 10, 560, 40, 560, arcade.color.BLUE)
    arcade.draw_triangle_outline(75, 590, 60, 560, 90, 560, arcade.color.BLUE)

    # Draw arc tops (to symbolize arc tops & bottoms)
    arcade.draw_arc_filled(25, 520, 15, 15, arcade.color.BLUE, 0, 180)
    arcade.draw_arc_outline(75, 520, 15, 15, arcade.color.BLUE, 0, 180)

    # Draw lines
    arcade.draw_line(10, 460, 40, 490, arcade.color.BLUE, line_width=2)
    arcade.draw_line(60, 460, 90, 490, arcade.color.BLUE, line_width=1)


def draw_toolbar_colors():
    # First column of colors
    arcade.draw_rectangle_filled(25, 425, 50, 50, arcade.color.RED)
    arcade.draw_rectangle_filled(25, 375, 50, 50, arcade.color.ORANGE)
    arcade.draw_rectangle_filled(25, 325, 50, 50, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(25, 275, 50, 50, arcade.color.GREEN)
    arcade.draw_rectangle_filled(25, 225, 50, 50, arcade.color.BLUE)
    arcade.draw_rectangle_filled(25, 175, 50, 50, arcade.color.PURPLE)
    arcade.draw_rectangle_filled(25, 125, 50, 50, arcade.color.VIOLET)
    arcade.draw_rectangle_filled(25, 75, 50, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(25, 25, 50, 50, arcade.color.BLACK)

    # Second column of colors
    arcade.draw_rectangle_filled(75, 425, 50, 50, arcade.color.RED_ORANGE)
    arcade.draw_rectangle_filled(75, 375, 50, 50, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_rectangle_filled(75, 325, 50, 50, arcade.color.FLUORESCENT_YELLOW)
    arcade.draw_rectangle_filled(75, 275, 50, 50, arcade.color.YELLOW_GREEN)
    arcade.draw_rectangle_filled(75, 225, 50, 50, arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.draw_rectangle_filled(75, 175, 50, 50, arcade.color.FUCHSIA_PURPLE)
    arcade.draw_rectangle_filled(75, 125, 50, 50, arcade.color.BLUE_VIOLET)
    arcade.draw_rectangle_filled(75, 75, 50, 50, arcade.color.WHITE_SMOKE)
    arcade.draw_rectangle_filled(75, 25, 50, 50, arcade.color.ASH_GREY)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global chosen_color_column, chosen_shape_column, chosen_color_row, chosen_shape_row
    global currently_drawing, start_x, start_y, end_x, end_y

    # choosing color & shape row * column
    if 450 <= y <= 750:
        if x <= 50:
            for i in range(500, 800, 50):
                if y <= i:
                    chosen_shape_row = i/50
                    chosen_shape_column = 1
                    break
        elif x <= 100:
            for i in range(500, 800, 50):
                if y <= i:
                    chosen_shape_row = i/50
                    chosen_shape_column = 2
                    break
    elif y <= 450:
        if x <= 50:
            for i in range(0, 500, 50):
                if y <= i:
                    chosen_color_row = i/50
                    chosen_color_column = 1
                    break
        elif x <= 100:
            for i in range(0, 500, 50):
                if y <= i:
                    chosen_color_row = i/50
                    chosen_color_column = 2
                    break

    if x > 100:
        currently_drawing = True
        start_x = x
        start_y = y


def on_mouse_release(x, y, button, modifiers):
    global chosen_color_column, chosen_shape_column, chosen_color_row, chosen_shape_row, color, history_num
    global currently_drawing, start_x, start_y, end_x, end_y
    global rectangles_filled, rectangles_outline, circle_filled, circle_outline, ellipse_filled, ellipse_outline, triangle_filled, triangle_outline, arc_top_filled, arc_top_outline, arc_bottom_filled, arc_bottom_outline, line_thick, line_thin

    if x > 100:
        currently_drawing = False
        end_x = x
        end_y = y
        color = None

        # Determines what color user has chosen
        if chosen_color_column == 1:
            if chosen_color_row == 1:
                color = arcade.color.BLACK
            if chosen_color_row == 2:
                color = arcade.color.WHITE
            if chosen_color_row == 3:
                color = arcade.color.VIOLET
            if chosen_color_row == 4:
                color = arcade.color.PURPLE
            if chosen_color_row == 5:
                color = arcade.color.BLUE
            if chosen_color_row == 6:
                color = arcade.color.GREEN
            if chosen_color_row == 7:
                color = arcade.color.YELLOW
            if chosen_color_row == 8:
                color = arcade.color.ORANGE
            if chosen_color_row == 9:
                color = arcade.color.RED
        if chosen_color_column == 2:
            if chosen_color_row == 1:
                color = arcade.color.ASH_GREY
            if chosen_color_row == 2:
                color = arcade.color.WHITE_SMOKE
            if chosen_color_row == 3:
                color = arcade.color.BLUE_VIOLET
            if chosen_color_row == 4:
                color = arcade.color.FUCHSIA_PURPLE
            if chosen_color_row == 5:
                color = arcade.color.AIR_SUPERIORITY_BLUE
            if chosen_color_row == 6:
                color = arcade.color.YELLOW_GREEN
            if chosen_color_row == 7:
                color = arcade.color.FLUORESCENT_YELLOW
            if chosen_color_row == 8:
                color = arcade.color.FLUORESCENT_ORANGE
            if chosen_color_row == 9:
                color = arcade.color.RED_ORANGE

        # Determines & adds shape to object list
        if chosen_shape_column == 1:
            if chosen_shape_row == 15:
                rectangles_filled.append(RectangleFilled(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 14:
                circle_filled.append(CircleFilled(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 13:
                ellipse_filled.append(EllipseFilled(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 12:
                triangle_filled.append(TriangleFilled(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 11:
                if end_y >= start_y:
                    arc_top_filled.append(ArcTopFilled(start_x, start_y, end_x, end_y, color))
                elif end_y < start_y:
                    arc_bottom_filled.append(ArcBottomFilled(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 10:
                line_thick.append(LineThick(start_x, start_y, end_x, end_y, color))

        if chosen_shape_column == 2:
            if chosen_shape_row == 15:
                rectangles_outline.append(RectangleOutline(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 14:
                circle_outline.append(CircleOutline(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 13:
                ellipse_outline.append(EllipseOutline(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 12:
                triangle_outline.append(TriangleOutline(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 11:
                if end_y >= start_y:
                    arc_top_outline.append(ArcTopOutline(start_x, start_y, end_x, end_y, color))
                elif end_y < start_y:
                    arc_bottom_outline.append(ArcBottomOutline(start_x, start_y, end_x, end_y, color))
            if chosen_shape_row == 10:
                line_thin.append(LineThin(start_x, start_y, end_x, end_y, color))

    elif x < 100 and 750 < y < 800:
        # Exports PyArcade python code into Exported_Code.py file
        with open('Exported_Code.py', 'w') as writer:

            writer.write("import arcade \n \n")
            writer.write("WIDTH = 800 \n")
            writer.write("HEIGHT = 800 \n \n \n")
            writer.write("def on_update(delta_time): \n")
            writer.write("    pass \n \n \n")
            writer.write("def on_draw(): \n")
            writer.write("    arcade.start_render() \n")
            writer.write("    # Drawing code here \n")

            for i in range(len(rectangles_filled)):
                writer.write("    " + RectangleFilled.create_code(rectangles_filled[i]) + "\n")
                rectangles_filled[i].x += 100
                rectangles_filled[i].x1 += 100
            for i in range(len(rectangles_outline)):
                writer.write("    " + RectangleOutline.create_code(rectangles_outline[i]) + "\n")
                rectangles_outline[i].x += 100
                rectangles_outline[i].x1 += 100
            for i in range(len(circle_filled)):
                writer.write("    " + CircleFilled.create_code(circle_filled[i]) + "\n")
                circle_filled[i].x += 100
                circle_filled[i].x1 += 100
            for i in range(len(circle_outline)):
                writer.write("    " + CircleOutline.create_code(circle_outline[i]) + "\n")
                circle_outline[i].x += 100
                circle_outline[i].x1 += 100
            for i in range(len(ellipse_filled)):
                writer.write("    " + EllipseFilled.create_code(ellipse_filled[i]) + "\n")
                ellipse_filled[i].x += 100
                ellipse_filled[i].x1 += 100
            for i in range(len(ellipse_outline)):
                writer.write("    " + EllipseOutline.create_code(ellipse_outline[i]) + "\n")
                ellipse_outline[i].x += 100
                ellipse_outline[i].x1 += 100
            for i in range(len(triangle_filled)):
                writer.write("    " + TriangleFilled.create_code(triangle_filled[i]) + "\n")
                triangle_filled[i].x += 100
                triangle_filled[i].x1 += 100
            for i in range(len(triangle_outline)):
                writer.write("    " + TriangleOutline.create_code(triangle_outline[i]) + "\n")
                triangle_outline[i].x += 100
                triangle_outline[i].x1 += 100
            for i in range(len(arc_top_filled)):
                writer.write("    " + ArcTopFilled.create_code(arc_top_filled[i]) + "\n")
                arc_top_filled[i].x += 100
                arc_top_filled[i].x1 += 100
            for i in range(len(arc_top_outline)):
                writer.write("    " + ArcTopOutline.create_code(arc_top_outline[i]) + "\n")
                arc_top_outline[i].x += 100
                arc_top_outline[i].x1 += 100
            for i in range(len(arc_bottom_filled)):
                writer.write("    " + ArcBottomFilled.create_code(arc_bottom_filled[i]) + "\n")
                arc_bottom_filled[i].x += 100
                arc_bottom_filled[i].x1 += 100
            for i in range(len(arc_bottom_outline)):
                writer.write("    " + ArcBottomOutline.create_code(arc_bottom_outline[i]) + "\n")
                arc_bottom_outline[i].x += 100
                arc_bottom_outline[i].x1 += 100
            for i in range(len(line_thick)):
                writer.write("    " + LineThick.create_code(line_thick[i]) + "\n")
                line_thick[i].x += 100
                line_thick[i].x1 += 100
            for i in range(len(line_thin)):
                writer.write("    " + LineThin.create_code(line_thin[i]) + "\n")
                line_thin[i].x += 100
                line_thin[i].x1 += 100

            writer.write("\n \n")
            writer.write("def on_key_press(key, modifiers): \n")
            writer.write("    pass \n \n \n")
            writer.write("def on_key_release(key, modifiers): \n")
            writer.write("    pass \n \n \n")
            writer.write("def on_mouse_press(x, y, button, modifiers): \n")
            writer.write("    pass \n \n \n")
            writer.write("def setup(): \n")
            writer.write("    arcade.open_window(WIDTH, HEIGHT, \"My Arcade Game\") \n")
            writer.write("    arcade.set_background_color(arcade.color.WHITE) \n")
            writer.write("    arcade.schedule(on_update, 1/60) \n")
            writer.write("    # Override arcade window methods \n")
            writer.write("    window = arcade.get_window() \n")
            writer.write("    window.on_draw = on_draw \n")
            writer.write("    window.on_key_press = on_key_press \n")
            writer.write("    window.on_key_release = on_key_release \n")
            writer.write("    window.on_mouse_press = on_mouse_press \n")
            writer.write("    arcade.run() \n \n \n")
            writer.write("if __name__ == '__main__': \n")
            writer.write("    setup() \n")

        chosen_color_column = 0
        chosen_color_row = 0
        chosen_shape_column = 0
        chosen_shape_row = 0

        pymsgbox.alert(text='You exported the drawing as Python Arcade code in Exported_Code.py in this project\'s folder. Run it and your drawing should appear. See the README.md on my GitHub repo for more details.', title='Successfully Exported!')


def setup():
    arcade.open_window(WIDTH, HEIGHT, "PyArcadePaint")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/30)

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
