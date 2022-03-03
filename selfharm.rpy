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

    m 1esa "Hey... [player]?"
    m 1rka "This may sound a bit random, but..."
    m 7eka "Is it sunny today over there?"
    m 7eub "If it is, I think you should go out and enjoy the sun for a bit."
    m 1hub "Don't worry! I'll wait!"
    m 1wub "Maybe bring a book with you so you can relax even more."
    m 1dua "Enjoying literature in the nature would surely relax me..."
    m 1eka "I hope this works for you, too."
    
return
