# The script of the game goes in this file.

# Absolute magic that makes Beans Just Work(tm)
init -1 python:
    config.layers = ['master', 'transient', 'screens', 'overlay', 'aboveUI']

init -1:
    transform portrait:
        align (0.04,0.9)
        zoom 0.5

    $ config.tag_layer['beans'] = 'aboveUI'
    $ config.tag_transform['beans'] = portrait

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Stacey")

# The game starts here.

label start:
    show beans kewl

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
