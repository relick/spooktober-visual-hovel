# Audio
# --------
# 

# Backgrounds/ Images
# --------

# Sprites
# --------
# stacey scared

label forestShed_killerArrives:
    hide stacey
    narrate "Suddenly, Stacey stops and goes completely rigid."
    show stacey scared
    stacey "Beans... can you hear that?"
    
    $ crossfade("audio/music/Hallowbean_Pads.ogg")

    think "She's frozen in place"
    think "I can hear rustling leaves, the hooting of an owl..."
    think "...and the heavy thud of approaching footsteps."

    show beans shout
    beans "{i}Oh my god{/i}"
    beans "It's that weird guy!"
    beans "He killed Gerald and now he's after us!"
    hide beans
    stacey "We have to hide!"


    menu:
        "{i}Hide in the lockers{/i}" if foundLockers:
            jump .hideInLockers
        "{i}Hide in an empty oil drum{/i}":
            jump .hideInOilDrum
        "{i}Hide in the shed{/i}":
            jump .hideInTheShed
        "{i}Run further into the woods{/i}":
            jump forestShed_runIntoWoods
    label .hideInLockers:
        scene bg locker
        $ crossfade("audio/music/Hallowbean_Heartbeat.ogg")

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
            
            show stacey worried # note: was surprised
            stacey "BEANS!"
            show beans sad
            beans "Do you think he heard that?"
            hide beans
            stacey "Of course he freakin heard it!"
            stacey "As if there's any point in hiding now - we've gotta run."
            jump forestShed_runIntoWoods

        
    label .hideInOilDrum:
        scene bg oildrums
        $ crossfade("audio/music/Hallowbean_Heartbeat.ogg")

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
            jump forestShed_runIntoWoods
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
                    show beans serious2
                    beans "Pull yourself together!"

                    jump .pullYourselfTogether
                "Did you death-stomp a raccoon??":
                    show beans shout
                    beans "Did you death-stomp a raccoon??"
                    hide beans 
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
                $ crossfade("audio/music/SweetRedBeans.ogg")
                play heartbeat "audio/music/Hallowbean_HeartbeatOnly.ogg" loop fadein 2.0

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
                think "I.."

                show beans meanbean
                think "I want to live!"
                hide beans 

                narrate "Pure adrenaline spikes in your veins"
                narrate "You push Stacey aside, scrambling over the rusted oil drums"
                narrate "There's no thoughts in  your head, only survival"

                stacey "Beans, what-"
                hide stacey

                jump endings_forestShed.ending_oilDrums_mediocre
            label .giveUp:
                jump endings_forestShed.ending_oilDrums_terribad
        label .raccoonStomp:
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
            think "Well, this is it."
            think "I'm about to die."
            beans "Stacey..."
            
            hide beans

            menu:
                "I'm so sorry":
                    show beans blush
                    beans "I'm so sorry"
                    show stacey scared
                    stacey "Me too-"
                    if stacey.approval > 3:
                        jump endings_forestShed.ending_oilDrums_terribad_hands
                    else:
                        jump endings_forestShed.ending_oilDrums_terribad
                    
                #"I love you":
                    #show beans confess
                    #beans "I love you."
                    
                    #show stacey scared
                    #stacey "Beans-"
                    #hide stacey
                    #hide beans
                    #jump endings_forestShed.ending_oilDrums_terribad_hands
                "I'll see you in hell":
                    show beans meanbean
                    beans "I'll see you in hell"
                    hide beans

                    show stacey scared
                    stacey "Fuck you, Beans"           
                    hide stacey
                    jump endings_forestShed.ending_oilDrums_terribad
            
    label .hideInTheShed:
        scene bg shedinterior
        $ crossfade("audio/music/Hallowbean_Heartbeat.ogg")

        think "The shed is tiny"
        if cutHand:
            narrate "Enormous weatherproof boots stomp slowly into view."
            narrate "You clamp your hands over your mouth."
            think "Can't... make... a... sound.."
      
            narrate "Stacey is trembling beside you."
            narrate "Your cut hand stings under its makeshift bandage."
            narrate "Your cut hand."
            think "{i}Shit.{/i}"

            narrate "The fresh blood spatters on the flood condemn you."
            narrate "The boots stop in front of them."
            narrate "Time slows down as the figure bends down,"
            narrate "Inspecting the fresh droplets of red."

            jump endings_forestShed.ending_underTable_cutHand
        else:
            jump forestShed_underTableTalk

