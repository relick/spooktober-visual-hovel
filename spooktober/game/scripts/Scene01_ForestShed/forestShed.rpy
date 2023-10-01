# Characters
define character.stacey = Character("Stacey", callback=mid_beep)
default stacey.approval = 0
default stacey.respondedProactivePassive = False

define character.beans = Character("Beans", callback=high_beep)
default beans.proactivePassive = 0
default beans.equipped = []
default beans.backpack = []
define character.think = Character(what_prefix="(", what_suffix=")")

define character.narrate = Character(what_color="#79afff", what_prefix="{i}", what_suffix="{/i}", callback=typewriter_beep)

define character.debug = Character(condition="True") # set to False to disable debug statements

define character.centered = Character(kind=centered, callback=typewriter_beep)

# Constants
define proactiveThreshold = 3
define passiveThreshold = -3

define staceyRunApprovalThreshold = -2
define staceyKissApprovalThreshold = 3

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

    python:
        """
    if not stacey.respondedProactivePassive:
        if beans.proactivePassive < passiveThreshold:
            $ stacey.respondedProactivePassive = True
            stacey "TODO: You are very passive."
        elif beans.proactivePassive > proactiveThreshold:
            $ stacey.respondedProactivePassive = True
            stacey "TODO: You are very proactive."
        """
    return

label .util_updateKillerDistance(delta = 0):
    $ killerDistance += delta
    # debug "TODO: Killer distance is [killerDistance]"

    if killerDistance <= 0:
        jump .e_killerArrives
    else:
        return

label .util_equipItem(item = "Default"):
    python:
        if not item in beans.equipped:
            beans.equipped.append(item)
    narrate "You've equipped the [item]"
    return

label .util_addItemToBag(item = "Default"):
    python:
        if not item in beans.backpack:
            beans.backpack.append(item)
    return

#--------------------------------------------------------
# Narrative Nodes
#--------------------------------------------------------

# 0 Introduction
label .backstoryIntro:
    centered "It's the summer of 1986"
    centered "The music is good and the perms are bad"
    centered "Like {i}real{/i} bad"
    centered "High School is behind you"
    centered "College is ahead of you"
    centered "And in between?"
    centered "It was meant to be the Best Summer Ever"

    centered "That was what Gerald promised when he invited you all out here"
    centered "To his family's {color=#f6ba00}cabin in the woods{/color}"
    centered "That was before he veered off the road with you all in the car"
    centered "That was before the first of your friends turned up dead"
    centered "That was before the mysterious figure began pursuing you"

    centered "Forget college - your only life goal now is survival"
    centered "Oh yeah..."
    centered "And this is probably your last chance to try it on with your crush"
    centered "So, you know,"
    centered "Priorities and whatever"

    jump .a_runningThroughWoods


# 1 Running through the woods
label .a_runningThroughWoods:
    jump forestShed_runningThroughWoods

# 2 Discovering the shed
label .b_discoveringShed:
    jump forestShed_discoveringShed

# 3 Searching the Shed
label .c_searchingShed:
    jump forestShed_searchingShed

# 4 Searching the surrounding area
label .d_areaSearch:
    think "The sunlight's basically gone."
    think "It's getting real hard to see..."    
    jump forestShed_searchingArea

label .e_killerArrives:
    jump forestShed_killerArrives

label .lockerTalk:
    jump forestShed_lockerTalk

label .runIntoTheWoods:
    jump forestShed_runIntoWoods

label .staceyBearTrap:
    narrate "TODO: Stacey steps on a bear trap and falls over, shrieking"
    menu:
        "Try and free her":
            narrate "TODO: It's useless, the jaws are stuck tight and you're weak and pathetic."
            menu:
                "Keep trying to free her":
                    narrate "You both die"
                    narrate "RIP"
                    jump endings_forestShed.ending_staceyStuckInBearTrap
                "Give up and save yourself":
                    jump .runningFromBearTrap
        "Leave her and run":
            jump .runningFromBearTrap
    
    label .runningFromBearTrap:
        if "Boots" in beans.equipped:
            narrate "You trip and fall on account of the stupid old boots"
            narrate "You both die. RIP"
            jump endings_forestShed.ending_runFromBearTrap_boots
        else:
            narrate "You get away, leaving Stacey to her fate"
            narrate "RIP Stacey"
            jump endings_forestShed.ending_runFromBearTrap_noBoots
    