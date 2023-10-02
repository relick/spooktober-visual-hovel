label endings_forestShed:
    label .ending_oilDrums_mediocre:
        # Stacey dies, you live
        narrate "The guilt will come later."
        narrate "You slip out of reach, stumbling over tree roots and dried leaves."
        narrate "Behind you comes a scream, cut off by a wet squelch."
        narrate "You run into the woods as fast as you can."
        narrate "..."

        narrate "It seems you and Stacey were not meant to be."
        
        # vertical columns
        play sound "audio/stingers/scream.wav"
        call screen game_over()
        return
    
    label .ending_oilDrums_heroic:
        # You die, Stacey lives        
        narrate "Stacey vaults over the drums, her cheerleader training paying off in her athleticism."
        narrate "You, however, are not a cheerleader." 

        narrate "As you run, trying to kite the maniac away from her, your lungs burn and your feet stumble."
        narrate "With a sinking feeling, you realise"
        narrate "there's only one way this can end."
        narrate "An enormous hand lifts you off the ground by the back of your shirt." 
        narrate "The air stinks of rotten meat and sweet, metallic blood." 
        narrate "A blade whistles through the air."

        narrate "This is your time."
        
        # ..squares
        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return

    label .ending_oilDrums_terribad:
        # You both die
        narrate "The figure looms over you"
        narrate "Expressionless eyes leer at you from the mask"
        narrate "It's impossible to tell whether they take any pleasure in this"

        narrate "This is the end."

        # ..squares
        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return       

    label .ending_oilDrums_terribad_hands:
        $ crossfade("audio/music/Hallowbean_Drone.ogg")

        # You both die
        narrate "The figure looms over you"
        narrate "Expressionless eyes leer at you from the mask"
        narrate "It's impossible to tell whether they take any pleasure in this"   

        narrate "Stacey wordlessly takes your hand in hers"
        narrate "She squeezes it tightly"

        show stacey sad
        stacey "I... wish I'd known you better, Beans."
        hide stacey

        narrate "This is the end."
        # weird pixellation
        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return

    label .ending_underTable_bootsInBag:
        # Not using this one
        narrate "TODO: The killer sees your bag and discovers your hiding place"
        narrate "RIP"
        # basically just a direct fade
        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return

    label .ending_underTable_cutHand:
        $ crossfade("audio/music/Hallowbean_Drone.ogg")

        # You both die
        show beans meanbean
        beans "..."
        hide beans

        think "I'm holding my breath."
        narrate "An enormous gloved hand shoots out and grabs you by the ankle."

        show beans shout
        beans "Aaagh!"
        hide beans

        narrate "You try and scramble away."
        narrate "Your hands scrape uselessly against the floorboards."

        think "I can't break free..."
        menu:
            "Stacey, run!":
                show beans earnest
                beans "Stacey, run!"
                hide beans


                stacey "..."
                narrate "Her eyes are wide, terrified beyond belief."
                narrate "She already knows it's too late."
                narrate "..."
                narrate "Your fates are sealed."

            "Let me go!":
                show beans shout
                "Let me go!"
                hide beans
                
                narrate "The figure gives no indication that it's heard you."
                narrate "The expressionless mask doesn't change."

                beans "Please..."

                narrate "You search for a glimpse of humanity in those hollow, empty eyes."
                narrate "There is nothing."
                
                beans "..."
                narrate "You cling to your hope."
                narrate "Until that last moment,"
                narrate "As you struggle weakly against their grip, and the heavy axe blade whistles through the air,"
                narrate "you cling to it."
                narrate "But it does not help you."
        
        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return

    python:
        """
        label .ending_runFromBearTrap_boots:
            narrate "TODO: You try and run, leaving Stacey in the bear trap"
            narrate "Unfortunately you trip on the stupid old boots you're wearing. The killer catches you anyway."
            narrate "Bad end."
            call screen you_died()
            return
        """
    label .ending_runFromBearTrap_noBoots:
        $ crossfade("audio/music/Hallowbean_Drone.ogg")

        # You live, Stacey dies
        narrate "You hear her scream, cut off by a wet squelch, and scramble into the woods as fast as you can."
        narrate "You may have made it,"
        narrate "But Stacey did not"
        play sound "audio/stingers/scream.wav"
        call screen game_over()
        return

    label .ending_staceyStuckInBearTrap:
        $ crossfade("audio/music/Hallowbean_Drone.ogg")

        # You both die
        narrate "You continue to fumble uselessly with the trap."
        narrate "Your hands are still uselessly trying to pry it apart when the heavy footsteps catch up to you."
        narrate "Could you have made it if you left her behind?"
        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return

    label .ending_staceyFreedFromBearTrap:
        # You both live!
        narrate "Stacey's leg is mangled by the bear trap."

        show beans stressed
        beans "Oh man... that's a lot of blood."
        hide beans

        show stacey determined
        stacey "Come on beans, we've made it this far."
        hide stacey

        narrate "You wrap an arm around her waist, and she leans on your shoulder."
        narrate "Despite the height difference, you manage to act as a sort of crutch for her to hobble along."

        narrate "Although she winces every time you take a step, Stacey doesn't cry out."

        if staceyDateAgreed:
            jump endings_forestShed.ending_lockerEscape_romance
        else:
            jump endings_forestShed.ending_lockerEscape_noRomance
        return

    label .ending_beansStuckInBearTrap:
        $ crossfade("audio/music/Hallowbean_Drone.ogg")

        # You die, Stacey lives
        hide stacey
        narrate "And just like that, Stacey disappears into the forest."
        narrate "You're lying on a carpet of leaves and blood, alone."
        narrate "Well, not quite alone."
        narrate "As you fade away, you can faintly hear heavy footsteps"
        narrate "Stomping relentlessly towards you in the dark."
        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return

    label .ending_beansStuckInBearTrap_noKiller:
        $ crossfade("audio/music/Hallowbean_Drone.ogg")

        # You die, Stacey lives
        hide stacey
        narrate "Stacey holds your hand as you begin to drift away."
        narrate "Just as if you were falling asleep."
        narrate "The forest is quiet."
        narrate "And you are still."
        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return

    label .ending_savedFromBearTrap:
        if staceyDateAgreed:
            $ crossfade("audio/music/SweetRedBeans.ogg")
        else:
            $ crossfade("audio/music/Hallowbean_Nature.ogg")

        # You both live!
        narrate "You're amazed that Stacey knows how to disarm a bear trap."
        show beans blush
        beans "You're full of surprises Stacey, you know that?"
        hide beans

        show stacey laugh
        stacey "Heh, it was nothing!"
        hide stacey

        if staceyDateAgreed:
            jump endings_forestShed.ending_lockerEscape_romance
        else:
            jump endings_forestShed.ending_lockerEscape_noRomance
        return

    label .ending_lockerEscape_romance:
        # GOOD ENDING WITH KISS
        narrate "You disappear safely into the forest."
        narrate "This has been the longest night of your lives."
        narrate "It seems like the sun is never going to rise."
        narrate "And yet..."

        show stacey happy
        stacey "Beans!"

        show beans tired
        beans "Uh?"

        show stacey laugh
        stacey "The sunlight! Through the trees!"
        narrate "A new day is dawning after all."

        show beans earnest
        beans "We made it back to the road!"

        show stacey laugh # note: was smile
        stacey "We did it!"

        narrate "You emerge from the woods, hand in hand."
        narrate "This night has not ended you."
        
        show stacey laugh
        stacey "Now, I believe someone promised me a date?"

        call screen good_ending("goodEndKiss") with dissolve
        return

    label .ending_lockerEscape_noRomance:
        # GOOD ENDING PLATONIC
        narrate "You run for your lives into the forest"
        narrate "The paths are winding,"
        narrate "And with only the vaguest idea of direction you could be getting further into danger each minute."
        narrate "The night drags on,"
        narrate "But eventually, every night must end."

        stacey "Beans... Beans!"

        show beans tired
        beans "I'm going as fast as I can..."
        beans "I just... need to rest a minute..."

        show stacey happy
        stacey "No Beans, look!"
        stacey "We finally made it back to the road!"

        narrate "Golden sunlight glimmers through the trees."

        beans "We... did?"

        show stacey laugh
        stacey "We did it, Beans!"

        show stacey happy
        stacey "We're going to live!"

        narrate "You emerge from the trees, exhausted, battered."
        narrate "But not broken."

        call screen good_ending("goodEnd") with dissolve
        return

    label .ending_killerCaughtInWoods:
        $ crossfade("audio/music/Hallowbean_Drone.ogg")

        # You both die
        narrate "You have made a terrible decision."
        narrate "The enormous masked figure appears from the trees, impossibly fast."

        narrate "The distance closes between you."

        stacey "Beans! Watch out!"

        narrate "The axe whistles through the air towards you."
        narrate "You're not going to make it."

        play sound "audio/stingers/dread.wav"
        call screen you_died()
        return