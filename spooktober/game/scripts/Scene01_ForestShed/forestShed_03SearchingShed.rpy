# Audio
# --------
# Striking match (striking a match to light a lantern)
# Metal clang (sitting on a rusted oil drum and it collapses/falls over)
# Cloth rip

# Backgrounds
# --------

# Sprites
# --------
# stacey determined
# stacey happy


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

        think "I can show Stacey I'm not totally useless!"
        
        scene bg shedinterior
        show stacey upsetshadow
        stacey "Ugh, this place is {i}dank{/i}."
        stacey "It feel like my lungs are rotting."

        show stacey determined
        stacey "Okay, look around for a flashlight or something."
        stacey "Careful! You touch any of these tools, it's a one-way trip to tetanus city."
        think "Those tools do look pretty unsafe..."
        think "But maybe we should be quick, who knows how long we've got before that weirdo comes after us?"
        menu: 
            "Search carefully":
                $ beansSearchedShed = True
                narrate "You carefully search the shelves, disturbing as little as possible."
                narrate "You spy a bulbous glass shape, hiding under a thick layer of dust, and gently wipe the grime away."
                show stacey happy
                stacey "A lantern! Great find, Beans."
                $ stacey.approval += 1

                stacey "And it's still got some fuel, ace."
                narrate "Stacey produces a lighter from her pocket."
                think "Stacey smokes?"

                show stacey worried
                stacey "Um. Don't tell my mom about this."

                narrate "The lantern lights easily."

                # Audio: Match striking? 
                # VFX: Glow of light to represent lantern lighting?
                show stacey laugh
                stacey "Let there be light!" # TODO: Not sure this fits the character

                show stacey happy
                call scene_forestShed.util_equipItem("Lantern")
                call scene_forestShed.util_updateKillerDistance(-1)                
                hide stacey
            "Search quickly":
                think "Screw being careful - I want to be out of here as quickly as possible."
                narrate "You begin rummaging haphazardly through the shelves."
                narrate "As you reach across the workbench your sleeve snags on the teeth of rusted rotary saw."
                # Audio: Cloth ripping
                show beans stressed
                beans "Ugh!"
                hide beans

                narrate "You rip your arm free a little too vigorously and your hand collides with the shelf above"
                narrate "Something glass and dust-covered falls off,  and shatters into pieces on the bench."

                show stacey annoyed
                stacey "Well that {i}was{/i} a lantern."
                $ smashedLantern = True
                $ stacey.approval -= 1

                think "That could have ended much worse!"
                think "I'd better be more careful, I don't want to hurt myself."
        call scene_forestShed.util_updateKillerDistance(-1)
        jump scene_forestShed.d_areaSearch

    # 3b Beans watches as Stacey searches the shed
    label .staceySearch:
        think "I'd better leave Stacey to it."
        think "I don't want to make things worse {i}again{/i}"
        call scene_forestShed.util_updateProactivePassive(-1)
        call scene_forestShed.util_updateKillerDistance(-1)
        stacey "Wait right there. Don't move a muscle, okay?"
        menu:
            "Wait anxiously for Stacey to finish searching":
                show beans blush
                beans "I'll just... wait right here then."
                think "Stacey seems to know what she's doing."
                hide beans

                show stacey happy
                stacey "Ah ha!"
                stacey "Still some paraffin left in this lantern"
                narrate "She pulls a lighter from her pocket."

                show beans earnest
                beans "Stacey! You {i}smoke?{/i}"
                hide beans

                show stacey sigh
                stacey "What are you, my mom?"

                narrate "The glass lantern sputters to life"

                show stacey happy
                stacey "Is that a good find or what?"
                call scene_forestShed.util_equipItem("Lantern")
            "Sit on one of the rusty oil drums while she searches":
                think "Ugh, my feet are killing me... I'll just take a load off on one of these oil drums."
                hide stacey
                stacey "Beans! I've found a lantern!"
                stacey "Looks like there's some fuel left in it, too"

                think "This drum looks like it's a gazillion years old."
                think "And something smells absolutely rank..."

                show beans shout
                beans "Woah!" with vpunch

                narrate "CLANG"
                think "That lid was rusted right through!"
                hide beans
                
                show stacey scared
                stacey "AAAAH!"

                # AUDIO: Glass smashing
                stacey "What's going on? Are you alright?!"

                # "I came SO close to getting my butt wedged in an old oil drum."
                show beans sad
                beans "I tried to sit on that oil drum but it totally just disintegrated!"
                hide beans

                show stacey angry
                stacey "Dammit Beans! You scared me so much I dropped the lantern!"
                stacey "And - oh god, what is {i}that{/i}?"

                # PETE: this line's halfway between think and narrate - should probably be one or the other
                # maybe something like: think "She's pointing inside the oil drum, which smells rancid..."
                think "She's pointing inside the oil drum."
                think "It smells absolutely rancid"

                show beans meanbean
                beans "Is that... a raccoon?"
                hide beans

                show stacey nauseous
                stacey "Well it's... half of one."

                show beans meanbean
                beans "I bet those maggots got the rest."
                hide beans

                think "The smell is so strong..."

                stacey "Oh man... that's so nasty"
                stacey "I think I'm gonna ralph."

                $ stacey.approval -= 1
                $ searchedDrums = True
                $ smashedLantern = True
        jump scene_forestShed.d_areaSearch