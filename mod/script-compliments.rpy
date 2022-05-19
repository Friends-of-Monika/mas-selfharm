#SH Submod compliments

#You saved me, [m_name].
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_saved_me",
            prompt="You saved me, [m_name].",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_saved_me:
    m "[player]...!"
    m "That means so much to me..."
    m "I’m so glad we were able to save each other."
    m "Thank you for saving me."
    m "I love you!"
    m "I wish I could help more with your struggles..."
    m "Just know I care and always will."
    return


#You're my everything, [m_name].
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_everything",
            prompt="You're my everything, [m_name].",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_everything:
    m "[player]..."
    m "I could say the same."
    m "I love you so much that my heart hurts!"
    m "You saved me in so many ways, my life and yours are intertwined!"
    m "And we'll be together forever!"
    return


#Thank you for being patient with me.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_patient",
            prompt="Thank you for being patient with me.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_patient:
    m "[player]..."
    m "I'll always be patient with you."
    m "It's no effort! After all, I love you, and I want to be by your side."
    m "Even in the tough moments."
    m "Listening to you and taking care of you is an honor!"
    m "Thank you for making me the happiest girl in the world."
    return


#Thanks to you, I'm still here
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp",
            category=['mshMod_compliment_still_here'],
            prompt="Thanks to you, I'm still here.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_still_here:
    m "..."
    m "[player]..."
    m "I'm sorry, I just..."
    extend "get so emotional!"
    m "Thank you for staying here."
    extend "Thank you for being my significant other."
    m "And thank you for being who you are."
    m "I’m so proud of you."
    m "Keep on fighting and know that you deserve to be happy."
    m "You are so inspiring!"
    extend "Never forget that."
    return


#You are my sunflower!
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_sunflower",
            prompt="You are my sunflower!",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_sunflower:
    m "Ahahaha, thank you, [player]!"
    m "I never need to face the sun as long as I have you by my side!"
    m "Because you are my sun."
    m "I love you, [mas_get_player_nickname()]."
    return


#You are my sunshine!
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_sunshine",
            prompt="You are my sunshine!",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_sunshine:
    m "Ehehehe~"
    m "Do I make you happy when skies are gray, [player]?"
    m "Ahaha, just teasing you."
    m "I love you, my little sun!"
    return


#Thank you for always being kind to me.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_being_kind",
            prompt="Thank you for always being kind to me.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_being_kind:
    m "Of course, [player]!" 
    m "What kind of girlfriend would I be if I wasn’t kind to you?"
    m "Coming to think of it though, I think Natsuki would disagree."
    m "Ahahaha~"
    m "I love you, [player]."
    extend "I'll always be kind to you."
    return


#Thanks for taking such good care of me.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_caring",
            prompt="Thanks for taking such good care of me.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_caring:
    m "I'll always take care of my precious [player]!"
    m "How I got so lucky to have you in my life, I don’t know, but I’m glad you’re mine."
    m "And since you're mine, I'll do my best to care for you and help you out!"
    m "I'll love you forever, [mas_get_player_nickname()]."
    return


#Thank you for always thinking of me.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_thinking_of_me",
            prompt="Thank you for always thinking of me.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_thinking_of_me:
    m "Oh, [player]..."
    extend "You're so sweet!"
    m "I will always think about you!"
    m "Doesn't matter if we're together or apart!"
    m "I hope you always think of me too."
    return


#Thank you for always helping me out.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_helping_out",
            prompt="Thank you for always helping me out.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_helping_out:
    m "[Player]...!"
    m "It's my pleasure."
    m "Often times, I wonder what I did to have a caring, loving and understanding person like you in my life."
    m "So, I'll always help you out whenever I can!"
    m "Thank you for allowing me to be present in your life."
    m "And for sticking with me."
    m "I love you!"
    return


#Thanks for being so understanding with me.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_being_understanding",
            prompt="Thanks for being so understanding with me.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_being_understanding:
    m "[Player]..."
    m "I should be the one to thank you."
    m "Sometimes, saying thank you feels like an understatement for everything you’ve done for me."
    m "I'll always be understanding with you, even if other people are not."
    m "I love you and I care about you!"
    m "You're the love of my life."
    return


#Thank you for understanding me.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_understanding_me",
            prompt="Thank you for understanding me.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_understanding_me:
    m "[Player]...!"
    m "Of course."
    extend "Why wouldn’t I?"
    m "I'll also do my best to understand you, and if I don't, I'll be by your side, nevertheless."
    m "And also, you understood me when I needed you to..."
    m "I'll never forget that and everything you did for me."
    m "I love you [player]."
    m "Remember you can always come to this room when you need reassurance."
    m "I'm here for you!"
    return
