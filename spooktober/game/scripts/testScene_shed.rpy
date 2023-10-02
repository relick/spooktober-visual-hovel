# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#define character.stacey = Character("Stacey")
#default stacey.approval = 0

default menuset = set()

#default searched_shed = False
#default found_locker = False
# The game starts here.

label testScene_shed:
    jump scene_forestShed.a_runningThroughWoods

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

    show stacey neutral

    stacey "Oh my god! A house! People!" with vpunch

    # Make a timed choice with 3 seconds, jumping to 'saved' if they time out
    show screen timed_choice(3.0, "saved")

    menu:
        "We're saved!":
            hide screen timed_choice
            jump saved
        "Careful - we don't know if we can trust them":
            hide screen timed_choice
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

    centered "The light of the moon glimmers off Stacey's hoop earrings, and dances across the chemically treated curls of her hair."

    show stacey angry
    stacey "Ugh."

    show stacey
    stacey "There's obviously nobody here. And this place is a DUMP."
    
    jump shed

    return

label shed:
    scene bg forest
    call screen panel("shed") with dissolve
    
    centered "What you  have found is a shed."

    centered "It stands in a little clearing full of junk. Rusted oil drums, stacked timber, a collection of sad looking jerrycans."

    "Looks like a toolshed..."

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

label investigate_shed:
    scene bg shed_interior
    $ searched_shed = True

    "Oh man, this shed is TINY."
    "There's barely room for the workbench in here."

    show stacey disgusted
    stacey "Ugh! Look at this dust."
    stacey "Don't touch any of those tools, you'll get tetanus."  

    menu:
        "Pick up a rusted saw from the bench.":
            show stacey annoyed
            stacey "What did I JUST say?"
            stacey "You're literally hopeless."
            $ stacey.approval -= 1

            "Well... this might come in handy."
            jump outside_shed
        "Leave the tools alone.":
            centered "You and Stacey search the shed."

            "Everything here is so old..."
            "Is there nothing useful at all?"
            jump outside_shed
    return

label outside_shed:
    $ found_locker = True
    centered "Around the side of the shed are two tall storage lockers."

    stacey "You could fit a whole body in one of those."
    stacey "What?"
    stacey "Don't tell me you weren't thinking it too."
    return