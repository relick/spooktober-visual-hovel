# The script of the game goes in this file.

# Absolute magic that makes Beans Just Work(tm)
init -1 python:
    # Add delays on punctuation
    def replace_text(s):
        s = s.replace(". ", ".{w=0.25} ")
        # but ellipsis is longer
        s = s.replace("...{w=0.25} ", "...{w=0.5} ")
        s = s.replace("! ", "!{w=0.25} ")
        s = s.replace("? ", "?{w=0.25} ")
        return s
    config.say_menu_text_filter = replace_text

    # but the above also applies on menus
    # so delete any erroneous tags that made it through
    def unreplace_text(s):
        s = s.replace("{w=0.5}", "")
        s = s.replace("{w=0.25}", "")
        return s
    config.replace_text = unreplace_text

    config.layers = ['master', 'transient', 'screens', 'overlay']

    renpy.music.register_channel("bleeps", mixer="sfx")

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("beeps/mid_beep.wav", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps")

    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("beeps/high_beep.wav", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps")

    def typewriter_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("beeps/typewriter_beep.wav", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps")

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

transform in_locker:
    zoom 1.4
    align (0.5, 1.0)

# The game starts here.
label start:
    stop music
    jump scene_forestShed.backstoryIntro

# This ends the game.
label exit:
    return
