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

default killerDistance = 5 # 3

label scene_forestShed:

# Utility labels not associated with a specific point in the narrative
label .util_updateProactivePassive(delta = 0):
    $ beans.proactivePassive += delta
    debug "TODO: Beans' proactivePassive score is [beans.proactivePassive]"

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
    debug "TODO: Killer distance is [killerDistance]"

    if killerDistance <= 0:
        jump .e_killerArrives
    else:
        return

label .util_equipItem(item = "Default"):
    python:
        if not item in beans.equipped:
            beans.equipped.append(item)
    debug "TODO: [item] equipped"
    return

label .util_addItemToBag(item = "Default"):
    python:
        if not item in beans.backpack:
            beans.backpack.append(item)
    debug "TODO: [item] added to backpack"
    return

#--------------------------------------------------------
# Narrative Nodes
#--------------------------------------------------------

# 1 Running through the woods
label .a_runningThroughWoods:
    debug "PLACEHOLDER: Section 1"
    debug "PLACEHOLDER: Beans and Stacey running scared through the woods."

    jump forestShed_runningThroughWoods

# 2 Discovering the shed
label .b_discoveringShed:
    debug "Section 2"
    debug "Beans and Stacey discover the shed"

    jump forestShed_discoveringShed

# 3 Searching the Shed
label .c_searchingShed:
    debug "Section 3"
    debug "Beans and/or Stacey search the shed"
    jump forestShed_searchingShed

# 4 Searching the surrounding area
label .d_areaSearch:
    think "The last rays of sunlight have dwindled."
    think "It's getting real hard to see..."    
    jump forestShed_searchingArea

label .e_killerArrives:
    jump forestShed_killerArrives

label .lockerTalk:
    debug "TODO: Flirt with Stacey but also try not to die"
    jump forestShed_lockerTalk

label .runIntoTheWoods:
    if stacey.approval < staceyRunApprovalThreshold:
        narrate "TODO: Stacey runs off and leaves you behind"
    elif "Lantern" in beans.equipped:
        narrate "TODO: You have to dodge a bear trap"
        # TODO DEAD END
    else:
        if beans.proactivePassive < 0:
            narrate "Stacey goes first and steps on the bear trap, which you can't see, on account of not having a lantern."
            jump .staceyBearTrap
        else:
            narrate "You go first and step on a bear trap, which you can't see on account of not having a lantern."
            if "Boots" in beans.equipped:
                narrate "TODO"
                narrate "The boots protect your leg from the bear trap."
                narrate "Stacey knows how to disarm them for some reason. You both get away."
                jump endings_forestShed.ending_savedFromBearTrap
            else:
                narrate "TODO"
                narrate "The bear trap chews your leg straight up"
                narrate "You die RIP"
                jump endings_forestShed.ending_beansStuckInBearTrap

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

label .underTabletalk:
    narrate "TODO: Under table talk"
    