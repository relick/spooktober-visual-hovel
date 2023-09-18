# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Stacey")

# Setup for timed choices
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out

screen timed_choice(time, timer_jump):
    default timer_range = time
    default timer_countdown = time

    # Tick time down and jump if we hit 0
    timer 0.01 repeat True action If(timer_countdown > 0, true=SetLocalVariable('timer_countdown', timer_countdown - 0.01), false=[Hide('timed_choice'), Jump(timer_jump)]) 

    # Timer bar, multiplied by 100 to make smooth?
    bar value (timer_countdown * 100):
        range (timer_range * 100)
        xalign 0.5
        yalign 0.9
        xmaximum 300
        at alpha_dissolve

# The game starts here.

label start:
    jump scene_forestShed.a_runningThroughWoods
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mills

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show stacey neutral

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    show stacey pain

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
