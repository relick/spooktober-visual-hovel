# The script of the game goes in this file.

# Absolute magic that makes Beans Just Work(tm)
init -1 python:
    config.layers = ['master', 'transient', 'screens', 'overlay']

init -1:
    transform portrait:
        align (0.04,0.9)
        zoom 0.5

    transform other_person:
        align (0.5, 1.0)

    $ config.tag_layer['beans'] = 'screens'
    $ config.tag_zorder['beans'] = 25 # above dialogue, below game over
    $ config.tag_transform['beans'] = portrait
    $ config.tag_transform['stacey'] = other_person
    define gui.dialogue_text_font = "LinLibertine_R.ttf"
    define gui.dialogue_text_size = 33

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Stacey")

# The game starts here.
label start:
    jump scene_forestShed.a_runningThroughWoods

# This ends the game.
label exit:
    return
