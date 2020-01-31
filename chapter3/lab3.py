import arcade

screen_wid = 1000
screen_hei = 600
arcade.open_window(screen_wid, screen_hei, "lab3_example")


# Background color is light blue
arcade.set_background_color((102, 227, 205))


def draw_bird(x, y):
    arcade.draw_arc_outline(x, y, 20, 20, (34, 48, 254), 0, 90)
    arcade.draw_arc_outline(x+40, y, 20, 20, (34, 48, 254), 90, 180)

def draw_church(x, y):
    arcade.draw_lrtb_rectangle_filled(x, x+200, y+200, y, (171, 105, 53))
    arcade.draw_triangle_filled(x+100, y+350, x, y+200, x+200, y+200, (255, 0, 0))
    arcade.draw_lrtb_rectangle_filled(x+95, x+105, y+400, y+340, (197, 178, 141))
    arcade.draw_lrtb_rectangle_filled(x+80, x+120, y+380, y+375, (197, 178, 141))
    arcade.draw_lrtb_rectangle_filled(x+50, x+150, y+150, y, (38, 254, 34))
    arcade.draw_line(x+100, y, x+100, y+150, arcade.color.WOOD_BROWN, 2)

def draw_church_window(x, y):
    arcade.draw_lrtb_rectangle_filled(x+150, x+250, y+380, y+360, (230, 244, 0))
    arcade.draw_line(x+200, y+360, x+200, y+380, arcade.color.WOOD_BROWN, 1.5)
    arcade.draw_line(x+150, y+370, x+250, y+370, arcade.color.WOOD_BROWN, 1.5)
    arcade.draw_text("Belhaven Church", x+150, y+390, arcade.color.BLACK, 11.5)

def draw_tree(x, y):
    arcade.draw_lrtb_rectangle_filled(x, x+40, y+120, y, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x-10, y+140, 60, (81, 132, 86))
    arcade.draw_circle_filled(x+20, y+200, 60, (81, 132, 86))
    arcade.draw_circle_filled(x+50, y+140, 60, (81, 132, 86))


def draw_flower(x, y):
    arcade.draw_line(x, y, x, y+20, (54, 192, 67), 1.5)
    arcade.draw_circle_filled(x, y+25, 5, (241, 248, 95))

arcade.start_render()


# ground is 1/3 and it's color is green
arcade.draw_lrtb_rectangle_filled(0, screen_wid, 150, 0, (80, 114, 61))
arcade.draw_arc_filled(300, 150, 600, 100, (80, 114, 61), 0, 180)

#draw birds
draw_bird(50, 560)
draw_bird(450, 450)
draw_bird(570, 500)

#draw church
draw_church(100, 100)
draw_church_window(0, -30)

draw_tree(600, 150)
draw_tree(850, 60)

draw_flower(550, 100)
draw_flower(590, 100)
draw_flower(580, 80)
draw_flower(500, 90)
draw_flower(530, 120)
draw_flower(540, 95)
draw_flower(560, 125)
draw_flower(520, 90)
draw_flower(553, 80)

arcade.finish_render()
arcade.run()

