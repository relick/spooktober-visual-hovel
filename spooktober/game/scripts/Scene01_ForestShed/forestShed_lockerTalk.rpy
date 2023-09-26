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
            narrate "You whisper as quietly as you can, hoping not to attrack the killer's attention."
            jump .lockerTalk_nextSteps

    label .util_updateStaceyApproval(delta = 0):
        # Update stacey approval
        $ stacey.approval += delta
        return
        # If below a certain threshold she bolts
        # PLIP: Changed my mind I don't like this
       
        # if stacey.approval < staceyLockerRunApprovalThreshold:
        #     jump .lockerTalk_staceyBolts_lowApproval
        # else:
        #     return
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
                narrate "Stacey laughs quietly"
                show stacey happy
                stacey "Yeah we've done alright at this, I guess."
                jump .lockerTalk_maybeWeCouldHang
    
    """
    label .lockerTalk_staceyBolts_lowApproval:
        narrate "Stacey runs and dies RIP"
    """

    label .lockerTalk_maybeWeCouldHang:
        show beans blush
        beans "Maybe when we get out of here we could... hang out sometime?"
        hide beans
        stacey "Oh yeah? And do what?"

        menu: 
            # TODO: Beans should have an idea of a date
            # Options should be more obvious in their difference

            "We could go to the movies!":
                jump .lockerTalk_iLikeMovies
            "We could go to a museum!":
                call .util_updateStaceyApproval(1)
                jump .lockerTalk_iLikeMuseums
            "I dunno, what's your idea of a good time?":
                jump .lockerTalk_iLikeMuseums
            "I'm gonna take you on the date of your dreams, baby.":
                if stacey.approval >= staceyRomanceApprovalThreshold:
                    show stacey blush
                    jump .lockerTalk_iLikeMuseums
                else:
                    narrate "Stacey laughs nervously"
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
                        "Doesn't that just make it more exciting?":
                            show stacey angry
                            stacey "No it just makes it more messed up!"
            "Just kidding. I'd rather lick a dead raccoon than spend more time with you.":
                call .util_updateStaceyApproval(-1)
                jump .lockerTalk_stuckHereWithYou 

    label .lockerTalk_iLikeMovies:
        show stacey sad
        stacey "Well... I guess that sounds fun."

        show beans stressed
        think "She doesn't sound that excited."
        show beans serious
        think "Maybe a movie wasn't the right suggestion..."

        beans "Is there something else you'd rather do?"
        jump .lockerTalk_iLikeMuseums

    label .lockerTalk_iLikeMuseums:
        show stacey blush
        stacey "Okay, you're going to think this is really dumb..."
        stacey "But you know those like, weird places that spring up by the road?"
        stacey "\"World's largest ball of String\", \"Museum of slightly small hats\" and whatever"
        
        show stacey excited
        stacey "I love those!"
        
        think "Wow, she actually seems really excited!"

        show stacey happy
        stacey "You know, there's a UFO museum that's opened just outside of town"
        stacey "I've been really wanting to go there - what do you say?"

        menu:
            "Let's do it!":
                stacey "Sounds great!"
                show stacey excited
                stacey "Finally, someone who's willing to come to weird museums with me!"
                stacey "Svenjamin wouldn't be caught dead in a museum."
            "It's a date!":
                stacey "A date, huh?"
                stacey "Well, it's got to be better than the ones Svenjamin took me on..."
            "You're right, that is dumb.":
                call .util_updateStaceyApproval(-1)
                show stacey angry
                stacey "Ugh... you sound just like Svenjamin."

        jump .lockerTalk_svenjamin
     
    label .lockerTalk_svenjamin:
        show beans serious
        think "Oh yeah, Svenjamin..."
        show beans meanbean
        think "He's the football team quarterback but also a TOTAL ass"
        show beans serious
        think "So are they dating, or...?" 

        stacey "{i}Sigh{/i}"
        stacey "I'm so glad we're not dating anymore..."       
        show stacey angry
        stacey "What an ass!"

        menu:
            "Why did you even go out with him?":
                stacey "I dunno... he's like, the quarterback, you know?"
                stacey "And I'm the head cheerleader"
                stacey "It just seemed right"

                show stacey sad
                stacey "I mean... {i}I{/i} thought we were dating..."

                show stacey angry
                stacey "Apparently he didn't think we were {i}exclusive{/i} or whatever."

                jump .lockerTalk_staceyCanDoBetter
            "He sounds like a terrible boyfriend":
                stacey "Ugh, he was."

                show stacey neutral
                stacey "He wasn't even really my boyfriend. We just kinda... dated a bit."
                stacey "You know. Went to the movies and whatever."

                show stacey sad
                stacey "I liked having someone to do all that stuff with, though."
                jump .lockerTalk_staceyCanDoBetter
            "I don't care about your lame issues, Stacey.":
                call .util_updateStaceyApproval(-1)
                jump .lockerTalk_stuckHereWithYou

    label .lockerTalk_staceyCanDoBetter:
        menu:
            "You can do way better, Stacey":
                show stacey happy
                stacey "You really think so?"
            "Give up on romance. You're basically unlovable.":
                call .util_updateStaceyApproval(-1)
                jump .lockerTalk_stuckHereWithYou


        menu:
            set relationshipAdvice_menuset
            "I can think of someone better who's right in front of you":
                jump .staceyCanDoBetter_rightInFrontOfYou
            "How about Kevin?":
                show stacey doubt
                stacey "Kevin?"
                stacey "He is extremely cool but... I dunno..."
                stacey "{i}Sigh{/i}"
                stacey "I'll think about it. Thanks though, Beans."
                stacey "For listening to me."
                jump .lockerTalk_hereComesKiller
            "Nah. Svenjamin's probably the best you'll ever get.":
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
                narrate "Stacey laughs."
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
            show stacey determined
            stacey "When we get out of here, I swear I'm never going on a date with Svenjamin again!"
            show stacey blush
            stacey "And maybe you can take me to that UFO museum."
            $ staceyDateAgreed = True
            jump .lockerTalk_hereComesKiller

    label .lockerTalk_stuckHereWithYou:
        show stacey angry
        stacey "Where do you get off on being such an {i}ass{/i}, Beans?"
        think "I'm starting to think Stacey doesn't like me"
        jump .lockerTalk_hereComesKiller

    label .lockerTalk_hereComesKiller:
        show stacey scared
        stacey "Ssh!" with vpunch
        stacey "He's coming this way"

        beans "Eeep!"

        # AUDIO: Killer footsteps audio
        think "I can hear his gross huge boots stomping across the clearing"
        think "My heart is beating out of my chest"
        
        # AUDIO: Killer footsteps fade out

        stacey "He's gone into the shed... "
        stacey "But he's still close"

        think "Should we risk making a break for it?"

        menu: 
            "Go now!":
                jump .lockerTalk_goEarly
            "Wait a little longer":
                jump .lockerTalk_waitForTime

    label .lockerTalk_goEarly:
        show stacey surprised
        stacey "Beans what-"
        show beans earnest
        beans "Now! Let's go!"
        hide beans

        if beans.proactivePassive > 0:
            narrate "You throw the locker open and run"
            narrate "Stacey following right behind you"
        else:
            narrate "Stacey throws the locker open and runs"
            narrate "You follow right behind"

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







