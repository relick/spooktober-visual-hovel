# Audio
# --------

# Backgrounds
# --------
# shed

# Sprites
# --------
# stacey thoughtful

label forestShed_discoveringShed:
    scene bg forest
    centered "What you have found is a shed."

    hide beans
    think "This forest clearing is kind of cute,"
    think "Shame it's full of junk."
    think "Old jerrycans, rotting firewood... and are those oil drums?"

    show stacey thoughtful
    stacey "Who puts a toolshed out in the woods?"
    stacey "There's gotta be something here we can use."

    jump scene_forestShed.c_searchingShed