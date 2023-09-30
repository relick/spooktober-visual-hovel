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
    
    think "She's frozen in place,"
    think "I can hear rustling leaves, the hooting of an owl..."
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
            if beans.proactivePassive <= 0:
                narrate "Stacey grabs your arm and pulls you over to the lockers."
            else:
                narrate "You grab Stacey's arm and pull her over to the lockers."

            show beans serious2
            beans "What the- this one's full of junk!"
            hide beans
            stacey "In here with me!"
            
            narrate "The two of you squeeze into a locker that's barely big enough for two."
            jump forestShed_lockerTalk      
        else:
            if beans.proactivePassive <= 0:
                narrate "Stacey grabs your arm and pulls you over to the lockers."
            else:
                narrate "You grab Stacey's arm and pull her over to the lockers."

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
            beans "We can hide in one of those oil drums!"

            show stacey worried
            stacey "Oh shit oh shit oh SHIT"

            narrate "Stacey fumbles as she tears the lid off the nearest drum"
            think "I've never seen her so scared"
            
            show beans stressed
            think "Oh man - what is that SMELL?"
            hide beans

            show stacey scared
            stacey "AAAAAAH!" with vpunch

            stacey "I just- in the drum-"
            stacey "I put my foot in it-"
            stacey "Aagh!"

            show stacey nauseous
            stacey "What {i}is{/i} that?"

            think "Stacey's shoe is covered in some kind of... sticky red mush."
            think "Oh god..."

            show beans stressed
            beans "Is that raccoon fur?"


            menu:
                "Pull yourself together!":
                    jump .pullYourselfTogether
                "Did you death-stomp a raccoon??":
                    jump .raccoonStomp    

        label .pullYourselfTogether:
            show beans stressed
            beans "We haven't got time for this!"
            hide beans

            stacey "This is SO GROSS!"
            narrate "Stacey frantically tries to wipe her shoes on the grass"
            narrate "Suddenly she stops, looking wide-eyed over your shoulder"

            narrate "You can hear the heavy thud of footsteps towards you."
            narrate "Your time has run out."
            narrate "You can't both outrun him."

            menu:
                "{i}Distract him so Stacey can escape{/i}":
                    jump .distract
                "{i}Push past Stacey and escape{/i}":
                    jump .escape
                "{i}Accept your fate.{/i}":
                    jump .giveUp

            label .distract:
                show beans meanbean
                beans "Stacey, {i}go{/i}."
                hide beans 

                show stacey upsetshadow
                stacey "Beans..."

                show beans shout
                beans "GO!"
                hide beans

                hide stacey
                think "Well here goes fucking nothing"

                narrate "You turn to face the killer."

                beans "Look over here, you big dumb sack of butts."
                beans "Catch me if you can!"
                jump endings_forestShed.ending_oilDrums_heroic
            label .escape:
                jump endings_forestShed.ending_oilDrums_mediocre
            label .giveUp:
                jump endings_forestShed.ending_oilDrums_terribad
        label .raccoonStomp:
            show beans shout
            beans "Did you death-stomp a raccoon??"
            hide beans 

            show stacey shout
            stacey "It was already dead!"
            
            show stacey nauseous
            stacey "I just put my foot in there and like, it just, {i}squelched{/i}"
            
            show beans stressed
            beans "It {i}squelched{/i}?"
            beans "Urggghh..."
            hide beans 

            narrate "Your stomach does a flip as you try not to stare at the scraps of dead raccoon in the drum"
            narrate "Stacey frantically tries to wipe her shoes on the grass"
            narrate "Suddenly she stops, standing stock-still"

            show stacey scared
            stacey "Um, Beans?"
            
            show beans stressed
            beans "Yeah?"
            hide beans

            stacey "Did you hear where that weirdo went?"

            show beans meanbean
            beans "..."
            hide beans

            think "We were too busy freaking out to keep track of him"

            narrate "There's a beat of silence."
            narrate "The silence gives way to heavy breathing."
            narrate "It's"
            narrate "right"
            narrate "behind"
            narrate "you"

            show beans meanbean
            beans "Stacey..."
            hide beans

            menu:
                "I'm so sorry":
                    show stacey scared
                    stacey "Me too-"
                "I love you":
                    show stacey scared
                    stacey "Beans-"
                "I'll see you in hell":
                    show stacey scared
                    stacey "Fuck you, Beans"
            
            hide stacey
            jump endings_forestShed.ending_oilDrums_terribad

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