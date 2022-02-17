# RANDOM EVENT, TECHNIQUE 1.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm3",
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm3:

    m "Hey... [player]?"
    m "This may sound a bit random, but..."
    m "Is it sunny today over there?"
    m "If it is, I think you should go out and enjoy the sun for a bit."
    m "Don't worry! I'll wait!"
    m "Maybe bring a book with you so you can relax even more."
    m "Enjoying literature in the nature would surely relax me..."
    m "I hope this works for you, too."
    
return
