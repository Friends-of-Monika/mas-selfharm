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
    m ""
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
    m ""
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
    m ""
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
    m ""
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
    m ""
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
    m ""
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
    m ""
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
    m ""
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
    m ""
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
    m ""
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
    m ""
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
