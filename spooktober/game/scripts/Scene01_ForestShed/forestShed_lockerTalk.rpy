default lockerTalkLocation = "Locker"

label forestShed_lockerTalk:
    $ crossfade("audio/music/Hallowbean_Drone.ogg")

    define staceyLockerRunApprovalThreshold = -4
    define staceyRomanceApprovalThreshold = 3

    default relationshipAdvice_menuset = set()

    narrate "You're pressed right up against each other."

    show beans kewl
    think "It's kinda... romantic actually."
    think "If it wasn't for the mortal danger."
    hide beans

    menu: 
        "{i}Say nothing{/i}":
            call scene_forestShed.util_updateProactivePassive(-1)
            jump .lockerTalk_nextSteps
        "{i}Press up closer against her{/i}":
            stacey "Um..."

            jump .lockerTalk_pressCloser
        "What do we do now?":
            narrate "You whisper as quietly as you can."
            show beans stressed
            beans "What do we do now?"
            hide beans
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
        narrate "You press up close to Stacey"
        narrate "She gently pushes you away"
        jump .lockerTalk_nextSteps
    label .lockerTalk_nextSteps:
        stacey "Okay, here's the plan."
        stacey "We wait until we're sure the coast is clear - and then we run."
        show stacey determined
        stacey "We have to make ABSOLUTELY SURE he's not right behind us"
        show stacey sigh
        stacey "Because no offense, Beans, but I don't think you could outrun a dead badger."

        menu:
            "Got it. I'll follow your lead.":
                show beans earnest
                beans "Got it. I'll follow your lead."
                hide beans
                call scene_forestShed.util_updateProactivePassive(-1)
            "Got it. You can follow my lead.":
                show beans kewlpewpew
                beans "Got it. You can follow my lead."
                hide beans
                call scene_forestShed.util_updateProactivePassive(1)
        
        stacey "..."
        show stacey happy
        stacey "You know..."
        stacey "You're not as useless as I thought you'd be."

        menu:
            "You're {i}amazing{/i}, Stacey!":
                show beans earnest
                beans "You're {i}amazing{/i}, Stacey!"
                think "Maybe this could be my chance to impress her...?"
                hide beans
                call .util_updateStaceyApproval(1)
                show stacey blush2
                stacey "Aww, you're sweet, Beans."
                stacey "In another High School life we could've been friends, you know."                
                jump .lockerTalk_maybeWeCouldHang
            "Well {i}one{/i} of us has to be competent if we're going to live.":
                show beans meanbean
                beans "Well {i}one{/i} of us has to be competent if we're going to live."
                call .util_updateStaceyApproval(-1)

                show stacey annoyed
                stacey "Yeah okay, whatever."
                jump .lockerTalk_stuckHereWithYou
            "It's teamwork that makes the dream work!":
                show beans kewl
                "It's teamwork that makes the dream work!"
                show beans kewlpewpew
                call .util_updateStaceyApproval(1)
                show stacey laugh
                narrate "Stacey laughs quietly"
                hide beans
                show stacey happy
                stacey "Yeah, we're doing okay."
                stacey "We're alive and that's what counts, right?"

                show stacey sigh
                stacey "In another High School life we could've been friends, you know."
                jump .lockerTalk_maybeWeCouldHang

    label .lockerTalk_maybeWeCouldHang:
        $ crossfade("audio/music/SweetRedBeans.ogg")

        show beans blush
        beans "Maybe when we get out of here we could... hang out sometime?"
        hide beans

        show stacey happy
        stacey "Oh yeah? And do what?"

        menu: 
            "We could go to the movies!":
                show beans confess
                beans "We could go to the movies!"
                hide beans
                jump .lockerTalk_iLikeMovies
            "We could go to a museum!":
                show beans confess
                beans "We could go to a museum!"
                hide beans
                call .util_updateStaceyApproval(1)
                jump .lockerTalk_iLikeMuseums
            "I dunno, what's your idea of a good time?":
                show beans blush
                beans "I dunno, what's your idea of a good time?"
                hide beans
                jump .lockerTalk_iLikeMuseums
            "I'm gonna take you on the date of your dreams, baby.":
                show beans kewlpewpew
                beans "I'm gonna take you on the date of your dreams, baby."
                hide beans
                if stacey.approval >= staceyRomanceApprovalThreshold:
                    show stacey blush
                    jump .lockerTalk_iLikeMuseums
                else:
                    narrate "Stacey laughs nervously"
                    stacey "Um... a date?"
                    stacey "I have a boyfriend Beans..."
                    menu:
                        "Oh...":
                            show beans meanbean
                            beans "Oh..."                            
                            think "This is so awkward..."
                            think "Even though it's dark I can tell she'd avoiding looking at me"
                            hide beans 
                            jump .lockerTalk_hereComesKiller
                        "{i}(lie){/i} Haha... me too... haha...":
                            show beans kewl
                            "Haha... me too... haha..."                            
                            think "This is so awkward..."
                            think "Even though it's dark I can tell she'd avoiding looking at me"
                            hide beans
                            jump .lockerTalk_hereComesKiller
                        "I'm just kidding Stacey, god. Don't be so conceited.":
                            show beans meanbean
                            beans "I'm just kidding Stacey, god. Don't be so conceited."
                            hide beans
                            call .util_updateStaceyApproval(-1)
                            jump .lockerTalk_stuckHereWithYou
                        "Doesn't that just make it more exciting?":
                            show beans kewlpewpew
                            beans "Doesn't that just make it more exciting?"
                            hide beans
                            show stacey annoyed # note: was angry
                            stacey "No it just makes it more messed up!"
                            stacey "Just forget about it."
                            stacey "You're so weird."
                            call .util_updateStaceyApproval(-1)
                            jump .lockerTalk_stuckHereWithYou                          
            "Just kidding. I'd rather lick a dead raccoon than spend more time with you.":
                show beans meanbean
                beans "Just kidding. I'd rather lick a dead raccoon than spend more time with you."
                hide beans
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
        stacey "But you know those like, weird museum places that spring up by the road?"
        stacey "{color=#f6ba00}\"World's largest ball of String\"{/colour}, {color=#f6ba00}\"Museum of slightly small hats\" {/colour}and whatever"
        
        show stacey excited
        stacey "I love those!" with vpunch
        
        think "Wow, she actually seems really excited!"
        hide beans

        show stacey happy
        stacey "You know, there's a UFO museum that's opened just outside of town"
        stacey "I've been really wanting to go there - what do you say?"

        menu:
            "Let's do it!":
                show beans confess
                beans "Let's do it!"
                hide beans
                stacey "Sounds great!"
                show stacey excited
                stacey "Finally, someone who's willing to come to weird museums with me!"
                stacey "Svenjamin wouldn't be caught dead in a museum."
            "It's a date!":
                show beans confess
                beans "It's a date!"
                hide beans                
                stacey "A date, huh?"
                stacey "Well, it's got to be better than the ones Svenjamin took me on..."
            "You're right, that is dumb.":
                show beans serious
                beans "You're right, that is dumb."
                hide beans
                call .util_updateStaceyApproval(-1)
                show stacey annoyed # note: was angry
                stacey "Ugh... you sound just like Svenjamin."

        jump .lockerTalk_svenjamin
     
    label .lockerTalk_svenjamin:
        show beans serious
        think "Oh yeah, Svenjamin..."
        show beans meanbean
        think "He's the football team quarterback but also a TOTAL ass"
        show beans serious
        think "So are they dating, or...?" 

        show stacey sigh
        stacey "{i}Sigh{/i}"
        stacey "I'm so glad we're not dating anymore..."       
        show stacey annoyed # note: was angry
        stacey "What an ass!"

        menu:
            "Why did you even go out with him?":
                show beans serious
                beans "Why did you even go out with him?"
                hide beans

                show stacey sigh
                stacey "I dunno... he's like, the quarterback, you know?"
                stacey "And I'm the head cheerleader"
                stacey "It just seemed right"

                show stacey sad
                stacey "I mean... {i}I{/i} thought we were dating..."

                show stacey annoyed # note: was angry
                stacey "Apparently he didn't think we were {i}exclusive{/i} or whatever."

                jump .lockerTalk_staceyCanDoBetter
            "He sounds like a terrible boyfriend":
                show beans serious2
                beans "He sounds like a terrible boyfriend"
                hide beans
                stacey "Ugh, he was."

                show stacey sigh # note: was neutral
                stacey "He wasn't even really my boyfriend. We just kinda... dated a bit."
                stacey "You know. Went to the movies and whatever."

                show stacey sad
                stacey "I liked having someone to do all that stuff with, though."
                jump .lockerTalk_staceyCanDoBetter
            "I don't care about your lame issues, Stacey.":
                show beans meanbean
                beans "I don't care about your lame issues, Stacey."
                hide beans
                call .util_updateStaceyApproval(-1)
                jump .lockerTalk_stuckHereWithYou

    label .lockerTalk_staceyCanDoBetter:
        menu:
            "You can do way better, Stacey":
                show beans earnest
                beans "You can do way better, Stacey"
                hide beans
                call .util_updateStaceyApproval(1)
                show stacey happy
                stacey "You really think so?"

                show beans earnest
                beans "Yeah! You've got so many options!"
                beans "In fact..."
            "Give up on romance. You're basically unlovable.":
                show beans meanbean
                beans "Give up on romance. You're basically unlovable."
                hide beans
                call .util_updateStaceyApproval(-1)
                jump .lockerTalk_stuckHereWithYou


        menu:
            set relationshipAdvice_menuset
            "I can think of someone better who's right in front of you.":
                show beans blush2
                beans "I can think of someone better who's right in front of you."
                hide beans
                jump .staceyCanDoBetter_rightInFrontOfYou
            "How about Kevin?":
                show beans kewl
                beans  "How about Kevin?"
                hide beans

                show stacey sad2 # note: was doubt
                stacey "Kevin?"
                stacey "He is extremely cool but... I dunno..."
                stacey "{i}Sigh{/i}"
                stacey "I'll think about it. Thanks though, Beans."
                stacey "For listening to me."
                jump .lockerTalk_hereComesKiller
            "Actually nevermind. Svenjamin's probably the best you'll ever get.":
                show beans serious
                beans "Actually nevermind. Svenjamin's probably the best you'll ever get."
                hide beans
                show stacey sad
                stacey "That's what I'm worried about"
                stacey "What if this is like... the peak?"
                stacey "High school, I mean."
                stacey "What if this is the best it gets?"
                stacey "And I've only got one year left of it."

                menu: 
                    "You've got your whole life ahead of you, Stacey!":
                        show beans earnest
                        beans "You've got your whole life ahead of you, Stacey!"
                        hide beans
                        stacey "{i}Sigh{/i}"
                        stacey "I know you're right..."
                        stacey "I just... what if you're not? What if this is-"

                    "You can't think like that Stacey":
                        show beans earnest
                        beans "You can't think like that Stacey"
                        hide beans
                        stacey "{i}Sigh{/i}"
                        stacey "Sorry"
                        stacey "I'll pull myself together"
                    "Jesus Christ Stacey, way to bring the mood down.":
                        show beans meanbean
                        beans "Jesus Christ Stacey, way to bring the mood down."
                        hide beans
                        stacey "Sorry"
                        stacey "I'll pull myself together"

                jump .lockerTalk_hereComesKiller

        label .staceyCanDoBetter_rightInFrontOfYou:
            show stacey laugh # note: was surprised
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
                        show beans confess
                        beans "I like you, Stacey"
                        hide beans
                        jump .staceyCanDoBetter_iLikeYou
                    "Nevermind, it was stupid. Forget it.":
                        show beans blush
                        beans "Nevermind, it was stupid. Forget it."
                        hide beans

                        show stacey sad
                        stacey "...oh."
                        jump .lockerTalk_hereComesKiller
                    "Nothing, Stacey. You're embarassing yourself.":
                        show beans meanbean
                        beans "Nothing, Stacey. You're embarassing yourself."
                        hide beans
                        call .util_updateStaceyApproval(-1)
                        jump .lockerTalk_stuckHereWithYou             

        label .staceyCanDoBetter_iLikeYou:
            stacey "Beans..."
            show stacey laugh
            stacey "I thought so! You're so obvious."
            menu:
                "Do you... like me too?":
                    show beans blush 
                    beans "Do you... like me too?"
                    hide beans
                    show stacey blush
                    stacey "You're cute, Beans"
                "Sorry, I just made this weird.":
                    show beans blush
                    beans "Sorry, I just made this weird."
                    hide beans
                    stacey "You don't have to be so awkward, Beans."
                    stacey "{i}Sigh{/i}"
            
            jump .staceyCanDoBetter_takeMeout

        label .staceyCanDoBetter_takeMeout:
            show stacey determined
            stacey "When we get out of here, I swear I'm never going on a date with Svenjamin again!"
            show stacey blush
            stacey "And maybe you can take me to that UFO museum."
            show stacey blush2
            stacey "If you still want to..."
            $ staceyDateAgreed = True
            jump .lockerTalk_hereComesKiller

    label .lockerTalk_stuckHereWithYou:
        show stacey annoyed # note: was angry
        stacey "Where do you get off on being such an {i}ass{/i}, Beans?"
        think "I'm starting to think Stacey doesn't like me"
        jump .lockerTalk_hereComesKiller

    label .lockerTalk_hereComesKiller:
        $ crossfade("audio/music/Hallowbean_Heartbeat.ogg")

        show stacey scared
        stacey "Ssh!" with vpunch
        narrate "Stacey abruptly shushes you."
        stacey "He's coming this way!"

        beans "Eeep!"

        # AUDIO: Killer footsteps audio
        if lockerTalkLocation == "Tree":
            think "I can hear him stomping through the trees"
            think "Is he... sniffing? Like an animal?"
        else:
            think "I can hear his gross huge boots stomping across the clearing"
        think "My heart is beating out of my chest"
        
        # AUDIO: Killer footsteps fade out
        if lockerTalkLocation == "Locker":
            stacey "He's gone into the shed..."
        elif lockerTalkLocation == "UnderTable":
            stacey "He's gone round the back of the shed..."
        elif lockerTalkLocation == "Tree":
            stacey "He's heading back towards the clearing..."
        stacey "But he's still close"

        think "Should we risk making a break for it?"

        menu: 
            "Go now!":
                show beans shout
                beans "Go now!"
                hide beans
                jump .lockerTalk_goEarly
            "Wait a little longer":
                show beans serious
                beans "Wait a little longer."
                hide beans
                jump .lockerTalk_waitForTime

    label .lockerTalk_goEarly:
        show stacey determined # note: was surprised
        stacey "Beans what-"
        show beans earnest
        beans "Now! Let's go!"
        hide beans

        if beans.proactivePassive > 0:
            if lockerTalkLocation == "Locker":
                narrate "You throw the locker open and run"
            elif lockerTalkLocation == "UnderTable":
                narrate "You scramble out from under the workbench and run"
            elif lockerTalkLocation == "Tree":
                narrate "You don't even check the coast is clear - you just run"
            narrate "Stacey follows right behind you"
   
        else:
            if lockerTalkLocation == "Locker":
                narrate "Stacey throws the locker open and runs"
            elif lockerTalkLocation == "UnderTable":
                narrate "Stacey scrambles out from under the workbench and runs"
            elif lockerTalkLocation == "Tree":
                narrate "Stacey doesn't even check the coast is clear - she just runs"
                # TODO: How do we get here? We've probably already run.

            narrate "You follow right behind"

        stacey "Beans! He's right behind us!"

        if lockerTalkLocation == "Tree":
            # TODO: He catches you and you die
            jump endings_forestShed.ending_killerCaughtInWoods
        else:
            jump forestShed_runIntoWoods



    label .lockerTalk_waitForTime:
        narrate "You wait."
        narrate "You're starting to think the perfect time will never come."
        narrate "But then, in the distance-"

        narrate "{i}SNAP!{/i}"

        narrate "You hear a pained scream"

        show stacey worried
        stacey "Is that... Theodora??"
        hide stacey

        narrate "Whoever the unlucky person is - they've piqued your pursuer's interest"
        narrate "You hear the familiar heavy footsteps disappearing away from you"
        narrate "Pursuing their new prey."
        if staceyDateAgreed:
            jump endings_forestShed.ending_lockerEscape_romance
        else:
            jump endings_forestShed.ending_lockerEscape_noRomance







