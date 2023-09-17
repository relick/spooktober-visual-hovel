# Audio
# --------
# panting (beans/stacey)

# Backgrounds
# --------
# forest
# shedSilhouette
# shed

# Sprites
# --------
# stacey tired
# stacey excited
# stacey disappointed

label forestShed_runningThroughWoods:
    scene bg forest
    # AUDIO: Panting?

    "I'm so tired... and my feet hurt..."
    "This tin of beans is so heavy..."
    "It's getting dark so fast..."

    show stacey tired
    stacey "I'm sure the road was this way..."

    show stacey excited
    stacey "Wait!" with vpunch

    scene bg shedSilhouette
    "Is that... a house?"

    menu:
        "We're saved!":
            jump .saved
        "Careful - we don't know if we can trust them":
            jump .careful

    # "We're saved!"
    label .saved:
        stacey "Maybe they have a telephone! We can call the police!"
        
        beans "Stacey, wait!"
        "Ugh... how am I meant to keep up with a champion cheerleader?"
        "I'm going as fast as I can!"

        beans "Huff.. huff.."
        scene bg shed
        show stacey disappointed

        stacey "It's obviously abandoned."
        

        "It looks pretty small for a house, too"

        jump scene_forestShed.b_discoveringShed

    # "Careful - we don't know if we can trust them"
    label .careful:
        stacey "True."
        stacey "They might be weird forest people who marry their uncles."

        "I creep forward, making each footstep as silent as possible."

        "The moonlight is glimmering off Stacey's hoop earrings"
        "The way it dances across the chemically treated curls of her hair.... "
        "It's almost magical"

        scene bg shed
        show stacey disgusted
        stacey "Ugh."
        stacey "This place is like, abandonedville. And it's {i}hella{/i} grody."
        
        jump scene_forestShed.b_discoveringShed