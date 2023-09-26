label endings_forestShed:
    label .ending_oilDrums_mediocre:
        narrate "TODO:"
        narrate "You scramble over the oil drums, slipping out of reach as the killer grabs Stacey."
        narrate "You hear her scream, cut off by a wet squelch, and scramble into the woods as fast as you can. "
        # vertical columns
        call screen game_over("shark") with blinds
        return
    
    label .ending_oilDrums_lowApproval:
        narrate "TODO:"
        narrate """
        Stacey vaults over the drums, her cheerleader training paying off in her athleticism.
        You, however, are not a cheerleader. 

        As you desperately try and claw through the rusted metal drums, heaving footsteps - and heavy breathing - arrive behind you. 
        An enormous hand lifts you off the ground by the back of your shirt. 
        The air stinks of rotten meat and sweet, metallic blood. 
        A blade whistles through the air.

        This is your time.
        """   
        # ..squares
        call screen game_over("shark") with squares
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
        narrate "TODO: The killer sees the blood from your saw accident and discovers your hiding place"
        narrate "RIP"
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