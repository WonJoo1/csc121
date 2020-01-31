import arcade

screen_wid = 600
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

arcade.finish_render()
arcade.run()

