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
        scene bg forest
        call screen panel("shed") with dissolve
        narrate "The lantern throws a reassuring glow around you."
        narrate "This should make it easier to search."
        menu:
            "Search the outside of the shed" if not foundLockers:
                jump .searchAroundShed
            "Search the oil drums" if not searchedDrums:
                jump .searchOilDrums
            "Continue deeper into the forest":
                jump .continueIntoForest
        
        # Search locations
        label .searchOilDrums:
            show beans kewlpewpew
            beans "Let's check out those oil drums."
            hide beans
            stacey "Sure, I guess."
            scene bg oilDrums
            narrate "The three oil drums are ancient, grimy and coated in rust."
            stacey "Oh man, something smells {i}gnarly{/i}"
            think "Something absolutely rank is in one of those drums..."

            menu: 
                "Open the stinky drum":
                    narrate "You go to pry open the lid from which the rancid odour seems to emanate."
                    narrate "It's so hideously rusted that it basically falls apart in your hands."
                    narrate "You and Stacey peer into the open container."
                    show stacey nauseous
                    stacey "Beans that is {i}nasty!{/i}"
                    stacey "Uh-uh. No way. No even. I'm gonna hurl."

                    think "That thing used to be a raccoon."
                    think "I can make out its cute little face under the maggots - well, it was cute once."
                    think "Those empty eye sockets are staring into my soul..."

                    show beans meanbean
                    beans "Urgh..."
                    hide beans
                    narrate "You try and put the raccoon corpse out of your mind. It doesn't really work."
                    narrate "It's still there, staring at you with its maggot-eaten eyes."

                    show beans sad
                    beans "Well, on to the next one."
                    hide beans
                "Avoid the rancid drum":
                    show beans serious2
                    beans "No way am I looking in there."
                    hide beans
                    $ stacey.approval += 1

            think "Two drums left."
            stacey "Let's see if there's anything in these bad boys"
            narrate "CLANG"
            stacey "Empty!"
            show beans blush3 # idk, is kicking things hot? maybe
            beans "Did you just {i}kick{/i} that?"
            hide beans
            
            show stacey annoyed
            stacey "Well I'm not gonna touch it with my {i}hands.{/i} Duh."
            narrate "CLANG-THUNK"
   
            show stacey happy
            stacey "Something in this one! Check it out, Beans."

            call scene_forestShed.util_updateKillerDistance(-1)
            $ searchedDrums = True
            menu:
                "Open the oil drum yourself":
                    call scene_forestShed.util_updateProactivePassive(1)
                    show beans sad # worried
                    beans "Oh man, I hope this isn't something gross."
                    beans "I have a nervous stomach you know."
                    hide beans

                    think "This lid {i}really{/i} doesn't want to come off, but I'll show it who's boss."
                    narrate "With a rusty screech, the lid of the drum comes free"
                    narrate "You and Stacey peer at your spoils."
                    jump .findBoots
                "Ask Stacey to open the oil drum":
                    show beans blush # apologetic
                    beans "Um Stacey, could you - uh - get the lid? "
                    hide beans
                    
                    show stacey annoyed
                    stacey "Wow Beans. Do you want me to tie your shoes and cut your food up too?"

                    think "Ouch."
                    think "She is stronger than me though... and just like, better at stuff in general."

                    narrate "Stacey deftly prises the lid from the drum."
                    stacey "Alrighty, let's see what we're working with."

                    call scene_forestShed.util_updateProactivePassive(-1)
                    jump .findBoots
                "Leave the oil drum":
                    think "Oh boy, I really don't want to open that thing up."
                    show beans blush
                    beans "Uh... I don't know..."
                    $ stacey.approval += 1
                    hide beans

                    show stacey annoyed
                    stacey "Oh come ON Beans."
                    stacey "What's it going to do, kill you?"

                    show beans tired
                    beans "I'm just being cautious! It could be... I dunno, toxic waste."
                    hide beans

                    stacey "Toxic waste? Really?"
                    show stacey sigh
                    stacey "You really are a dweeb."

                    jump forestShed_searchingArea

            label .findBoots:
                show stacey bored
                stacey "Wow. Gross old boots. This will save us."
                show beans kewl
                beans "Is that sarcasm?"
                hide beans
                stacey "{i}Duh.{/i}"
                
                call screen panel("boots") with dissolve
                narrate "It's true. You have found gross old boots."
                think "Leather, steel toecaps... now that's some practical footwear."
                menu:
                    "Put on the boots":
                        $ stacey.approval -= 1
                        show beans kewl
                        beans "Shame to let them go to waste!"
                        hide beans
                        narrate "You retrieve the dusty old boots from the drum and put them on."
                        
                        show stacey disgusted
                        stacey "BEANS."
                        stacey "What. Is. Wrong. With. You."

                        think "These are like... five sizes too big."
                        think "I don't really know why I did that."
                        call scene_forestShed.util_equipItem("Boots")
                    "Put the boots in your backpack":
                        think "They don't look like my size."
                        think "Hey, might come in handy later though."

                        narrate "You retrieve the boots and add them to your backpack, which is now awkwardly bulky and pretty heavy."
                        stacey "Um. Okay then..."
     
                        call scene_forestShed.util_addItemToBag("Boots")

                    "Leave the boots in the oil drum":
                        show beans meanbean
                        beans "Yeah, I'm not touching those."
                        hide beans

                        stacey "Good, because they're {i}so{/i} not your colour."
                        think "Oh Stacey... how stereotypical can she get?"

                        stacey "You know I'm joking, right?"
                        stacey "What use could we possibly have for decaying footwear that's clearly five sizes too big for either of us."
                        return
                jump forestShed_searchingArea
    
    label .areaSearch_noLantern:
        menu:
            "Search the shed for another lantern" if not beansSearchedShed:
                jump .searchShed_noLantern
            "Attempt to search the outside of the shed" if not foundLockers:
                jump forestShed_searchingArea.searchAroundShed
            "Continue into the forest":
                jump .continueIntoForest
        
        # Search shed without lantern
        label .searchShed_noLantern:
            call scene_forestShed.util_updateKillerDistance(-1)
            if smashedLantern:
                stacey "Maybe there's another like, backup lantern."
                stacey "You know. Because you freakazoided out and the last one broke."
            
            think "It's getting pretty dark to search, but what choice do we have?"

            think "Ugh. I bet there's all kinds of horrible things in here."
            think "Those old drills ands saws hanging on the wall..."
            think "It's kind of creepy."
            think "Reminds me of a butcher's shop."

            stacey "Okay, you search the shelves. I'm gonna look through these drawers."
            show beans earnest
            beans "Okay!"
            hide beans

            narrate "You start rifling through the shelves above the workbench."
            narrate "You squint through your glasses to make out the objects in front of you."
            narrate "As you reach across the bench to the next shelf, your arm encounters resistance-"

            narrate "RRRRRRRRIP"

            show stacey surprised
            stacey "Beans! What was that?"

            show beans shout
            beans "Um, it was just my sleeve-"
            hide beans

            show stacey shocked
            stacey "Your hand! "

            narrate "You realise there's a dull ache in your hand."
            think "Is that... blood? "
            stacey "You must have caught it on that bandsaw. You need to be more careful!"
            stacey "How bad is it?"
            show beans stressed
            beans "I dunno... there's a bit of blood..."
            hide beans

            stacey "Ugh, that needs cleaning {i}stat{/i}."
            stacey "I've gotta bandage it until we find actual first aid."

            narrate "She pulls a spare neon pink scrunchie out of her pocket and attempts to bind your hand with it."
            narrate "It immediately soaks through with a dark bloodstain."
            narrate "At least you're no longer dripping on the floor."

            think "So much for not leaving a trail..." # warns the player that the blood trail could have consequences
            $ cutHand = True
            
            # Respond to Stacey's help
            menu:
                "Thank Stacey for her help":
                    $ stacey.approval += 1
                    show stacey blush
                    stacey "Yeah, well, don't mention it. "    
                    "TODO: Jump where?"
                "Kiss Stacey":
                    $ stacey.approval -= 5
                    stacey "BEANS! EW!"
                    show stacey angry
                    show beans blush
                    beans "{i}Oof{/i}"
                    hide beans
                    narrate "Stacey shoves you away, disgusted."
                    stacey "Why would you think that's okay?"
                    stacey "Ew. Not even. Don't even try it."

                    stacey "Let's just forget this ever happened, okay?"
                    call scene_forestShed.util_updateKillerDistance(-1)
                    "TODO: Jump where?"
                "Say nothing":
                    $ stacey.approval -= 1
                    show stacey uncomfortable
                    show beans blush2
                    beans "..."
                    hide beans
                    stacey "..."
                    think "Well, that was awkward."
                    "TODO: Jump where?"
            
            show stacey sigh
            stacey "So much for finding another flashlight."


    # Search around the shed
    label .searchAroundShed:
        $ foundLockers = True
        narrate "Around the side of the shed are two tall storage lockers."

        stacey "You could fit a whole body in one of those."
        stacey "What?"
        stacey "Don't tell me you weren't thinking it too."
        call scene_forestShed.util_updateKillerDistance(-1)
        jump forestShed_searchingArea

    label .continueIntoForest:
        show beans serious
        beans "We should get out of here."
        beans "You know, before that weirdo catches up to us."
        hide beans

        # You head into the forest
        jump forestShed_runIntoWoods

        # You still have to avoid the bear trap

        # If you do - you run deeper into the forest and end up hiding behind a tree while having your romantic talk with Stacey

