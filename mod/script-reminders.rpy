# Medication reminder.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder_intro",
            prompt="Can you remind me about my medication?",
            category=["self-Harm"],
            conditional="not store.mshMod_reminder.isReminderActive('mshMod_medication_reminder')",
            action=EV_ACT_POOL,
            pool=True
        )
    )

label mshMod_medication_reminder_intro:
    m "Okay! What time do you want me to remind you about it?{nw}"

    menu:
        m "Okay! What time do you want me to remind you about it?{fast}"

        "In the morning.":
            $ delay, tod = store.mshMod_reminder_utils.getDailyMorningInterval(), "morning"

        "In the afternoon.":
            $ delay, tod = store.mshMod_reminder_utils.getDailyAfternoonInterval(), "afternoon"

        "In the evening.":
            $ delay, tod = store.mshMod_reminder_utils.getDailyEveningInterval(), "evening"

    m "Alright! I'll be sure to remind you in the [tod]~"

    python:
        # This has to be performed AFTER all the lines. We must ensure this applies
        # immediately and is not blocked by user idling at some dialogue line.
        store.mshMod_reminder.addRecurringReminder(
            "mshMod_medication_reminder",
            delay, store.mshMod_reminder_utils.INTERVAL_DAILY, store.mshMod_reminder_utils.LATENCY_HOURLY
        )
        mas_hideEVL("mshMod_medication_reminder_intro", "EVE", depool=True)

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder_stop",
            prompt="You no longer need to remind me about medication.",
            category=["self-Harm"],
            conditional="store.mshMod_reminder.isReminderActive('mshMod_medication_reminder')",
            action=EV_ACT_POOL
        )
    )

label mshMod_medication_reminder_stop:
    m "Okay! I'll stop~"

    python:
        # Same here, DO NOT move this anywhere, this has to be right above the return statement.
        store.mshMod_reminder.stopReminder("mshMod_medication_reminder")
        # Hide this event
        mas_hideEVL("mshMod_medication_reminder_stop", "EVE", depool=True)

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder",
            conditional="store.mshMod_reminder.shouldTriggerReminder('mshMod_medication_reminder')",
            action=EV_ACT_PUSH,
            rules={"force repeat": None}
        )
    )

label mshMod_medication_reminder:
    m "Hey, [player]!"
    m "Guess what time it is?"
    m "That's right, it's time to take your meds! Don't forget to have lots of water with them~"
    m "You can do it~"
    m "I love you!"

    # Do not move this anywhere, this must be above the return.
    $ store.mshMod_medication_reminder.extendCurrentReminder()
    return "no_unlock|love"
