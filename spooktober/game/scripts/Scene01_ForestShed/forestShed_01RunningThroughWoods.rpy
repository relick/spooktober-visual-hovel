# Audio
# --------
# panting (beans/stacey)
# beans tripping over a tree root
# crack/thud (dropping the flashlight and it breaks)

# Backgrounds
# --------
# forest
# shedSilhouette
# shed

# Sprites
# --------
# stacey tired
# stacey excited
# stacey disappointed
# stacey angry

label forestShed_runningThroughWoods:
    scene bg forest

    play music "audio/music/Hallowbean_Nature.ogg" fadein 2.0 loop

    # AUDIO: Panting?

    show beans tired # PETE: added this
    think "I'm so tired... and my feet hurt..."
    #  think "This tin of beans is so heavy..."
    think "It's getting dark so fast..."
    show beans shout # PETE: added this
    think "Glad I grabbed that flashlight from Gerald's survival kit."

    show beans sad
    beans "Poor Gerald..."
    show beans tired
    beans "I wonder where the others are?"
    hide beans

    show stacey sigh
    stacey "I'm sure the road was this way."

    show stacey annoyed
    stacey "Can't you keep up, Beans?"

    show beans stressed
    beans "I'm going as fast as I can!"
    think "How am I meant to keep up with a champion cheerleader?"
    hide stacey 

    show beans tired
    think "I can barely see where I'm putting my feet!"
    hide beans
    
    show screen timed_choice(3.0, "forestShed_runningThroughWoods.fail_choice_trip_treeroot")
    menu:
        "Trip over a tree root!":
            hide screen timed_choice
            call .trip("tree root")
            jump after_treeroot
        "Fall over a log!":
            hide screen timed_choice
            call .trip("log")
            jump after_treeroot
        "Avoid the obstacles!":
            hide screen timed_choice
            call .avoid
            jump after_treeroot
        "Stumble on a fallen branch!":
            hide screen timed_choice
            call .trip("branch")
            jump after_treeroot

    label .fail_choice_trip_treeroot:
        call .trip("tree root")
        jump after_treeroot

    label .trip(object = "default"):
        # AUDIO: Thud
        show beans shout
        beans "OOF-" with vpunch
        think "That [object] came out of nowhere!"
        hide beans
        return

    label .avoid:
        show beans kewl
        think "Sure footed as a mountain goat!"
        show beans shout # pain
        beans "OOF-" with vpunch
        beans "Ohh..."
        beans "I was so busy avoiding the branches I just ran face first into that tree."
        hide beans
        return



label after_treeroot:

    # AUDIO: Crack
    narrate "CRACK"

    # TODO: Some kind of flash indicating the light went out?
    think "Was that... the flashlight?"
    
    show beans shout
    beans "Oh no..."
    hide beans

    show stacey annoyed # note: was angry
    stacey "Beans! Please tell me you did not just break our ONLY flashlight."

    menu:
        "I'm sorry...":
            show beans sad
            beans "I'm sorry..."
            hide beans

            $ stacey.approval += 1
            show stacey sigh
            stacey "{i}Sigh{/i}"
            stacey "Sorry it's just... this is kind of stressful, you know."

            show stacey sad
            stacey "I don't want anyone else to wind up dead."
            stacey "It would look {i}real{/i} bad on my record as class president."
        "It wasn't my fault, I can't see where I'm going in this dumb forest.":
            show beans stressed
            beans "It wasn't my fault, I can't see where I'm going in this dumb forest."
            hide beans

            show stacey sigh
            stacey "Ugh, Beans..."

            show stacey determined
            stacey "You're a major liability."
            stacey "You know that, right?"
            stacey "Just try not to break anything else."

            show stacey sigh
            stacey  "{i}Please{/i}."

            show stacey determined
        "Can it, Stacey":
            show beans meanbean
            beans "Can it, Stacey."
            hide beans

            $ stacey.approval -= 1
            show stacey annoyed # note: was angry
            stacey "Don't tell me to can it!"
            stacey "This day is {i}literally{/i} the worst."

            stacey "First the crash, then what happened to Gerald."
            stacey "THEN you break our flashlight, and NOW you tell me to can it!"

            show stacey annoyed # note: was angry
            stacey "Ugh! You are making me so mad right now!"
            hide stacey
            show beans sad
            think "She's stormed off!"
            show beans stressed
            think "I'd better follow if I don't want to get even more lost."

    show beans serious2
    think "Come on Beans. No more running into things."

    hide stacey
    
    show beans kewlpewpew
    think "You got this, Beanie-baby!"

    show beans kewl
    think "..."
    think "Can't believe I'm still single."
    hide beans

    show stacey excited
    stacey "Wait!" with vpunch

    $ crossfade("audio/music/Hallowbean_Drone.ogg")

    play sound "audio/stingers/lonely.wav"
    call screen panel("shedShadow") with dissolve
    show beans shout
    think "Is that... a house?"
    hide beans

    menu:
        "We're saved!":
            show beans earnest
            beans "We're saved!"
            hide beans 
            jump .saved
        "Careful - we don't know if we can trust them":
            show beans earnest
            beans "Careful - we don't know if we can trust them."
            hide beans 
            jump .careful

    # "We're saved!"
    label .saved:
        stacey "Maybe they have a telephone! We can call the police!"
        
        show beans earnest
        beans "Stacey, wait!"
        show beans sad
        think "How is she so fast??"

        show beans tired
        beans "Huff... huff..."
        hide beans
        scene bg forest
        play sound "audio/stingers/shiver.wav"
        call screen panel("shed") with dissolve
        show stacey sigh # note: was disappointed

        stacey "Ugh. It's obviously abandoned."
        think "It looks pretty small for a house, too."

        jump scene_forestShed.b_discoveringShed

    # "Careful - we don't know if we can trust them"
    label .careful:
        stacey "True."
        stacey "They might be those weird forest people who marry their uncles."

        narrate "You creep forward, making each footstep as silent as possible."

        narrate "The moonlight is glimmering off Stacey's hoop earrings."
        show beans blush
        think "The way it dances across the chemically treated curls of her hair..."
        think "It's almost magical."
        hide beans

        scene bg forest
        play sound "audio/stingers/shiver.wav"
        call screen panel("shed") with dissolve
        show stacey sad # note: was disgusted
        stacey "Ugh."
        stacey "Man, is this place {i}grody{/i}."
        jump scene_forestShed.b_discoveringShed
        
