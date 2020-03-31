import arcade

def draw_section_outlines():
    
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLUE)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLUE)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLUE)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLUE)

    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLUE)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLUE)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLUE)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLUE)
    
def draw_section_1(x, y):
    i = x + 2.5
    j = y - 2.5
    for row in range(30):
        for column in range(30):
            arcade.draw_lrtb_rectangle_filled(i , i + 5, j,  j - 5, arcade.color.WHITE)
            i += 10
        i = x + 2.5
        j -= 10

def draw_section_2(x, y):
    i = x + 2.5
    j = y - 2.5
    for row in range(30):
        for column in range(15):
            arcade.draw_lrtb_rectangle_filled(i, i + 5, j, j - 5, arcade.color.WHITE)
            i += 20
        i = x + 2.5
        j -= 10

    i = x + 2.5
    j = y - 2.5
    for row in range(30):
        for column in range(15):
            arcade.draw_lrtb_rectangle_filled(i + 10, i + 15, j, j - 5, arcade.color.BLACK)
            i += 20
        i = x + 2.5
        j -= 10


def draw_section_3(x, y):
    i = x + 2.5
    j = y - 2.5
    for row in range(15):
        for column in range(30):
            arcade.draw_lrtb_rectangle_filled(i, i + 5, j, j - 5, arcade.color.BLACK)
            i += 10
        i = x + 2.5
        j -= 20
    
    i = x + 2.5
    j = y - 2.5
    for row in range(15):
        for column in range(30):
            arcade.draw_lrtb_rectangle_filled(i, i + 5, j - 10, j - 15, arcade.color.WHITE)
            i += 10
        i = x + 2.5
        j -= 20    

def draw_section_4(x, y):
    i = x + 2.5
    j = y - 2.5
    for row in range(15):
        for column in range(30):
            arcade.draw_lrtb_rectangle_filled(i, i + 5, j, j - 5, arcade.color.BLACK)
            i += 10
        i = x + 2.5
        j -= 20
    
    i = x + 2.5
    j = y - 2.5
    for row in range(15):
        for column in range(15):
            arcade.draw_lrtb_rectangle_filled(i + 0, i+5, j-10, j-15, arcade.color.WHITE)
            arcade.draw_lrtb_rectangle_filled(i + 10, i + 15, j-10, j-15, arcade.color.BLACK)
            i += 20
        i = x + 2.5
        j -= 20


def draw_section_5(x, y):
    i = x + 2.5
    j = y - 2.5
    for row in range(30):
        for column in range(30):
            if 30 - row <= column:
                arcade.draw_lrtb_rectangle_filled(i + (10*column), i + 5 + (10*column), j - (10*row), j - 5 - (10*row), arcade.color.WHITE )



def draw_section_6(x, y):
    i = x + 2.5
    j = y - 2.5
    for row in range(30):
        for column in range(30):
            if row >= column:
                arcade.draw_lrtb_rectangle_filled(i + (10*column), i + 5 + (10*column), j - (10*row), j - 5 - (10*row), arcade.color.WHITE )


def draw_section_7(x, y):
    i = x + 2.5
    j = y - 2.5
    for row in range(30):
        for column in range(30):
            if 30 - row > column:
                arcade.draw_lrtb_rectangle_filled(i + (10*column), i + 5 + (10*column), j - (10*row), j - 5 - (10*row), arcade.color.WHITE )


def draw_section_8(x, y):
    i = x + 2.5
    j = y - 2.5
    for row in range(30):
        for column in range(30):
            if row <= column:
                arcade.draw_lrtb_rectangle_filled(i + (10*column), i + 5 + (10*column), j - (10*row), j - 5 - (10*row), arcade.color.WHITE )


def main():
    arcade.open_window(1200, 600, "Lab 06 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    draw_section_outlines()

    draw_section_1(0, 300)
    draw_section_2(300, 300)
    draw_section_3(600, 300)
    draw_section_4(900, 300)
    draw_section_5(0, 600)
    draw_section_6(300, 600)
    draw_section_7(600, 600)
    draw_section_8(900, 600)

    arcade.finish_render()

    arcade.run()

if __name__=='__main__':
    main()


