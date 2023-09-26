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
    # PETE: "She's frozen in place?"
    think "She freezes in place."
    think "I listen - to the rustling leaves, the hooting of an owl..."
    think "...and the heavy thud of approaching footsteps."

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
            # PETE: I think these two lines need rewriting as narration
            if beans.proactivePassive <= 0:
                think "Stacey grabs my arm and pulls me over to the lockers."
            else:
                think "I grab Stacey's arm and pull her over to the lockers."

            show beans serious2
            beans "What the- this one's full of junk!"
            hide beans
            stacey "In here with me!"
            
            narrate "The two of you squeeze into a locker that's barely big enough for two."
            jump .lockerTalk      
        else:
            # PETE: I think these two lines need rewriting as narration
            if beans.proactivePassive <= 0:
                think "Stacey grabs my arm and pulls me over to the lockers."
            else:
                think "I grab Stacey's arm and pull her over to the lockers."

            think "Man, I hope there's nothing gross in here because I can't see a THING."
            narrate "CRASH" with vpunch

            narrate "An enormous pile of rusted junk comes crashing down on you."
            narrate "It makes an enormous racket"

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

            think "Okay - time to hide myself in one of these drums."
            think "..."
            think "This looks a lot smaller than I remembered..."

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
            narrate "TODO: Stacey rushes to hide in a drum, not noticing the rancid smell coming from it"
            narrate "Unfortunately there's a rotting dead raccoon in there"
            narrate "While she's freaking out the killer is basically on top of you"
            jump endings_forestShed.ending_oilDrums_mediocre

    label .hideInTheShed:
        if cutHand:
            jump endings_forestShed.ending_underTable_cutHand
        elif "Boots" in beans.backpack:
            narrate "The boots make your bag too bulky to fit under the table with you"
            menu:
                "Throw your bag out of the shed":
                    narrate "You throw your bag out into the darkness and scramble under the table - not a moment too soon."
                    jump .underTabletalk
                "Keep the bag but try and stay hidden":
                    jump endings_forestShed.ending_underTable_bootsInBag
        else:
            jump .underTabletalk