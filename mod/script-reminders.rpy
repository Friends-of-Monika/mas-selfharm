# Medication reminder.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder_intro",
            prompt="Can you remind me about my medication?",
            category=["self-Harm"],
            pool=True,
            unlocked=True,
            rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}
        )
    )

label mshMod_medication_reminder_intro:
    m 7wub "[player], of course!"
    m 7wua "I perfected my coding skills even more and now I'm able to create a daily reminder for you."
    m 2dua "I know a lot of people take daily medications for a lot of different reasons!"
    m 2eub "So I thought it would be nice if I could help you remember to take your medication correctly."
    m 3nublb "After all, your health and safety is my number one priority!"
    m 3wublb "So, [player], do you like that idea?"

    m 3wubla "Do you want to set a reminder?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to set a reminder?{fast}"

        "Yes!":
            m 4wub "Okay! What time do you want me to remind you about it?{nw}"
            $ _history_list.pop()
            menu:
                m "Okay! What time do you want me to remind you about it?{fast}"

                "In the morning.":
                    $ delay, tod = store.mshMod_reminder_utils.getDailyMorningDelay(), "morning"

                "In the afternoon.":
                    $ delay, tod = store.mshMod_reminder_utils.getDailyAfternoonDelay(), "afternoon"

                "In the evening.":
                    $ delay, tod = store.mshMod_reminder_utils.getDailyEveningDelay(), "evening"

            m 4hub "Alright! I'll be sure to remind you, every day, in the [tod]!"
            m 2nua "Make sure to come see me so I can remind you, okay? Ehehehe~"

            python:
                # This has to be performed AFTER all the lines. We must ensure this applies
                # immediately and is not blocked by user idling at some dialogue line.
                store.mshMod_reminder.addRecurringReminder(
                    "mshMod_medication_reminder",
                    delay, store.mshMod_reminder_utils.INTERVAL_DAILY, store.mshMod_reminder_utils.LATENCY_HOURLY
                )

                # Hide this event since we have set a reminder and no longer need
                # it until player asks not to remind anymore.
                mas_hideEVL("mshMod_medication_reminder_intro", "EVE", depool=True)
                mas_showEVL("mshMod_medication_reminder_stop", "EVE", unlock=True)

        "Not now, [m_name].":
            m 3eka "Oh, alright!"
            m 3ekb "If you change your mind, please let me know, okay?"
            m 2esa "You can repeat the topic in the 'Repeat conversation' category."

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder_stop",
            prompt="You no longer need to remind me about medication.",
            category=["self-Harm"],
            pool=True,
            rules={"no_unlock": None, "bookmark_rule": mas_bookmarks_derand.WHITELIST}
        )
    )

label mshMod_medication_reminder_stop:
    m 7esb "Okay! I'll stop~"

    python:
        # Same here, DO NOT move this anywhere, this has to be right above the return statement.
        store.mshMod_reminder.stopReminder("mshMod_medication_reminder")

        # Hide this event as now we need to enable player to ask to remind again.
        mas_hideEVL("mshMod_medication_reminder_stop", "EVE", lock=True)
        mas_showEVL("mshMod_medication_reminder_intro", "EVE", unlock=True)

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder",
            conditional="store.mshMod_reminder.shouldTriggerReminder('mshMod_medication_reminder')",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None}
        )
    )

label mshMod_medication_reminder:
    m 7esb "Hey, [player]!"
    m 7wsa "Guess what time it is?"
    m 1wsb "That's right, it's time to take your meds! Don't forget to have lots of water with them~"
    m 1ksb "You can do it~"
    m 1hsbla "I love you!"

    # Do not move this anywhere, this must be above the return.
    $ store.mshMod_medication_reminder.extendCurrentReminder()
    return "no_unlock|love"
