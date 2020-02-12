import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

def draw_background():
    arcade.set_background_color((8, 73, 185))
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT/3, 0, (2, 178, 199))

def draw_snowman(x, y):
    #snowman body
    arcade.draw_circle_filled(x, y, 60, arcade.color.WHITE)
    arcade.draw_circle_outline(x, y, 60, (244, 236, 202), 3)
    arcade.draw_circle_filled(x, y + 80, 50, arcade.color.WHITE)
    arcade.draw_circle_outline(x, y + 80, 50, (244, 236, 202), 3)
    arcade.draw_circle_filled(x, y + 140, 40, arcade.color.WHITE)
    arcade.draw_circle_outline(x, y + 140, 40, (244, 236, 202), 3)

    #snowman eyes
    arcade.draw_circle_filled(x - 15, y + 150, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, y + 150, 5, arcade.color.BLACK)

positions = {
    "snowmen": [
        [100, 200]
        [300, 300]
        [400, 100]
    ]
}

def on_draw(delta_time):
    arcade.start_render()
    s1 = snowmen[0]
    s2 = snowmen[1]
    s3 = snowmen[2]
    s1x, s1y = s1
    s2x, s2y = s2
    s3x, s3y = s3

    daw_snowmen(positinos["x"], positions["y"])

    positions["x"] += 1


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Snowman")

    draw_background()
    draw_snowman(300, 200)
    draw_snowman(500, 300)

    arcade.schedule(on_draw, 1/60)

    arcade.run()

if __name__ == '__main__':
    main()