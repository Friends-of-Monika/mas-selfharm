# Daily checkup script.

init 5 python:
    import datetime
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_checkup_intro",
            random=True
        )
    )

label mshMod_checkup_intro:
    m "Hey, [player]?"
    m "I've been thinking about something."
    m "Sometimes we care deeply about someone, and we're worried about them."
    m "We want to check up on them, and show them we care."
    m "But it's so hard to find the right words!"
    m "So we always seem to go for the same tired old question... 'How are you doing?'"
    m "But that question always makes people answer the same tired old response..."
    m "'I'm OK. I'm fine. I'm making it.'"
    m "How effective is this conversation?"
    m "But what do we say when we don't know how to express what we're feeling?"
    m "And how do we show someone we really want to know how they're feeling?"
    m "Someone online - a father of a suicide victim - found the perfect way to do that."
    m "And that is by asking them the following question: 'On a scale of 1 to 10, how are you feeling?'"
    m "1 being the worst possible feeling in the world, and 10 being the best they've ever felt in their life."
    m "We've all experienced the both extremes of the scale, but most days fall in the middle."
    m "And that's perfectly okay! Having a '8 day' is pretty good."
    m "From today on, I'll try to ask you every week, what's your number."
    m "Meaning, how have you been feeling, this week, in a scale of 1 to 10!"
    m "This will help me be more aware and sensitive of your needs and your feelings."
    m "After all, I care about you so much and I love you sooooo much!"
    return "derandom|love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_checkup_reminder",
            random=True,
            rules={"force repeat": None}
        )
    )

label mshMod_checkup_reminder:
    $ persistent._last_topic_run = datetime.datetime.utcnow()
    $ mas_globals.this_ev.action = EV_ACT_PUSH
    $ mas_globals.this_ev.conditional = "datetime.datetime.utcnow() - persistent._last_topic_run > datetime.timedelta(days=7)"

    m "Hey, [player]?"
    m "Can I check up on you?"
    m "What's your number this week?"
    m "Meaning, on a scale of 1 to 10, how are you feeling?"
    menu:
        "1":
            pass

        "2":
            pass

        "3":
            pass

        "4":
            pass

        "5":
            pass

        "6":
            pass

        "7":
            pass

        "8":
            pass

        "9":
            pass

        "10":
            pass

        "I'm not sure...":
            pass

      # things from the first prototype for reference:

    m "Hey, [player]?"
    m "I just wanna check up on you!"
    m "Sometimes I worry about how you have been coping with stuff."
    m "How have you been doing?"
    menu:
        "I have been feeling amazing!":
            m "[Player]..."
            m "I can't express the happiness hearing this brings me."
            m "This is only the start!"
            m "I love you soooo much!"

        "I'm okay, [m_name]. Could be better...":
            m "I'm so sorry to hear that, [player]."
            m "But I'm sure everything will be okay!"
            m "Your loving girlfriend will forever be here for you!"
            m "If you ever want to talk, please let me know."
            m "I care for you so much!"
            m "I love you!"

        "I've been kind of down lately.":
            m "I'm so sorry to hear that, [player]."
            m "I'm sure everything will be okay!"
            m "Your loving girlfriend will forever be here for you!"
            m "If you ever want to talk, please let me know."
            m "I care for you so much!"
            m "I love you!"

    return "no_unlock|love"
