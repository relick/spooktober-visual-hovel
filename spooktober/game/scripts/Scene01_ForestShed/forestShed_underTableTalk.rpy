label forestShed_underTableTalk:
    narrate "You huddle together under the workbench."

    show beans stressed
    think "Uggh, it's so dusty down here."
    hide beans

    show stacey worried 
    stacey "Don't. Make. A. Sound."
    hide stacey

    think "Stacey's actually shaking..."
    think "She must be terrified!"

    show beans blush
    think "I always thought she was like..."
    think "Invincible or something."
    show beans blush2
    think "Is she... holding my hand?"
    hide beans

    narrate "You realise that Stacey has your hand in a vice-like grip."
    narrate "She's staring straight ahead."

    think "I don't think she's even noticed she's doing it."

    show beans blush
    beans "Um, Stacey..."
    menu:
        "Are you ok?":
            show beans serious
            beans "Are you ok?"
            hide beans
            $ stacey.approval += 1
            show stacey blush
            stacey "Oh, um."
            show stacey sigh
            stacey "Sorry - I just got a little spooked."
            hide stacey 


        "What's with the hand?":
            show beans serious
            beans "What's with the hand?"
            hide beans
            show stacey blush
            stacey "Oh, um."
            show stacey sigh
            stacey "Sorry - I just got a little spooked."
            hide stacey 

        "Let go of my damn hand.":
            show beans meanbean
            beans "Let go of my damn hand."
            hide beans

            $ stacey.approval -= 1
            show stacey worried
            stacey "Oh - sorry Beans."
            show stacey sad
            stacey "I don't know what came over me."

    $ lockerTalkLocation = "UnderTable"
    jump forestShed_lockerTalk
    