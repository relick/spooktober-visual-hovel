# Audio
# --------
# 

# Backgrounds/ Images
# --------
# Shed exterior
# Oil drums close up
# Boots (can be picked up or equipped)

# Sprites
# --------
# stacey determined
# stacey happy



# 4 Searching the surrounding area
label forestShed_searchingArea:
    if "Lantern" in beans.equipped:
        jump .areaSearch_withLantern
    else:
        jump .areaSearch_noLantern

    # Searching with a lantern
    label .areaSearch_withLantern:
        scene bg shed
        "{i}The lantern throws a reassuring glow around you.{/i}"
        "{i}This should make it easier to search.{/i}"
        menu:
            "Search the outside of the shed":
                jump .searchAroundShed
            "Search the oil drums":
                jump .searchOilDrums
            "Continue deeper into the forest":
                jump scene_forestShed.continueIntoForest
        
        # Search locations
        label .searchOilDrums:
            beans "Let's check out those oil drums."
            stacey "Sure, I guess."
            scene bg oilDrums
            "{i}The three oil drums are ancient, grimy and coated in rust.{/i}"
            stacey "Oh man, something smells {i}gnarly{/i}"
            "Something absolutely rank is in one of those drums..."

            menu: 
                "Open the stinky drum":
                    "{i}You go to pry open the lid from which the rancid odour seems to emanate.{/i}"
                    "{i}It's so hideously rusted that it basically falls apart in your hands.{/i}"
                    "{i}You and Stacey peer into the open container.{/i}"
                    show stacey nauseous
                    stacey "Beans that is {i}nasty!{/i}"
                    stacey "Uh-uh. No way. No even. I'm gonna hurl."

                    "That thing used to be a raccoon."
                    "I can make out its cute little face under the maggots - well, it was cute once."
                    "Those empty eye sockets are staring into my soul..."

                    beans "Urgh..."
                    "{i}You try and put the raccoon corpse out of your mind. It doesn't really work.{/i}"
                    "{i}It's still there, staring at you with its maggot-eaten eyes.{/i}"

                    beans "Well, on to the next one."
                "Avoid the rancid drum":
                    beans "No way am I looking in there."
                    $ stacey.approval += 1

            "Two drums left."
            stacey "Let's see if there's anything in these bad boys"
            "{i}CLANG{/i}"
            stacey "Empty!"
            beans "Did you just {i}kick{/i} that?"
            
            show stacey annoyed
            stacey "Well I'm not gonna touch it with my {i}hands.{/i} Duh."
            "{i}CLANG-THUNK{/i}"
   
            show stacey happy
            stacey "Something in this one! Check it out, Beans."

            call scene_forestShed.util_updateKillerDistance(-1)
            $ searchedDrums = True
            menu:
                "Open the oil drum yourself":
                    call scene_forestShed.util_updateProactivePassive(1)
                    show beans worried
                    beans "Oh man, I hope this isn't something gross."
                    beans "I have a nervous stomach you know."

                    "This lid {i}really{/i} doesn't want to come off, but I'll show it who's boss."
                    "{i}With a rusty screech, the lid of the drum comes free{/i}"
                    "{i}You and Stacey peer at your spoils.{/i}"
                    jump .findBoots
                "Ask Stacey to open the oil drum":
                    show beans apologetic
                    beans "Um Stacey, could you - uh - get the lid? "
                    
                    show stacey annoyed
                    stacey "Wow Beans. Do you want me to tie your shoes and cut your food up too?"

                    "Ouch."
                    "She is stronger than me though... and just like, better at stuff in general."

                    "{i}Stacey deftly prises the lid from the drum.{/i}"
                    stacey "Alrighty, let's see what we're working with."

                    call scene_forestShed.util_updateProactivePassive(-1)
                    jump .findBoots
                "Leave the oil drum":
                    return

            label .findBoots:
                show stacey bored
                stacey "Wow. Gross old boots. This will save us."
                beans "Is that sarcasm?"
                stacey "{i}Duh.{/i}"
                
                show bg boots
                "{i}It's true. You have found gross old boots.{/i}"
                "Leather, steel toecaps... now that's some practical footwear."
                menu:
                    "Put on the boots":
                        $ stacey.approval -= 1
                        beans "Shame to let them go to waste!"
                        "{i}You retrieve the dusty old boots from the drum and put them on.{/i}"
                        
                        show stacey disgusted
                        stacey "BEANS."
                        stacey "What. Is. Wrong. With. You."

                        "These are like... five sizes too big."
                        "I don't really know why I did that."
                        call scene_forestShed.util_equipItem("Boots")
                    "Put the boots in your backpack":
                        "They don't look like my size."
                        "Hey, might come in handy later though."

                        "{i}You retrieve the boots and add them to your backpack, which is now awkwardly bulky and pretty heavy.{/i}"
                        stacey "Um. Okay then..."
     
                        call scene_forestShed.util_addItemToBag("Boots")

                    "Leave the boots in the oil drum":
                        beans "Yeah, I'm not touching those."

                        stacey "Good, because they're {i}so{/i} not your colour."
                        "Oh Stacey... how stereotypical can she get?"

                        stacey "You know I'm joking, right?"
                        stacey "What use could we possibly have for decaying footwear that's clearly five sizes too big for either of us."
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