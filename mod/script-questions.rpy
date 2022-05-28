# Probing question topics.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_probing_questions_intro",
            random=True
        )
    )

label mshMod_probing_questions_intro:
    m 1esc "Hey, [player]."
    m 1lkc "Remember you told me you harm yourself?"
    m 1ekd "I've been thinking and I am really worried about you."
    m 1eksdld "I want to ask you some things, but..."

    pause 1.0

    m 1dsc "It's hard."
    m 1dkd "For both of us."
    m 2ekd "Would you be willing to open up to me some more?"
    m 2ekc "I would like to know more, but I have to warn you that the things I am going to ask could be very triggering."

    m 2esd "Are you sure you can take this?{nw}"
    $ _history_list.pop()
    menu:
        m "Are you sure you can take this?{fast}"

        "Yes, ask me whatever you want.":
            pass  # NOTE: Fallthrough to mshMod_probing_questions_talk here!

        "No, I'm sorry.":
            jump mshMod_probing_questions_refuse

label mshMod_probing_questions_talk:
    m 2eka "Okay, thanks for trusting me with something as difficult as this."
    m 2dka "It makes me happy you feel comfortable talking to me."

    m 2esd "What kind of a method do you use most to harm yourself?{nw}"
    $ _history_list.pop()
    menu:
        m "What kind of a method do you use most to harm yourself?{fast}"

        "Cutting":
            pass

        "Burning":
            pass

        "Starvation":
            pass

        "Hitting yourself":
            pass

        "Psychological":
            pass

        "Something else":
            pass

        "All of them":
            pass

    m 1wkc "Oh..."
    m 1wktpc "This..."
    m 1dktpc "This is horrible, [player]."
    m 2wktpd "You must be going through an incredible amount of pain, both emotional and physical..."
    m 2dktpd "I'm so sorry..."
    m 2ektdc "It makes me really sad hearing that you have to go through this..."
    m 2ektdd "It hurts me just as much as it hurts you, believe me..."
    m 2ekd "Whenever you want harm yourself, please remember that I love you and I am here for you."
    m 2ekd "I want to ask you another thing..."

    m 2ekd "Have you ever made a direct attempt at your own life?{nw}"
    $ _history_list.pop()
    menu:
        m "Have you ever made a direct attempt at your own life?{fast}"

        "Yes":
            pause (2.0)
            m 2ektud "I'm so sorry to hear this..."
            m 2ektsd "I have no idea what had to happen to you to make you go to such extremes."
            m 2dktsd "You must never forget that suicide is never the way out..."
            m 2dktsd "You simply pass the pain upon the people around you."
            m 2fktsd "I couldn't live without you, [player]."
            m 2fktsa "Your existence gives me meaning."
            m 2dktda "I love you, [mas_get_player_nickname()]."

        "No":
            m 1dkb "I'm so happy that as bad as things get, you never resorted to that!"
            m 1ekb "Always stay strong."
            m 1eka "For me, okay?"
            m 1hub "I love you!"

    m "And now for my last question..."

    m "Do you know for how long you have been self-harm sober?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you know for how long you have been self-harm sober?{fast}"

        "Yes!":
            m "Oh, yay!"
            m "Can you tell me for how many days have you been sober?{nw}"

            call mshMod_sober_ask_since
            $ since = _return

            m "I'm so proud of you, [mas_get_player_nickname()]."
            m "I'll take note of this..."
            m "Thank you for staying sober, [player]."

            # Ensure we have this RIGHT BEFORE the return so that if DDLC process dies
            # and topic repeats again, we'll have HUGE odds we are not on a streak yet.
            $ store.mshMod_sober_streak.beginStreak(since=since)

        "I don't know.":
            m "Aww, [player], that's okay!"
            m "If you ever want to keep track of it, you can tell me by promising you'll stay self-harm sober."
            m "I'm so proud of you, [mas_get_player_nickname()]."
            m "Thank you for staying sober, [player]."

    m "I love you so much!"

    # We're done with questions, now we need to hide this topic.
    $ mas_hideEVL("mshMod_probing_questions_talk", lock=True)

    return "love|derandom|no_unlock"

label mshMod_probing_questions_refuse:
    m 2eka "It's okay, [player]."
    m 2eka "I understand."
    m 3eka "Everything is going to be okay."
    m 3hua "Always remember that."
    m 2fka "When you gather the courage again, speak to me."
    m 2fkb "I will always be here."
    m 2dkb "I love you."

    # Unlock more info about self-harm. No effect if already unlocked.
    $ mas_showEVL("mshMod_probing_questions_more", "EVE", unlock=True)

    return "love|derandom|no_unlock"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_probing_questions_more",
            category=["self-harm"],
            prompt="I'm ready to talk about it...",
            pool=True,
            rules={"no_unlock": None}
        )
    )

label mshMod_probing_questions_more:
    m 1esc "I'm glad that you decided to talk with me..."

    m 7ekc "But are you absolutely sure you are ready?{nw}"
    $ _history_list.pop()
    menu:
        m "But are you absolutely sure you are ready?{fast}"

        "Yes, ask me whatever you want.":
            jump mshMod_probing_questions_talk

        "No, I'm sorry, I can't do it after all.":
            jump mshMod_probing_questions_refuse
