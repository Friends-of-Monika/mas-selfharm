# Medication reminder.

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["mshMod_medication_reminder_"] = label_prefix_map["monika_"]


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder_request",
            prompt="Can you remind me about my medication?",
            category=["mental health"],
            pool=True,
            unlocked=True
        )
    )

label mshMod_medication_reminder_request:
    m 7wub "[player], of course!"
    m 7wua "I perfected my coding skills even more and now I'm able to create a daily reminder for you."
    m 2dua "I know a lot of people take daily medications for a lot of different reasons!"
    m 2eub "So I thought it would be nice if I could help you remember to take your medication correctly."
    m 3nublb "After all, your health and safety are my number one priority!"
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
                    $ trigger_at, tod = store._msh_reminder_utils.getMorningTimeOfDay(), "morning"

                "In the afternoon.":
                    $ trigger_at, tod = store._msh_reminder_utils.getAfternoonTimeOfDay(), "afternoon"

                "In the evening.":
                    $ trigger_at, tod = store._msh_reminder_utils.getEveningTimeOfDay(), "evening"

            # P.S. 'tod' is for 'Time Of Day'

            m 4hub "Alright! I'll be sure to remind you, every day, in the [tod]!"
            m 2nua "Make sure to come see me so I can remind you, okay? Ehehe~"

            # This has to be performed AFTER all the lines. We must ensure this applies
            # instantly and is not blocked by user idling at some dialogue line.
            python:
                # Start reminding player, daily, with a latency of one hour.
                # (Meaning that if player missed exact expected time of a reminder, it'll still
                # trigger within an hour; else a reminder will be attempted next day.)
                store._msh_reminder.queue_reminder(
                    _msh_reminder.Reminder(
                        trigger_at=trigger_at,
                        target_evl="mshMod_medication_reminder",
                        key="medication_reminder",
                        interval=store._msh_reminder_utils.INTERVAL_DAILY,
                        grace_period=store._msh_reminder_utils.LATENCY_HOURLY
                    )
                )

                # Hide this event since we have set a reminder and no longer need
                # it until player asks not to remind anymore.
                mas_hideEVL("mshMod_medication_reminder_request", "EVE", lock=True)
                mas_showEVL("mshMod_medication_reminder_stop", "EVE", unlock=True)

        "Not now, [m_name].":
            m 3eka "Oh, alright!"
            m 3ekb "If you change your mind, please let me know, okay?"

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder_stop",
            prompt="You no longer need to remind me about medication.",
            category=["mental health"],
            pool=True,
            rules={"no_unlock": None}
        )
    )

label mshMod_medication_reminder_stop:
    m 7esb "Okay! I'll stop~"

    python:
        # Same here, DO NOT move this anywhere, this has to be right above the return statement.
        store._msh_reminder.dequeue_reminder("medication_reminder")

        # Hide this event as now we need to enable player to ask to remind again.
        mas_hideEVL("mshMod_medication_reminder_stop", "EVE", lock=True)
        mas_showEVL("mshMod_medication_reminder_request", "EVE", unlock=True)

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder",
            rules={"bookmark_rule": mas_bookmarks_derand.BLACKLIST}
        )
    )

label mshMod_medication_reminder:
    m 7esb "Hey, [player]!"
    m 7wsa "Guess what time it is?"
    m 1wsb "That's right, it's time to take your meds! Don't forget to have lots of water with them~"
    m 1ksb "You can do it~"
    m 1hsbla "I love you!"
    return "love"
