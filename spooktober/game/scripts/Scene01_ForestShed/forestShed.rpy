# Characters
define character.stacey = Character("Stacey")
default stacey.approval = 0
default stacey.respondedProactivePassive = False

define character.beans = Character("Beans")
default beans.proactivePassive = 0
default beans.equipped = []
default beans.backpack = []

# Constants
define proactiveThreshold = 3
define passiveThreshold = -3

define staceyRunApprovalThreshold = -2

# Narrative state variables
default beansSearchedShed = False
default foundLockers = False
default searchedDrums = False
default cutHand = False

default staceyDateAgreed = False

default killerDistance = 3

label scene_forestShed:

# Utility labels not associated with a specific point in the narrative
label .util_updateProactivePassive(delta = 0):
    $ beans.proactivePassive += delta
    "TODO: Beans' proactivePassive scored is [beans.proactivePassive]"

    if not stacey.respondedProactivePassive:
        if beans.proactivePassive < passiveThreshold:
            $ stacey.respondedProactivePassive = True
            stacey "TODO: You are very passive."
        elif beans.proactivePassive > proactiveThreshold:
            $ stacey.respondedProactivePassive = True
            stacey "TODO: You are very proactive."

    return

label .util_updateKillerDistance(delta = 0):
    $ killerDistance += delta
    "TODO: Killer distance is [killerDistance]"

    if killerDistance <= 0:
        jump .e_killerArrives
    return

label .util_equipItem(item = "Default"):
    python:
        if not item in beans.equipped:
            beans.equipped.append(item)
    "TODO: [item] equipped"
    return

label .util_addItemToBag(item = "Default"):
    python:
        if not item in beans.backpack:
            beans.backpack.append(item)
    "TODO: [item] added to backpack"
    return

#--------------------------------------------------------
# Narrative Nodes
#--------------------------------------------------------

# 1 Running through the woods
label .a_runningThroughWoods:
    "PLACEHOLDER: Section 1"
    "PLACEHOLDER: Beans and Stacey running scared through the woods."

    jump forestShed_runningThroughWoods

# 2 Discovering the shed
label .b_discoveringShed:
    "Section 2"
    "Beans and Stacey discover the shed"

    jump forestShed_discoveringShed

# 3 Searching the Shed
label .c_searchingShed:
    "Section 3"
    "Beans and/or Stacey search the shed"
    jump forestShed_searchingShed

# 4 Searching the surrounding area
label .d_areaSearch:
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


    label .continueIntoForest:


label .e_killerArrives:
    "TODO: The killer is upon you, oh no. What do you do?"

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
            "TODO: You see that one of the lockers is full of stuff"
            "TODO: You have no choice but to squeeze into a locker with Stacey"
            if stacey.approval < staceyRunApprovalThreshold:
                jump endings_forestShed.ending_staceyRuns_lowApproval
            else:
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
            if stacey.approval < staceyRunApprovalThreshold:
                jump endings_forestShed.ending_oilDrums_lowApproval
            else:
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
        elif stacey.approval < staceyRunApprovalThreshold:
            jump endings_forestShed.ending_staceyRuns_lowApproval
        else:
            jump .underTabletalk

label .lockerTalk:
    "TODO: Flirt with Stacey but also try not to die"
    jump forestShed_lockerTalk

label .runIntoTheWoods:
    if stacey.approval < staceyRunApprovalThreshold:
        "TODO: Stacey runs off and leaves you behind"
    elif "Lantern" in beans.equipped:
        "TODO: You have to dodge a bear trap"
    else:
        if beans.proactivePassive < 0:
            "Stacey goes first and steps on the bear trap, which you can't see, on account of not having a lantern."
            jump .staceyBearTrap
        else:
            "You go first and step on a bear trap, which you can't see on account of not having a lantern."
            if "Boots" in beans.equipped:
                "TODO"
                "The boots protect your leg from the bear trap."
                "Stacey knows how to disarm them for some reason. You both get away."
                jump endings_forestShed.ending_savedFromBearTrap
            else:
                "TODO"
                "The bear trap chews your leg straight up"
                "You die RIP"
                jump endings_forestShed.ending_beansStuckInBearTrap

label .staceyBearTrap:
    "TODO: Stacey steps on a bear trap and falls over, shrieking"
    menu:
        "Try and free her":
            "TODO: It's useless, the jaws are stuck tight and you're weak and pathetic."
            menu:
                "Keep trying to free her":
                    "You both die"
                    "RIP"
                    jump endings_forestShed.ending_staceyStuckInBearTrap
                "Give up and save yourself":
                    jump .runningFromBearTrap
        "Leave her and run":
            jump .runningFromBearTrap
    
    label .runningFromBearTrap:
        if "Boots" in beans.equipped:
            "You trip and fall on account of the stupid old boots"
            "You both die. RIP"
            jump endings_forestShed.ending_runFromBearTrap_boots
        else:
            "You get away, leaving Stacey to her fate"
            "RIP Stacey"
            jump endings_forestShed.ending_runFromBearTrap_noBoots

label .underTabletalk:
    