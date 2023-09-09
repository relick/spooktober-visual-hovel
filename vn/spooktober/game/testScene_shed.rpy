# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define character.stacey = Character("Stacey")
default stacey.approval = 0

default menuset = set()

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg forest

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "I'm so tired... and my feet hurt..."

    "This tin of beans is so heavy..."

    "The moon is shining right in my eyes..."

    centered """
    Even through the canopy of trees, the moon is surprisingly bright.

    Something large and building-shaped appears, silhouetted in the moonlight in front of you.
    """

    show stacey happy

    stacey "Oh my god! A house! People!" with vpunch

    menu:
        "We're saved!":
            jump saved
        "Careful - we don't know if we can trust them":
            jump careful



    stacey "My approval of you is [stacey.approval]"
    # This ends the game.

    return

label saved:
    stacey "{i}Squealing{/i}"
    
    "Stacey wait!"

    "How am I meant to keep up with a hyperactive cheerleader?!"

    centered "You struggle after her."

    centered "It quickly becomes apparent that this lightless building is deserted."

    show stacey sad

    stacey """
    It's abandoned. 
    
    We're doomed. 
    
    And what kind of shitty, tiny house is this anyway?
    """

    jump shed

    return

label careful:
    stacey "True."
    stacey "They might be like, weird forest people who marry their uncles."

    centered "You creep forward, making each footstep as silent as possible."

    centered "The light of the moon glimmers off Stacey's hoop earrings, and dances across the chemically treated curls of her hair. "

    "She's like a peroxide angel..."

    show stacey angry
    stacey "Ugh."

    show stacey
    stacey "There's obviously nobody here. And this place is a DUMP."
    
    jump shed

    return

label shed:
    scene bg shed
    
    centered "What you  have found is a shed."

    centered "It stands in a little clearing full of junk. Rusted oil drums, stacked timber, a collection of sad looking jerrycans."

    "Looks like a toolshed"

    "And some kind of makeshift work yard..."

    "Maybe we can find something useful here."

    menu shed_search: 
        "What should I do?"

        set menuset
        "Investigate the shed":
            jump shed_search
        "Check the oil drums":
            jump shed_search
        "All out of options!":
            return

    return
