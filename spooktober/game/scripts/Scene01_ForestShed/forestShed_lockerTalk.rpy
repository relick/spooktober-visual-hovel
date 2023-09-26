label forestShed_lockerTalk:
    define staceyLockerRunApprovalThreshold = -4
    define staceyRomanceApprovalThreshold = 3

    default relationshipAdvice_menuset = set()

    narrate "You're both crammed into one tiny locker, pressed right up against each other."
    narrate "It's the perfect time to chat her up, but also not get murdered by being too loud."

    menu: 
        "{i}Say nothing{/i}":
            call scene_forestShed.util_updateProactivePassive(-1)
            jump .lockerTalk_nextSteps
        "{i}Press up closer against her{/i}":
            stacey "Um..."
        "What do we do now?":
            narrate "{i}You whisper as quietly as you can, hoping not to attrack the killer's attention.{/i}"
            jump .lockerTalk_nextSteps

    label .util_updateStaceyApproval(delta = 0):
        # Update stacey approval
        $ stacey.approval += delta
        # If below a certain threshold she bolts
        if stacey.approval < staceyLockerRunApprovalThreshold:
            jump .lockerTalk_staceyBolts_lowApproval
        else:
            return
        # If above a certain threshold she confesses? maybe


    label .lockerTalk_pressCloser:

    label .lockerTalk_nextSteps:
        stacey "Okay, here's the plan."
        stacey "We wait until we're sure the coast is clear - and then we run."
        show stacey determined
        stacey "We have to make ABSOLUTELY SURE he's not right behind us"
        show stacey apologetic
        stacey "Because no offense, Beans, but I don't think you could outrun a dead badger."

        menu:
            "Got it. I'll follow your lead.":
                call scene_forestShed.util_updateProactivePassive(-1)
            "Got it. You can follow my lead.":
                call scene_forestShed.util_updateProactivePassive(1)
        
        stacey "..."
        show stacey neutral
        stacey "You know..."
        stacey "You're not as bad at this as I thought you'd be"

        menu:
            "Well you're great at this, Stacey!":
                call .util_updateStaceyApproval(1)
                show stacey blush
                think "I know storage lockers aren't very romantic but..."
                think "Maybe this could be my chance to impress her...?"
                jump .lockerTalk_maybeWeCouldHang
            "Well {i}one{/i} of us has to be competent if we're going to live.":
                call .util_updateStaceyApproval(-1)
            "It's teamwork that makes the dream work!":
                call .util_updateStaceyApproval(1)
                narrate "{i}Stacey laughs quietly{/i}"
                show stacey happy
                stacey "Yeah we've done alright at this, I guess."
                jump .lockerTalk_maybeWeCouldHang
    
    label .lockerTalk_staceyBolts_lowApproval:
        narrate "Stacey runs and dies RIP"

    label .lockerTalk_maybeWeCouldHang:
        show beans blush
        beans "Maybe when we get out of here we could... do other stuff together sometime?"
        hide beans
        stacey "Oh yeah? Like what?"

        menu: 
            # TODO: Beans should have an idea of a date
            # Options should be more obvious in their difference
            "I dunno, what's your idea of a good time?":
                jump .lockerTalk_iLikeMovies
            "I dunno, what's your idea of a dream date?":
                if stacey.approval >= staceyRomanceApprovalThreshold:
                    show stacey blush
                    jump .lockerTalk_iLikeMovies
                else:
                    narrate "{i}Stacey laughs nervously{/i}"
                    stacey "Um... a date?"
                    stacey "I have a boyfriend Beans..."
                    menu:
                        "Oh...":
                            think "This is so awkward..."
                            think "Even though it's dark I can tell she'd avoiding looking at me"
                            jump .lockerTalk_hereComesKiller
                        "{i}(lie){/i} Haha... me too... haha...":
                            think "This is so awkward..."
                            think "Even though it's dark I can tell she'd avoiding looking at me"
                            jump .lockerTalk_hereComesKiller
                        "I'm just kidding Stacey, god. Don't be so conceited.":
                            call .util_updateStaceyApproval(-1)
                            jump .lockerTalk_stuckHereWithYou
                        # TODO: Add an option where you don't care about the boyfriend
            "Just kidding. I'd rather lick a dead raccoon than spend more time with you.":
                call .util_updateStaceyApproval(-1)
                jump .lockerTalk_stuckHereWithYou 

    label .lockerTalk_iLikeMovies:
        stacey "Well... I like movies"
        show stacey excited
        stacey "And I really want to see {i}The Brunch Gang!{/i}"
        menu:
            "Let's do it!":
                stacey "Sounds great!"
                stacey "I wish my boyfriend was that excited to take me to the movies..."
            "It's a date!":
                stacey "A date, huh?"
                stacey "Well, it's got to be better than a date with my loser boyfriend..."
            "Ugh, that movie looks awful. No thanks.":
                call .util_updateStaceyApproval(-1)
                show stacey angry
                stacey "You sound just like my crappy boyfriend."
        jump .lockerTalk_staceysLoserBoyfriend

    label .lockerTalk_staceysLoserBoyfriend:
        stacey "He never wants to do anything I like"
        menu:
            "Why are you going out with him then?":
                stacey "I dunno... he's like, the quarterback, you know?"
                stacey "And I'm the head cheerleader"
                stacey "It's just the way things are, you know."
                jump .lockerTalk_relationshipAdvice
            "He sounds like a terrible boyfriend":
                stacey "Yeah... I know"
                show stacey sad
                stacey "But what if I can't find anyone better?"
                jump .lockerTalk_staceyCanDoBetter
            "Probably because everything {i}you{/i} enjoy sucks":
                call .util_updateStaceyApproval(-1)
                jump .lockerTalk_stuckHereWithYou

    label .lockerTalk_relationshipAdvice:
        menu:
            "You should dump him":
                stacey "And then what? Go to prom by myself? Like a loser?"
                jump .lockerTalk_staceyCanDoBetter
            "You can do better, Stacey":
                stacey "Oh yeah? Like who?"
                jump .lockerTalk_staceyCanDoBetter
            "Actually I don't care about your lame issues.":
                call .util_updateStaceyApproval(-1)
                jump .lockerTalk_stuckHereWithYou

    label .lockerTalk_staceyCanDoBetter:
        menu:
            set relationshipAdvice_menuset
            "You're better off single than with someone that makes you unhappy":
                stacey "You really think so?"
                jump .lockerTalk_staceyCanDoBetter
            "I can think of someone better who's right in front of you":
                jump .staceyCanDoBetter_rightInFrontOfYou
            "I dunno, maybe Kevin?":
                show stacey doubt
                stacey "Kevin?"
                stacey "He is extremely cool but... I dunno..."
                stacey "{i}Sigh{/i}"
                stacey "I'll think about it. Thanks though, Beans."
                stacey "For listening to me."
                jump .lockerTalk_hereComesKiller
            "You're right. He's probably the best you'll ever get.":
                show stacey sad
                stacey "That's what I'm worried about"
                stacey "What if this is like... the peak?"
                stacey "High school, I mean."
                stacey "What if this is the best it gets?"
                stacey "And I've only got one year left of it."

                menu:
                    "You've got your whole life ahead of you, Stacey!":
                        stacey "{i}Sigh{/i}"
                        stacey "I know you're right..."
                        stacey "I just... what if you're not? What if this is-"

                    "You can't think like that Stacey":
                        stacey "{i}Sigh{/i}"
                        stacey "Sorry"
                        stacey "I'll pull myself together"
                    "Jesus Christ Stacey, way to bring the mood down.":
                        stacey "Sorry"
                        stacey "I'll pull myself together"

                jump .lockerTalk_hereComesKiller

        label .staceyCanDoBetter_rightInFrontOfYou:
            show stacey surprised
            stacey "You?"
            if stacey.approval < staceyRomanceApprovalThreshold:
                narrate "{i}Stacey laughs.{/i}"
                stacey "You're such a goof, Beans"
                stacey "Svenjamin isn't {i}that{/i} bad"
                stacey "Thanks for trying to cheer me up though"
                think "Oof..."
                think "Maybe if she liked me more that would have worked."
                jump .lockerTalk_hereComesKiller
            else:
                show stacey blush
                stacey "What are you trying to say, Beans?"
                menu:
                    "I like you, Stacey":
                        jump .staceyCanDoBetter_iLikeYou
                    "Nevermind, it was stupid. Forget it.":
                        show stacey sad
                        stacey "...oh."
                        jump .lockerTalk_hereComesKiller
                    "Nothing, Stacey. You're embarassing yourself.":
                        call .util_updateStaceyApproval(-1)
                        jump .lockerTalk_stuckHereWithYou             

        label .staceyCanDoBetter_iLikeYou:
            stacey "Beans..."
            show stacey laugh
            stacey "I thought so! You're so obvious."
            menu:
                "Do you... like me too?":
                    show stacey blush
                    stacey "You're cute, Beans"
                "Sorry, I just made this weird.":
                    stacey "You don't have to be so awkward, Beans."
                    stacey "{i}Sigh{/i}"
            
            jump .staceyCanDoBetter_takeMeout

        label .staceyCanDoBetter_takeMeout:
            stacey "When we get out of here, I'm going to dump Svenjamin"
            show stacey blush
            stacey "And maybe you can take me out for a movie date"
            $ staceyDateAgreed = True
            jump .lockerTalk_hereComesKiller

    label .lockerTalk_stuckHereWithYou:
        show stacey angry
        stacey "Ugh. Just my luck to get stuck here with someone like {i}you.{/i}"
        think "I'm starting to think Stacey doesn't like me"
        jump .lockerTalk_hereComesKiller

    label .lockerTalk_hereComesKiller:
        show stacey scared
        stacey "Ssh!" with vpunch
        stacey "He's coming this way"

        # AUDIO: Killer footsteps audio

        think "My heart is beating out of my chest"
        
        # AUDIO: Killer footsteps fade out
        think "He's disappeared into the shed..."
        think "Should we risk making a break for it?"

        menu: 
            "Go now!":
                jump .lockerTalk_goEarly
            "Wait a little longer":
                jump lockerTalk_waitForTime

    label .lockerTalk_goEarly:
        show stacey surprised
        stacey "Beans what-"
        show beans earnest
        beans "Now! Let's go!"
        hide beans

        if beans.proactivePassive > 0:
            narrate "{i}You throw the locker open and run{/i}"
            narrate "{i}Stacey following right behind you{/i}"
        else:
            narrate "{i}Stacey throws the locker open and runs{/i}"
            narrate "{i}You follow right behind{/i}"

        stacey "Beans! He's right behind us!"
        jump scene_forestShed.runIntoTheWoods

    label .lockerTalk_waitForTime:
        narrate "TODO: You wait and somewhere in the distance hear the snap of a bear trap's jaws and a scream"
        narrate "The killer stomps off in that direction"
        narrate "You and stacey slip out undetected - to freedom!"
        if staceyDateAgreed:
            jump endings_forestShed.ending_lockerEscape_romance
        else:
            jump endings_forestShed.ending_lockerEscape_noRomance







