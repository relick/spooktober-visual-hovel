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

    beans "{i}Oh my god{/i}"
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

            beans "What the- this one's full of junk!"
            stacey "In here with me!"
            
            "{i}The two of you squeeze into a locker that's barely big enough for two.{/i}"
            jump .lockerTalk      
        else:
            "TODO: You fling the locker open to hide, but without a lantern you don't notice it's full of stuff, which comes crashing down on you"
            "With the killer alerted to your location, you're forced to run into the woods!"
            jump .runIntoTheWoods

        
    label .hideInOilDrum:
        if searchedDrums:
            "TODO: You avoid the stinky drum and try to cram yourself into one"
            "TODO: It's clearly not going to work. You have no choice but to run into the woods."
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