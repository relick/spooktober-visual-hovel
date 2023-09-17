# Audio
# --------

# Backgrounds
# --------

# Sprites
# --------

label forestShed_searchingShed:
    show stacey determined 
    stacey "I'm going to search for another flashlight."

    menu:
        "Help Stacey search the shed":
            jump .beansSearch
        "Watch Stacey search the shed":
            jump .staceySearch

    # 3a Beans searches the shed herself
    label .beansSearch:
        call scene_forestShed.util_updateProactivePassive(1)
        call scene_forestShed.util_updateKillerDistance(-1)
        $ beansSearchedShed = True
        menu: 
            "Search carefully":
                call scene_forestShed.util_equipItem("Lantern")
                call scene_forestShed.util_updateKillerDistance(-1)                
                
            "Search quickly":
                $ stacey.approval -= 1
        jump scene_forestShed.d_areaSearch

    # 3b Beans watches as Stacey searches the shed
    label .staceySearch:
        "I'd better leave Stacey to it."
        "I don't want to make things worse {i}again{/i}"
        call scene_forestShed.util_updateProactivePassive(-1)
        call scene_forestShed.util_updateKillerDistance(-1)
        stacey "Wait right there. Don't move a muscle, okay?"
        menu:
            "Wait anxiously for Stacey to finish searching":
                beans "I'll just... wait right here then."
                "Stacey seems to know what she's doing."

                show stacey happy
                stacey "Ah ha!"
                stacey "Still some paraffin left in this lantern"
                "She strikes a match and the glass lantern sputters to life"
                stacey "Is that a good find or what?"
                call scene_forestShed.util_updateKillerDistance(-1)
                call scene_forestShed.util_equipItem("Lantern")
            "Sit on one of the rusty oil drums while she searches":
                "Ugh, my feet are killing me... I'll just take a load off on one of these oil drums."
                hide stacey
                stacey "Beans! I've found a lantern!"
                stacey "Looks like there's some fuel left in it, too"

                "This drum looks like it's a gazillion years old."
                "And something smells absolutely rank..."

                beans "Woah!" with vpunch

                "{i}CLANG{/i}"
                "That lid was rusted right through!"
                
                show stacey scared
                stacey "AAAAH!"

                # AUDIO: Glass smashing
                stacey "What's going on? Are you alright?!"

                # "I came SO close to getting my butt wedged in an old oil drum."
                beans "I tried to sit on that oil drum but it totally just disintegrated!"

                show stacey angry
                stacey "Dammit Beans! You scared me so much I dropped the lantern!"
                stacey "And - oh god, what is {i}that{/i}?"

                "I look at where she's pointing - inside the oil drum, where that rancid smell is coming from."

                beans "Is that... a raccoon?"

                show stacey nauseous
                stacey "Well it's... half of one."
                beans "I bet those maggots got the rest."

                "The smell is so strong..."

                stacey "Oh man... that's so nasty"
                stacey "I think I'm gonna ralph."

                $ stacey.approval -= 1
                $ searchedDrums = True
                call scene_forestShed.util_updateKillerDistance(-2)
        jump scene_forestShed.d_areaSearch