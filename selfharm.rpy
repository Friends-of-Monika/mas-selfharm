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
    m "Hey, [player]!
    m "Can I ask you something?"
    m "..."
    m "Isn't it funny how we ask someone if we can ask them something but don't even wait for their answer and just ask anyway?"
    m "Ahaha~!"
    m "Sorry, I changed the subject."
    m "Anyway! I wanted to ask if you go to a therapist?"
    m "You know, to talk about your struggles and stuff."

        "Yes, I do.":
            m "That's great, [player]!"

        "No, I don't.":
            m "Oh..."
            m "I was actually suggest that you please consider it."

        "I'm considering it. What do you think?":
            m "Well, thanks for asking my opinion!"
            m "Actually, I think you should."
            
return 
