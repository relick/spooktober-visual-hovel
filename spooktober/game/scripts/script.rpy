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
    
    renpy.music.register_channel("music2", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    renpy.music.register_channel("heartbeat", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    def crossfade(track_new, track_new_loop=None, curr_time=2.0,new_time=2.0):
        curr_track = "music"
        x_fade_track = "music2"
        do_loop = True
        if track_new_loop is not None:
            do_loop = False
        if not renpy.music.is_playing("music"):
            x_fade_track = "music"
            curr_track = "music2"
        if renpy.music.get_playing(curr_track) == track_new:
            return

        renpy.music.stop(curr_track,fadeout=curr_time)
        renpy.music.play(track_new,channel=x_fade_track,fadein=new_time,loop=do_loop)
        if not do_loop:
            renpy.music.queue(track_new_loop,channel=x_fade_track,loop=True)

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
        # hovering next to text
        # align (0.07,0.95)
        # zoom 0.4

        # aligned in bottom left
        align (0.0,1.0)
        zoom 0.5

    transform other_person:
        align (0.5, 1.0)

    $ config.tag_layer['beans'] = 'screens'
    $ config.tag_zorder['beans'] = 25 # above dialogue, below game over
    $ config.tag_transform['beans'] = portrait
    $ config.tag_transform['stacey'] = other_person
    define gui.dialogue_text_font = "LinLibertine_R.ttf"
    define gui.dialogue_text_size = 33

    image cg killerIsHere = "images/cg killerIsHere.png"
    image cg killerIsHereBlurred = "images/cg killerIsHereBlurred.png"

transform in_locker:
    zoom 1.4
    align (0.5, 1.0)

# The game starts here.
label start:
    stop music
    stop music2
    jump scene_forestShed.backstoryIntro

# This ends the game.
label exit:
    return
