label forestShed_runIntoWoods:
    if "Lantern" in beans.equipped:
        narrate "You and Stacey venture further into the woods."
        narrate "The lantern lights your path - without it, the forest would be pitch black."

        show stacey surprised
        stacey "Beans! Watch out!"
        
        narrate "Concealed under some leaves, you spy a vicious-looking set of metal teeth."

        show beans shout
        beans "A bear trap?!"
        hide beans

        show screen timed_choice(2.0, ".beansBearTrap")
        menu:
            "{i}Step on the trap{/i}":
                hide screen timed_choice
                jump .beansBearTrap
            "{i}Run around the trap{/i}":
                hide screen timed_choice
                jump .dodgedBearTrap
            "{i}Trip on the trap{/i}":
                hide screen timed_choice
                jump .beansBearTrap
            "{i}Put your foot on the trap{/i}":
                hide screen timed_choice
                jump .beansBearTrap
        
    else:
        if beans.proactivePassive < 0:
            narrate "Stacey goes first and steps on the bear trap, which you can't see, on account of not having a lantern."
            jump .staceyBearTrap
        else:
            narrate "You go first and step on a bear trap, which you can't see on account of not having a lantern."
            jump .beansBearTrap

    label .staceyBearTrap:
        narrate "TODO: Stacey steps on a bear trap and falls over, shrieking"
        menu:
            "{i}Try and free her{/i}":
                narrate "TODO: It's useless, the jaws are stuck tight and you're weak and pathetic."
                menu:
                    "{i}Keep trying to free her{/i}":
                        narrate "You both die"
                        narrate "RIP"
                        jump endings_forestShed.ending_staceyStuckInBearTrap
                    "{i}Give up and save yourself{/i}":
                        jump .runningFromBearTrap
            "{i}Leave her and run{/i}":
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

    label .beansBearTrap:
        narrate "The trap snaps shut on your leg."
        if "Boots" in beans.equipped:
            narrate "You close your eyes, expecting searing pain-"
            narrate "But it's... not as bad as you expected?"

            show stacey determined
            stacey "No way!"

            show stacey laugh
            stacey "Those stupid boots actually came in handy!"

            think "The boots!"
            narrate "The metal jaws of the trap are sunk into the thick leather of the old boots you're wearing."
            narrate "They've still lodged themselves firmly in your leg, and it's not comfortable"
            narrate "But you'd hate to think what it would look like if you didn't havethe boots to protect you."
            
            show stacey determined
            stacey "Hold still. My dad's a hunter, he told me how to disarm these things."
            stacey "You've just got to compress the springs like this... and then..."
            show stacey happy
            stacey "Voila!"
            hide stacey
            narrate "Somehow, Stacey jimmies the trap open and frees you."

            show stacey determined
            stacey "Now let's get out of here!"
            hide stacey
            jump endings_forestShed.ending_savedFromBearTrap
        else:
            narrate "Your socks and loafers offer no resistance at all."

            show beans shout
            beans "Aagh!"
            hide beans 

            narrate "The metal jaws chew through your flesh with a violent, searing pain."

            show stacey shout
            stacey "BEANS!"

            show stacey upsetshadow
            stacey "Ohmygod. Oh my god."

            show stacey worried
            stacey "Okay, um. There's a trick to disarming these- you gotta, um..."

            think "Oh boy, that's a lot of blood."

            show beans stressed
            beans "Stacey... "

            menu:
                "Get me out of here!":
                    show beans blush2 #beans be woozy
                    beans "Get... ge.. get me..."
                    think "I don't feel so good..."
                    hide beans

                    narrate "As the blood leaves your body, a heavy fog settles in your brain."
                    narrate "The words stumble and slur on your tongue"
                    narrate "You're fading."
                "For god's sake Stacey, get me out of here!":
                    show beans blush2 #beans be woozy
                    beans "For god's... god.. Stace..."
                    think "I don't feel so good..."
                    hide beans

                    narrate "As the blood leaves your body, a heavy fog settles in your brain."
                    narrate "The words stumble and slur on your tongue"
                    narrate "You're fading."                  
                "AAAAAAAAAAAAAAAAA":
                    think "That screaming..."
                    think "It's ear splitting."
                    think "Is that... me?"
                    narrate "As the blood leaves your body, a heavy fog settles in your brain."
                    narrate "The sound of your own scream seems far away."
                    narrate "You're fading."

            show stacey upsetshadow
            stacey "No no no...."
            stacey "Come on Beans.. I can do this..."
            narrate "You're faintly aware of Stacey struggling to prise the jaws of the trap open."
            
            show stacey upset
            stacey "Just gotta... compress the springs..."

            if killerDistance <= 0:
                # stacey has to leave you and run
                narrate "All the while, the heavy footsteps of your pursuer get closer."

                show stacey upsetshadow
                stacey "Beans..."
                stacey "I can't do it..."

                menu:
                    "Run! Save yourself!":
                        show beans confess
                        beans "Run..."
                        hide beans
                        stacey "I'm so sorry Beans."
                        if stacey.approval > staceyKissApprovalThreshold:
                            narrate "She gives you a gentle kiss on the forehead."
                            show stacey upset
                            stacey "I'm so, so sorry."
                            hide stacey
                        else:
                            narrate "Her eyes flick between you and her only route of escape-"
                            narrate "through the forest."                      
                    "Don't leave me!":
                        show beans stressed
                        beans "Don't... leave..."
                        hide beans
                        show stacey upset
                        stacey "You're not going to make it, Beans."
                        stacey "I..."
                        stacey "I have to run."
                        hide stacey 

                        narrate "She gives you hand one last squeeze."
                # TODO IF TIME
                # If your approval is high enough maybe she saves you
                jump endings_forestShed.ending_beansStuckInBearTrap
                # the killer catches up to you
            else:
                # stacey tries to help you but it's no use
                show stacey upset 
                stacey "It's not WORKING!"
                narrate "She wipes the tears angrily from her eyes."
                stacey "This isn't fair."
                if staceyDateAgreed:
                    stacey "You were meant to take me to the UFO museum."
                    think "Our date..."
                elif stacey.approval <= 0:
                    stacey "I know we weren't friends but..."
                    stacey "I didn't want you to {i}die{/i}"
                elif stacey.approval < staceyKissApprovalThreshold:
                    stacey "I didn't want to let anyone else die."
                    show stacey upsetshadow
                    stacey "Why does everyone keep dying?"
                else:
                    stacey "I never got to tell you that..."
                    show stacey upset2
                    stacey "I like you beans"
                    stacey "And now it's too late."

                    think "Score!"
                    show beans confess
                    beans "..."
                    narrate "Stacey gives you a gentle peck on the forehead."

                menu:
                    "I'm cold.":
                        beans "Cold..."
                        narrate "Stacey takes her jacket off and gently drapes it over you."
                        narrate "She's shivering slightly."
                        narrate "It's not clear whether from the cold, or her quiet sobbing."
                        
                    "I'm tired.":
                        beans "Tired..."
                        stacey "I know, Beans."
                        stacey "Just rest now."
                    "{i}Die{/i}":
                        narrate "You close your eyes."
                jump endings_forestShed.ending_beansStuckInBearTrap_noKiller

         

    label .dodgedBearTrap:
        # If being chased by killer - you get away
        if killerDistance <= 0:
            if "Boots" in beans.equipped:
                debug "TODO: You stumble on your stupid badly fitting boots"
                debug "Stacey pulls you up"
            
            if staceyDateAgreed:
                jump endings_forestShed.ending_lockerEscape_romance
            else:
                jump endings_forestShed.ending_lockerEscape_noRomance
        else:
            jump forestShed_treeTalk
            # Otherwise - tree talk
