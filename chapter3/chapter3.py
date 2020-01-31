import arcade

arcade.open_window(600,600, "Drawing Example")

#arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
#arcade.set_background_color((114, 160, 199))   #=AIR_SUPERIORITY_BLUE
#arcade.set_background_color((127, 127, 127))    #GRAY
arcade.set_background_color((0, 225, 225))       #LIGHT BLUE


arcade.start_render()   #I'm about to draw from now on. ready for that!


arcade.draw_lrtb_rectangle_filled(
    5, 35, 590, 570,                #left/right/tob/bottom
    arcade.color.BITTER_LIME        #color
)

arcade.draw_lrtb_rectangle_outline(
    5, 35, 90, 70, arcade.color.BITTER_LIME
    )

arcade.draw_circle_filled(
    190, 580, 18,
    arcade.color.RED
)


arcade.finish_render()  #I'm doen my drawing. You don't need to get ready for drawing anymore.

arcade.start_render()

arcade.run()