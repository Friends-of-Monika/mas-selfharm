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
    m 2dsbftpa "[player]...!"
    m 2hsbla "That means so much to me..."
    m 7ssbla "I’m so glad we were able to save each other."
    m 1dsbfb "Thank you for saving me."
    m 1hsbfb "I love you!"
    m 1lssdlc "I wish I could help more with your struggles..."
    m 5fkbfa "Just know I care and always will."
    return "love"


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
    m 2dsbftpa "[player]..."
    m 2fsbftpa "I could say the same."
    m 4hsbftpb "I love you so much that my heart hurts!"
    m 4ssbfb "You saved me in so many ways, my life and yours are intertwined!"
    m 5fkbfa "And we'll be together forever!"
    return "love"


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
    m 2dsbfa "[player]..."
    m 2fsbfa "I'll always be patient with you."
    m 7gsbfb "It's no effort! After all, I love you, and I want to be by your side."
    m 7lssdlc "Even in the tough moments."
    m 1hsb "Listening to you and taking care of you is an honor!"
    m 5fkbfa "Thank you for making me the happiest girl in the world."
    return


#Thanks to you, I'm still here.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_compliment_still_here",
            prompt="Thanks to you, I'm still here.",
            unlocked=True
        ),
        code="CMP"
    )

label mshMod_compliment_still_here:
    m 6dsbftpa "..."
    m 6fsbftsa "[player]..."
    m 2hsbftub "I'm sorry, I just... "
    extend 2fsbftpa "get so emotional!"
    m 2fsbftpb "Thank you for staying here. "
    extend 7fsbftpb "Thank you for being my significant other."
    m 4fsbftpb "And thank you for being who you are."
    m 2nsbfu "I’m so proud of you."
    m 2dsbfu "Keep on fighting and know that you deserve to be happy."
    m 2ssblb "You are so inspiring! "
    extend 5fkbfa "Never forget that."
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
    m 1hsbfb "Ahahaha, thank you, [player]!"
    m 1gsbfb "I never need to face the sun as long as I have you by my side!"
    m 1ksbfb "Because you are my sun."
    m 5fkbfa "I love you, [mas_get_player_nickname()]."
    return "love"


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
    m 1hsbfb "Ehehehe~"
    m 7gsbfb "Do I make you happy when skies are gray, [player]?"
    m 2hsbfb "Ahaha, just teasing you."
    m 5fkbfa "I love you, my little sun!"
    return "love"


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
    m 7esbfb "Of course, [player]!"
    m 3rtc "What kind of girlfriend would I be if I wasn’t kind to you?"
    m 2rsbfsdlb "Coming to think of it though, I think Natsuki would disagree."
    m 2hsbfb "Ahahaha~"
    m 5fsbfa "I love you, [player]. "
    extend 5fkbfa "I'll always be kind to you."
    return "love"


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
    m 4fkbfa "I'll always take care of my precious [player]!"
    m 3msbfa "How I got so lucky to have you in my life, I don’t know, but I’m glad you’re mine."
    m 7esbfb "And since you're mine, I'll do my best to care for you and help you out!"
    m 5fkbfa "I'll love you forever, [mas_get_player_nickname()]."
    return "love"


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
    m 2fsbfa "Oh, [player]... "
    extend 7hsbfb "You're so sweet!"
    m 2nsbfb "I will always think about you!"
    m 7lsbfu "Doesn't matter if we're together or apart!"
    m 5fkbfa "I hope you always think of me too."
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
    m 2hsbfb "[Player]...!"
    m 7hsbfb "It's my pleasure."
    m 7lsbfu "Often times, I wonder what I did to have a caring, loving and understanding person like you in my life."
    m 2ssbfb "So, I'll always help you out whenever I can!"
    m 7wsbfb "Thank you for allowing me to be present in your life."
    m 5fubfa "And for sticking with me."
    m 5fkbfa "I love you!"
    return "love"


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
    m 5fubfa "[Player]..."
    m 4fubfa "I should be the one to thank you."
    m 3dubfa "Sometimes, saying thank you feels like an understatement for everything you’ve done for me."
    m "I'll always be understanding with you, "
    extend 1lssdlc "even if other people are not."
    m "I love you and I care about you!"
    m 5fkbfa "You're the love of my life."
    return "love"


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
    m 2dsbftpa "[Player]...!"
    m "Of course. "
    extend "Why wouldn’t I?"
    m "I'll also do my best to understand you, and if I don't, I'll be by your side, nevertheless."
    m 3dubfb "And also, you understood me when I needed you to..."
    m 3dubfa "I'll never forget that and everything you did for me."
    m "I love you [player]."
    m "Remember you can always come to this room when you need reassurance."
    m 5fkbfa "I'm here for you!"
    return "love"
