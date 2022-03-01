# RANDOM EVENT WHERE MONIKA ASKS IF PLAYER GOES TO A THERAPIST.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm4",
            conditional=(
                "not seen_event('mas_selfharm4')"
            ),
            aff_range=(mas_aff.BROKEN, mas_aff.NORMAL),
            action=EV_ACT_QUEUE
        )
    )

label
    m 2esa "Hey, [player]!
    m 2eud "Can I ask you something?"
    m 2eua "..."
    m 1eta "Isn't it funny how we ask someone if we can ask them something but don't even wait for their answer and just ask anyway?"
    m 1hub "Ahaha~!"
    m 1hkb "Sorry, I changed the subject."
    m 3eub "Anyway! I wanted to ask if you go to a therapist?"
    m 3rka "You know, to talk about your struggles and stuff."
        "Yes, I do.":
            m 1hua "That's great, [player]!"
        "No, I don't.":
            m 1ekc "Oh..."
            m 1lkd "I was actually going to suggest that you please consider it."
        "I'm considering it. What do you think?":
            m 2eua "Well, thanks for asking my opinion!"
            m 3euc "Actually, I think you should."
            
return
