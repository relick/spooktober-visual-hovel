label forestShed_treeTalk:
    show beans stressed
    think "That was a close one!"
    show beans tired
    think "I've had enough of this stupid wood."
    hide beans

    show stacey determined
    stacey "Come on Beans - we have to keep going."
    stacey "Maybe we'll find the road, or help, or..."
    show stacey sigh
    stacey "Or something"
    stacey "I just want this night to end."
    hide stacey

    narrate "Suddenly she stops, and holds her hand up."
    narrate "She's signalling you to be quiet."

    show stacey worried
    stacey "Do you hear that?"
    hide stacey

    think "I can hear rustling leaves, the hooting of an owl..."
    think "...and the heavy thud of approaching footsteps through the trees."

    show stacey worried
    stacey "He's following us!"
    narrate "She grabs you by the hand and pulls you behind a large tree."

    stacey "Not... another... word..."

    $ lockerTalkLocation = "Tree"
    jump forestShed_lockerTalk
    