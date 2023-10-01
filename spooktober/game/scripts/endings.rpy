label endings_forestShed:
    label .ending_oilDrums_mediocre:
        narrate "The guilt will come later."
        narrate "You slip out of reach, stumbling over tree roots and dried leaves."
        narrate "Behind you comes a scream, cut off by a wet squelch."
        narrate "You run into the woods as fast as you can. "
        narrate "..."

        narrate "It seems you and Stacey were not meant to be."
        
        # vertical columns
        call screen game_over("shark") with blinds
        return
    
    label .ending_oilDrums_heroic:
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
        call screen game_over("shark") with squares
        return

    label .ending_oilDrums_terribad:
        narrate "The figure looms over you"
        narrate "Expressionless eyes leer at you from the mask"
        narrate "It's impossible to tell whether they take any pleasure in this"

        narrate "This is the end."

        # ..squares
        call screen game_over("shark") with squares
        return       

    label .ending_oilDrums_terribad_hands:
        narrate "The figure looms over you"
        narrate "Expressionless eyes leer at you from the mask"
        narrate "It's impossible to tell whether they take any pleasure in this"   

        narrate "Stacey wordlessly takes your hand in hers"
        narrate "She squeezes it tightly"

        show stacey sad
        stacey "I... wish I'd known you better, Beans."
        hide stacey

        narrate "This is the end."
        return

    label .ending_staceyRuns_lowApproval:
        narrate "TODO: Stacey bolts from your hiding place and gets fuckin murdered"
        narrate "TODO: You live to tell the tale, but at what cost?"
        # weird pixellation
        call screen game_over("shark") with pixellate
        return

    label .ending_underTable_bootsInBag:
        narrate "TODO: The killer sees your bag and discovers your hiding place"
        narrate "RIP"
        # basically just a direct fade
        call screen game_over("shark") with dissolve
        return

    label .ending_underTable_cutHand:
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
        
        # fades to black then fades into image
        call screen game_over("shark") with fade
        return

    label .ending_runIntoWoods_boots:
        narrate "TODO: You both run into the woods but you trip over the poorly fitting boots"
        narrate "Bad end."
        call screen game_over("shark") with dissolve
        return

    label .ending_runFromBearTrap_boots:
        narrate "TODO: You try and run, leaving Stacey in the bear trap"
        narrate "Unfortunately you trip on the stupid old boots you're wearing. The killer catches you anyway."
        narrate "Bad end."
        call screen game_over("shark") with dissolve
        return

    label .ending_runFromBearTrap_noBoots:
        narrate "TODO: You get away, leaving Stacey stuck in the bear trap"
        narrate "You live, but Stacey does not"
        call screen game_over("shark") with dissolve
        return

    label .ending_staceyStuckInBearTrap:
        narrate "TODO: You try to free Stacey, but don't manage it."
        narrate "The killer catches up and kills you both."
        narrate "Could you have made it if you left her behind?"
        call screen game_over("shark") with dissolve
        return

    label .ending_beansStuckInBearTrap:
        narrate "TODO: With your leg absolutely destroyed by the bear trap, there's no way you can get away from the killer, even with Stacey's help"
        narrate "Unfortunately you're a goner"
        call screen game_over("shark") with dissolve
        return

    label .ending_beansStuckInBearTrap_noKiller:
        narrate "TODO: The bear trap injury is deep, and you"
        narrate "Unfortunately you're a goner"
        call screen game_over("shark") with dissolve
        return

    label .ending_savedFromBearTrap:
        narrate "TODO: Luckily the old leather boots protect your leg from any serious damage."
        narrate "For some reason Stacey knows how to disarm a bear trap. You just push down on both vertical springs, apparently."
        narrate "She frees you and you disappear into the forest together, safe - for now."
        call screen game_over("shark") with dissolve
        return

    label .ending_lockerEscape_romance:
        narrate "TODO: You escape the locker, with a promise of a date on the cards. Yay!"
        call screen game_over("shark") with dissolve
        return

    label .ending_lockerEscape_noRomance:
        narrate "TODO: You escape the locker, as friends. Yay, I guess?"
        call screen game_over("shark") with dissolve
        return