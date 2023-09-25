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
default smashedLantern = False

default staceyDateAgreed = False

default killerDistance = 3

label scene_forestShed:

# Utility labels not associated with a specific point in the narrative
label .util_updateProactivePassive(delta = 0):
    $ beans.proactivePassive += delta
    "TODO: Beans' proactivePassive score is [beans.proactivePassive]"

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
    else:
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
    jump forestShed_searchingArea

label .e_killerArrives:
    jump forestShed_killerArrives

label .lockerTalk:
    "TODO: Flirt with Stacey but also try not to die"
    jump forestShed_lockerTalk

label .runIntoTheWoods:
    if stacey.approval < staceyRunApprovalThreshold:
        "TODO: Stacey runs off and leaves you behind"
    elif "Lantern" in beans.equipped:
        "TODO: You have to dodge a bear trap"
        # TODO DEAD END
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
    "TODO: Under table talk"
    