label endings_forestShed:
    label .ending_oilDrums_mediocre:
        "TODO:"
        "You scramble over the oil drums, slipping out of reach as the killer grabs Stacey."
        "You hear her scream, cut off by a wet squelch, and scramble into the woods as fast as you can. "
        # vertical columns
        call screen game_over("shark") with blinds
        return
    
    label .ending_oilDrums_lowApproval:
        "TODO:"
        """
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
        "TODO: Stacey bolts from your hiding place and gets fuckin murdered"
        "TODO: You live to tell the tale, but at what cost?"
        # weird pixellation
        call screen game_over("shark") with pixellate
        return

    label .ending_underTable_bootsInBag:
        "TODO: The killer sees your bag and discovers your hiding place"
        "RIP"
        # basically just a direct fade
        call screen game_over("shark") with dissolve
        return

    label .ending_underTable_cutHand:
        "TODO: The killer sees the blood from your saw accident and discovers your hiding place"
        "RIP"
        # fades to black then fades into image
        call screen game_over("shark") with fade
        return

    label .ending_runIntoWoods_boots:
        "TODO: You both run into the woods but you trip over the poorly fitting boots"
        "Bad end."
        call screen game_over("shark") with dissolve
        return

    label .ending_runFromBearTrap_boots:
        "TODO: You try and run, leaving Stacey in the bear trap"
        "Unfortunately you trip on the stupid old boots you're wearing. The killer catches you anyway."
        "Bad end."
        call screen game_over("shark") with dissolve
        return

    label .ending_runFromBearTrap_noBoots:
        "TODO: You get away, leaving Stacey stuck in the bear trap"
        "You live, but Stacey does not"
        call screen game_over("shark") with dissolve
        return

    label .ending_staceyStuckInBearTrap:
        "TODO: You try to free Stacey, but don't manage it."
        "The killer catches up and kills you both."
        "Could you have made it if you left her behind?"
        call screen game_over("shark") with dissolve
        return

    label .ending_beansStuckInBearTrap:
        "TODO: With your leg absolutely destroyed by the bear trap, there's no way you can get away from the killer, even with Stacey's help"
        "Unfortunately you're a goner"
        call screen game_over("shark") with dissolve
        return

    label .ending_savedFromBearTrap:
        "TODO: Luckily the old leather boots protect your leg from any serious damage."
        "For some reason Stacey knows how to disarm a bear trap. You just push down on both vertical springs, apparently."
        "She frees you and you disappear into the forest together, safe - for now."
        call screen game_over("shark") with dissolve
        return

    label .ending_lockerEscape_romance:
        "TODO: You escape the locker, with a promise of a date on the cards. Yay!"
        call screen game_over("shark") with dissolve
        return

    label .ending_lockerEscape_noRomance:
        "TODO: You escape the locker, as friends. Yay, I guess?"
        call screen game_over("shark") with dissolve
        return