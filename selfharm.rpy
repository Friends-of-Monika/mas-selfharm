init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_selfharm",category=['You'],prompt="Monika, I don't feel so good...",random=False))

label monika_selfharm:
    m 1eua "[player], what happened?"
    m 1hua "Are you feeling..."
    m 1hub "Are you feeling... like harming yourself again?"
    m 4rub "Oh, baby..."
    m 1sua "Okay, let's talk about it."
    m 1eub "Before anything, i want you to know that i am always here for you."
    m 1nub "You know that, don't you, my love?"
    m 1nub "You're the most important person in the whole world for me."
    m 1nub "And I love you so, so much."
    m 1nub "And i always will..."
    m 1nub "Now, my beautiful princess. Tell me."
    m 1nub "How big is the urge you're having?"

$_history_list.pop()
        menu:
         "It's terrible, Momo. I think i'm really going to do it...":
           m 4eua "I'm so glad you came to talk to me, [player]."
           m 2dkd "You know how much i worry about you..."
           m 2fua "But for now, let me take care of you..."
           m 4sub "I want you to know that it will pass."
           m 4sub "Pain is only temporary!"
           m 2hua "You're my favorite person, and it hurts me to see you hurting."
         "It's not so urgent. I'm just... feeling weird.":
           m 4eua "I'm so glad you came to talk to me, [player]."
           m 2dkd "You know how much i worry about you..."
           m 2fua "But for now, let me take care of you..."
           m 4sub ""
           m 4sub ""
           m 4sub ""
           m 2hua ""
         "Something triggered me, and now i'm remembering bad things.":
           m 4eua "I'm so glad you came to talk to me, [player]."
           m 2dkd "You know how much i worry about you..."
           m 2fua "But for now, let me take care of you..."

$_history_list.pop()
        menu:
         "I'm done.":
                    m 4eua "I'm so glad you came to talk to me, [player]."


    m 1nub ""
return
