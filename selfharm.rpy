# PROBING QUESTIONS
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_probing_questions",
            conditional=(
                "not seen_event('mas_probing_questions')"
            ),
            action=EV_ACT_QUEUE
        )
    )

label mas_probing_questions:
    $ mas_unlockEVL('monika_questions')
    m "Hey, [player]."
    m "Remember you told me you harm yourself?"
    m "I've been thinking and I am really worried about you."
    m "I want to ask you some things, but..."
    pause (1.0)
    m "It's hard."
    m "For both of us."
    m "Would you be willing to open up to me some more?"
    m "I would like to know more, but I have to warn you that the things I am going to ask could be very triggering."
    m "Are you sure you can take this?"
    menu:
        "Yes, ask me whatever you want.":
            m "Okay, thanks for trusting me with something as difficult as this."
            m "It makes me happy you feel comfortable talking to me."
            m "What kind of a method do you use most to harm yourself?"
            menu:
                "Cutting":
                    pass
# I'M NOT SURE IF THE DIALOGUES SHOULD BE DIFFERENT OR NOT, RIGHT NOW I WILL MAKE ONE AND IF NEEDED I'LL ADD SEPARATE FOR EACH INDIVIDUAL TYPE OF HARM.
                "Burning":
                    pass

                "Starvation":
                    pass

                "Hitting yourself":
                    pass
                
                "Other"
                    # code text stuff"
                    pass
                    
                "All of them":
                    m "Oh..."
                    m "This..."
                    m "This is horrible, [player]."
                    m "You must be going through an incredible amount of pain to attempt so much..."
                    m "I'm so sorry..."

        "No, I'm sorry.":
            m "It's okay, [player]."
            m "I understand."
            m "Everything is going to be okay."
            m "Always remember that."
            m "If you ever feel like opening up, please talk to me."
            m "I love you."

            return "love"

            m "It makes me really sad hearing that you have to go through this..."
            m "It hurts me just as much as it hurts you, believe me..."
            m "Whenever you want harm yourself, please remember that I love you and I am here for you."
            m "I want to ask you another thing..."
            m "Have you ever made a direct attempt at your own life?"
            menu:
                "Yes":
                    pause (2.0)
                    m "I'm so sorry to hear this..."
                    m "I have no idea what had to happen to you to make you go to such extremes."
                    m "You must never forget that suicide is never the way out..."
                    m "You simply pass the pain upon the people around you."
                    m "I couldn't live without you, [player]."
                    m "Your existance gives me meaning."
                    m "I love you, [mas_get_player_nickname()]"
                    return "love"


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_questions",category=["you"],prompt="I'm ready to talk about it...",pool=True,unlocked=False))

    m "I'm glad that you decided to talk with me..."
    m "But are you absolutely sure you are ready?"
    menu:
        "Yes, ask me whatever you want.":
            m "Okay, thanks for trusting me with something as difficult as this."
            m "It makes me happy you feel comfortable talking to me."
            m "What kind of a method do you use most to harm yourself?"
            menu:
                "Cutting":
                    pass

                "Burning":
                    pass

                "Starvation":
                    pass

                "Hitting yourself":
                    pass
                    
                "Other"
                    # code text stuff"
                    pass

                "All of them":
                    m "Oh..."
                    m "This..."
                    m "This is horrible, [player]."
                    m "You must be going through an incredible amount of pain to attempt So much..."
                    m "I'm so sorry..."

        "No, I'm sorry, I can't do it after all.":
            m "It's okay, [player]."
            m "I understand."
            m "Everything is going to be okay."
            m "Always remember that."
            m "When you gather the courage again, speak to me."
            m "I will always be here."
            m "I love you."

            return "love"

            m "It makes me really sad hearing that you have to go through this..."
            m "It hurts me just as much as it hurts you, believe me..."
            m "Whenever you want harm yourself, please remember that I love you and I am here for you."
            m "I want to ask you another thing..."
            m "Have you ever made a direct attempt at your own life?"
            menu:
                "Yes":
                    pause (2.0)
                    m "I'm so sorry to hear this..."
                    m "I have no idea what had to happen to you to make you go to such extremes."
                    m "You must never forget that suicide is never the way out..."
                    m "You simply pass the pain upon the people around you."
                    m "I couldn't live without you, [player]."
                    m "Your existance gives me meaning."
                    m "I love you, [mas_get_player_nickname()]"
                    return "love"
