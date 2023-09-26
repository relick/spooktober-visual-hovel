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
    # AUDIO: Panting?

    hide beans
    think "I'm so tired... and my feet hurt..."
    think "This tin of beans is so heavy..."
    think "It's getting dark so fast..."
    think "Good thing I brought Gerald's flashlight!"

    show stacey tired
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
    
    show screen timed_choice(3.0, "fail_choice_trip_treeroot")
    menu:
        "Trip over a tree root!":
            hide screen timed_choice
            call after_treeroot.trip("tree root")
            jump after_treeroot
        "Fall over a log!":
            hide screen timed_choice
            call after_treeroot.trip("log")
            jump after_treeroot
        "Avoid the obstacles!":
            hide screen timed_choice
            call after_treeroot.avoid
            jump after_treeroot
        "Stumble on a fallen branch!":
            hide screen timed_choice
            call after_treeroot.trip("branch")
            jump after_treeroot

label fail_choice_trip_treeroot:
    call after_treeroot.trip("tree root")

label after_treeroot:

    # AUDIO: Crack
    narrate "{i}CRACK{/i}"

    # TODO: Some kind of flash indicating the light went out?
    show beans shout
    think "Was that... the flashlight?"
    # PETE: the 'Oh no...' might be better vocalised
    think "Oh no..."
    hide beans

    show stacey angry
    stacey "Beans! Please tell me you did not just break our ONLY flashlight."

    menu:
        "I'm sorry...":
            $ stacey.approval += 1
            show stacey tired
            stacey "{i}Sigh{/i}"
            stacey "Sorry it's just... this is kind of stressful, you know."
            stacey "I don't want anyone else to wind up dead."
            stacey "It would look {i}real{/i} bad on my record as class president."
        "It wasn't my fault, I can't see where I'm going in this dumb forest.":
            show stacey tired
            stacey "Ugh, Beans..."
            stacey "You're a major liability. You know that, right?"
            stacey "Just try not to break anything else, {i}please{/i}."
        "Can it, Stacey":
            $ stacey.approval -= 1
            stacey "Don't tell me to can it!"
            stacey "First you make us crash, then you break our flashlight-"
            stacey "UGH! You are making me SO MAD right now!"
            hide stacey
            show beans sad
            think "She's stormed off!"
            show beans stressed
            think "I'd better follow if I don't want to get even more lost"

    show beans serious2
    think "I'm trying really, {i}really{/i} hard not to run into anything else"
    think "...but it's getting harder as the daylight is fading"
    hide beans

    show stacey excited
    stacey "Wait!" with vpunch

    call screen panel("shedSillhouette") with dissolve
    show beans shout
    think "Is that... a house?"
    hide beans

    menu:
        "We're saved!":
            jump .saved
        "Careful - we don't know if we can trust them":
            jump .careful

    # "We're saved!"
    label .saved:
        stacey "Maybe they have a telephone! We can call the police!"
        
        show beans earnest
        beans "Stacey, wait!"
        show beans sad
        think "How is she so fast??"

        show beans tired
        beans "Huff.. huff.."
        hide beans
        scene bg forest
        call screen panel("shed") with dissolve
        show stacey disappointed

        stacey "Ugh. It's obviously abandoned."
        think "It looks pretty small for a house, too"

        jump scene_forestShed.b_discoveringShed

    # "Careful - we don't know if we can trust them"
    label .careful:
        stacey "True."
        stacey "They might be those weird forest people who marry their uncles."

        think "I creep forward, making each footstep as silent as possible."

        think "The moonlight is glimmering off Stacey's hoop earrings."
        think "The way it dances across the chemically treated curls of her hair.... "
        think "It's almost magical."

        scene bg forest
        call screen panel("shed") with dissolve
        show stacey disgusted
        stacey "Ugh."
        stacey "This place is abandonedville. And it's {i}hella{/i} grody."
        jump scene_forestShed.b_discoveringShed
        

    label .trip(object = "default"):
        # AUDIO: Thud
        show beans shout
        beans "OOF-" with vpunch
        think "That [object] came out of nowhere!"
        hide beans

    label .avoid:
        show beans kewl
        think "Sure footed as a mountain goat!"
        show beans shout # pain
        beans "OOF-" with vpunch
        beans "Ohh... should have watched where I was going..."
        beans "I just ran face first into that tree."
        hide beans