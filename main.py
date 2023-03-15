import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Dessin d'une maison"


def nature():
    arcade.draw_arc_filled(150, 100 / 2 + 140, 210, 460, arcade.csscolor.DARK_OLIVE_GREEN, 0, 180)
    arcade.draw_rectangle_filled(400, 100, 800, 200, arcade.color.INDIA_GREEN)
    arcade.draw_circle_filled(200, 227, 30, arcade.color.DARK_GREEN, num_segments=8, tilt_angle=23)
    arcade.draw_circle_filled(100, 500, 80, arcade.color.ELECTRIC_YELLOW)
    arcade.draw_ellipse_filled(400, 150, 100, 75, arcade.color.DARK_CYAN)


def car():
    arcade.draw_rectangle_filled(400, 250, 150, 50, arcade.color.REDWOOD)
    arcade.draw_rectangle_filled(400, 280, 80, 100, arcade.color.REDWOOD)
    arcade.draw_circle_filled(350, 220, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(450, 220, 30, arcade.color.BLACK)


def house():
    arcade.draw_triangle_filled(610, + 420, 715, + 300, 500, + 300, arcade.color.RED)
    arcade.draw_rectangle_filled(610, 250, 200, 100, arcade.color.DARK_BROWN)
    arcade.draw_line(SCREEN_WIDTH - 00, SCREEN_HEIGHT - 30, SCREEN_WIDTH, SCREEN_HEIGHT - 19, arcade.color.SKY_BLUE, 10)
    arcade.draw_text("it's a house.", 450, 500, arcade.color.BARBIE_PINK)


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
arcade.set_background_color(arcade.color.BLUEBERRY)

arcade.start_render()

car()
nature()
house()
arcade.finish_render()

arcade.run()
