# 4 Searching the surrounding area
label forestShed_searchingArea:
    if "Lantern" in beans.equipped:
        jump .areaSearch_withLantern
    else:
        jump .areaSearch_noLantern

    # Searching with a lantern
    label .areaSearch_withLantern:
        "{i}The lantern throws a reassuring glow around you.{/i}"
        menu:
            "Search the outside of the shed":
                jump .searchAroundShed
            "Search the oil drums":
                jump .searchOilDrums
            "Continue deeper into the forest":
                jump scene_forestShed.continueIntoForest
        
        # Search locations
        label .searchOilDrums:
            "TODO: You discover three oil drums - one is empty, one has something in but smells disgusting, one has something clunking around in it"    
            call scene_forestShed.util_updateKillerDistance(-1)
            $ searchedDrums = True
            menu:
                "Open the oil drum yourself":
                    call scene_forestShed.util_updateProactivePassive(1)
                    jump .findBoots
                "Ask Stacey to open the oil drum":
                    call scene_forestShed.util_updateProactivePassive(-1)
                    jump .findBoots
                "Leave the oil drum":
                    return
            label .findBoots:
                "TODO:  Beans finds a manky old pair of boots"
                menu:
                    "Put on the boots":
                        $ stacey.approval -= 1
                        call scene_forestShed.util_equipItem("Boots")
                    "Put the boots in your backpack":
                        call scene_forestShed.util_addItemToBag("Boots")
                    "Leave the boots in the oil drum":
                        return
    
    label .areaSearch_noLantern:
        "The last rays of sunlight have dwindled."
        "It's getting real hard to see..."
        menu:
            "Search the shed for another lantern" if not beansSearchedShed:
                jump .searchShed_noLantern
            "Attempt to search the outside of the shed":
                jump scene_forestShed.searchAroundShed

            "Continue into the forest":
                jump scene_forestShed.continueIntoForest
        
        # Search shed without lantern
        label .searchShed_noLantern:
            call scene_forestShed.util_updateKillerDistance(-1)
            "TODO: You cut your hand on the bandsaw on the workbench"
            "TODO: Stacey has to bandage it with a headband"
            $ cutHand = True
            
            # Respond to Stacey's help
            menu:
                "Thank Stacey for her help":
                    $ stacey.approval += 1
                    "TODO: Stacey is pleased"
                "Kiss Stacey":
                    $ stacey.approval -= 5
                    call scene_forestShed.util_updateKillerDistance(-1)
                    "TODO: Stacey is horrified and pushed you away."
                "Say nothing":
                    $ stacey.approval -= 1
                    "TODO: Stacey is disappointed in you and the silence is awkward."

    # Search around the shed
    label .searchAroundShed:
    $ foundLockers = True
    "TODO: You find two storage lockers, large enough to hide bodies in."
    call scene_forestShed.util_updateKillerDistance(-1)