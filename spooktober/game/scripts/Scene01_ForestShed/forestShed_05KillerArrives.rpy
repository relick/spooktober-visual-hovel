# Audio
# --------
# 

# Backgrounds/ Images
# --------

# Sprites
# --------
# stacey scared

label forestShed_killerArrives:
    show stacey scared
    stacey "Beans... can you hear that?"
    "She freezes in place."
    "I listen - to the rustling leaves, the hooting of an owl..."
    "...and the heavy thud of approaching footsteps."

    show beans shout
    beans "{i}Oh my god{/i}"
    hide beans
    stacey "We have to hide!"


    menu:
        "Hide in the lockers" if foundLockers:
            jump .hideInLockers
        "Hide in an empty oil drum":
            jump .hideInOilDrum
        "Hide in the shed":
            jump .hideInTheShed
        "Run further into the woods":
            jump .runIntoTheWoods
    label .hideInLockers:
        if "Lantern" in beans.equipped:
            if beans.proactivePassive <= 0:
                "Stacey grabs my arm and pulls me over to the lockers."
            else:
                "I grab Stacey's arm and pull her over to the lockers."

            show beans serious2
            beans "What the- this one's full of junk!"
            hide beans
            stacey "In here with me!"
            
            "{i}The two of you squeeze into a locker that's barely big enough for two.{/i}"
            jump .lockerTalk      
        else:
            if beans.proactivePassive <= 0:
                "Stacey grabs my arm and pulls me over to the lockers."
            else:
                "I grab Stacey's arm and pull her over to the lockers."

            "Man, I hope there's nothing gross in here because I can't see a THING."
            "{i}CRASH{/i}" with vpunch

            "{i}An enormous pile of rusted junk comes crashing down on you.{/i}"
            "{i}It makes an enormous racket{/i}"

            show beans tired
            beans "Oh nooooooo-"
            hide beans
            
            show stacey surprised
            stacey "BEANS!"
            show beans sad
            beans "Do you think he heard that?"
            hide beans
            stacey "Of course he freakin heard it!"
            stacey "As if there's any point in hiding now - we've gotta run."
            jump .runIntoTheWoods

        
    label .hideInOilDrum:
        if searchedDrums:
            stacey "Don't go near the gnarly drum!"
            show beans sad
            beans "Oh man - it still {i}reeks.{/i}"
            hide beans

            "Okay - time to hide myself in one of these drums."
            "..."
            "This looks a lot smaller than I remembered..."

            stacey "Beans I'm not being funny, but like,"
            show stacey annoyed
            stacey "There is no WAY I'm going to fit into one of these."

            show beans stressed
            beans "So where do we go? Into the dark, forboding woods?!"
            hide beans

            show stacey determined
            stacey "It's our only hope! Come on, Beans!"
            jump scene_forestShed.runIntoTheWoods
        else:
            "TODO: Stacey rushes to hide in a drum, not noticing the rancid smell coming from it"
            "Unfortunately there's a rotting dead raccoon in there"
            "While she's freaking out the killer is basically on top of you"
            jump endings_forestShed.ending_oilDrums_mediocre

    label .hideInTheShed:
        if cutHand:
            jump endings_forestShed.ending_underTable_cutHand
        elif "Boots" in beans.backpack:
            "The boots make your bag too bulky to fit under the table with you"
            menu:
                "Throw your bag out of the shed":
                    "You throw your bag out into the darkness and scramble under the table - not a moment too soon."
                    jump .underTabletalk
                "Keep the bag but try and stay hidden":
                    jump endings_forestShed.ending_underTable_bootsInBag
        else:
            jump .underTabletalk