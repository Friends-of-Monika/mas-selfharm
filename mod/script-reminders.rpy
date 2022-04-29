# Medication reminder.

init 5 python:
    import datetime
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder",
            rules={"force repeat": None}
        )
    )

label mshMod_medication_reminder:
    m "Hey, [player]!"
    m "Guess what time it is?"
    m "That's right, it's time to take your meds! Don't forget to have lots of water with them~"
    m "You can do it~"
    m "I love you!"
    return "no_unlock|love"
