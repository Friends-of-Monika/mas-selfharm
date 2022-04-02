#MEDICATION REMINDERS - AMY

init 5 python:
    import datetime
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_medicationreminder",
            random=True,
            rules={"force repeat": None}
        )
    )

label monika_medicationreminder:
    $ persistent._last_topic_run = datetime.datetime.utcnow()
    $ mas_globals.this_ev.action = EV_ACT_PUSH
    $ mas_globals.this_ev.conditional = "datetime.datetime.utcnow() - persistent._last_topic_run > datetime.timedelta(minutes=1440)"
    # You can alter the minutes

    m "Hey, [player]!"
    m "It's your daily reminder to take your medication."
    m "You can do it~"
    m "I love you!"
    m "Time since last topic shown: [mas_globals.this_ev.conditional]"
    # Yeah I'll let someone else write this dialogue lol, but this should work!
    return "no_unlock|love"

#MEDICATION REMINDERS - DREAM
