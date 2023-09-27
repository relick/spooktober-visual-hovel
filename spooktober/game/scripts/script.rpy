# The script of the game goes in this file.

# Absolute magic that makes Beans Just Work(tm)
init -1 python:
    config.layers = ['master', 'transient', 'screens', 'overlay']

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("beeps/mid_beep.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("beeps/high_beep.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def typewriter_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("beeps/typewriter_beep.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

init -1:
    transform portrait:
        align (0.07,0.95)
        zoom 0.4

    transform other_person:
        align (0.5, 1.0)

    $ config.tag_layer['beans'] = 'screens'
    $ config.tag_zorder['beans'] = 25 # above dialogue, below game over
    $ config.tag_transform['beans'] = portrait
    $ config.tag_transform['stacey'] = other_person
    define gui.dialogue_text_font = "LinLibertine_R.ttf"
    define gui.dialogue_text_size = 33

# The game starts here.
label start:
    jump scene_forestShed.a_runningThroughWoods

# This ends the game.
label exit:
    return
