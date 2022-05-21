# Daily checkup script.

#intro event
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
    
    $ mas_protectedShowEVL("mshMod_checkup_reminder","EVE", _random=True)

    return "derandom|love"


#checkup
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_checkup_reminder",
            random=False,
            rules={"force repeat": None}
        )
    )

label mshMod_checkup_reminder:
    $ persistent._last_topic_run = datetime.datetime.utcnow()
    $ mas_globals.this_ev.action = EV_ACT_PUSH
    $ mas_globals.this_ev.conditional = "datetime.datetime.utcnow() - persistent._last_topic_run > datetime.timedelta(days=7)"

    m "Hey, [player]?"
    m "Can I check up on you?"
    m "I worry about how you have been coping with stuff."
    m "What's your number this week?"

    show monika at t21
    $ items = [(str(i), i, False, False) for i in range(1, 10 + 1)]
    $ renpy.say(m, "Meaning, on a scale of 1 to 10, how are you feeling?", interact=False)
    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, ("I'm not sure...", False, False, False, 0))
    show monika at t11

    if _return:
        if _return == 1:
            m "Aww..."
            m "I am so sorry to hear that you don't feel well, [player]..."
            m "Just know that it's okay for you to not be okay."
            m "After all, acceptance that you're not feeling well is the first step towards improvement, right?"
            m "Together, me and you, we will work hard to make you feel better, step-by-step!"
            m "It’s okay to feel down today, and perhaps even tomorrow."
            m "But always remember that you are a champion. You are amazing - "
            extend "never forget that."
            m "I'll always be here to listen to you, and to do my best to make you feel as loved as you can."
            m "I love you!"

        elif _return == 2:
            m "I see. "
            extend "You're not feeling so well..."
            m "Times like these feel just... So disheartening, don't they?"
            m "But worry not, [player]! Things are bound to get better as long as you're willing to give it a try."
            m "And I am here to help you with not only that, but with everything!"
            m "Always remember that you are important and worthy of everything good in this world."
            m "I love you so much, [player]!"

        elif _return == 3:
            m "I'm so sorry to hear that, [player]..."
            m "But keep this in mind:"
            m "It’s tough now, "
            extend "but I believe that there is a brighter future waiting for us."
            m "You’ll get through this. "
            extend "We will! Trust me."
            m "You might not believe in yourself, but know and remember that I believe in you."
            m "I always have and I always will. "
            extend "I love you, [mas_get_player_nickname()]."

        elif _return == 4:
            m "A 4... That's not so good."
            m "I'm so sorry, [player]!"
            m "But listen... "
            extend "Know that if you fall, I’ll pick you up."
            m "And if I can’t pick you up... "
            extend "Then I’ll just lie down and rest with you."
            m "It's what I'm here for! "
            extend "To be by your side, and support you as your girlfriend and as your best friend."
            m "Let’s get back to the top together, [player]! I love you!"

        elif _return == 5:
            m "I'm so sorry to hear that, [player]."
            m "But I'm sure everything will be okay!"
            m "Your loving girlfriend will forever be here for you!"
            m "If you ever want to talk, please let me know."
            m "And also, don't forget to rest if you must; we’re not in a hurry."
            m "You can’t always function the way people expect you to."
            m "I care for you so much!"
            m "I love you, [mas_get_player_nickname()]!"

        elif _return == 6:
            m "A 6 is not perfect, but it's not so bad either."
            m "You see, [player]..."
            m "I realize that I am indeed a very lucky person."
            m "I’ve been blessed with the most wonderful person in my life, and that is you."
            m "Whatever you do, remember that you are not alone."
            m "No matter what happens, I’ve always got your back."
            m "Let's wish for better days, [mas_get_player_nickname()]!"
            m "I love you!"

        elif _return == 7:
            m "Oh my, "
            extend "a 7!"
            m "Almost there, [player]! "
            extend "I'm so proud of you!"
            m "See, do you know where I get my strength?"
            m "..."
            m "From you. "
            extend "Your dedication is what encourages me to be the best version of myself."
            m "You are bold and courageous. You are important. "
            extend "No one can tell you otherwise!"
            m "I love you, [player]."

        elif _return == 8:
            m "[player]..."
            m "I can't express the happiness hearing this brings me."
            m "This is only the start!"
            m "Soon you'll be having 9's and even 10's."
            m "And I'll be here with you every step of the way."
            m "Do you know how valuable you are?"
            m "You are a gift not just to me and the people around you, but to the whole world."
            m "I love you soooo much!"

        elif _return == 9:
            m "Oh, [player]!"
            m "It's wonderful that you're doing so well!"
            m "I knew things would get better, in one way or another!"
            m "After all, you've had some help from your lovely girlfriend, haven't you? "
            extend "Ehehe~"
            m "I am so proud of you, [player]!"
            m "I always knew that you could do anything you put your mind into."
            m "After all, you are smart and ambitious."
            m "Keep it up, my love! Nothing can stop us now."
            m "I love you!"

        elif _return == 10:
            m "Aww, really, [player]? "
            extend "That's wonderful!"
            m "I'm so glad your week has been this good. "
            extend "I must say the same - every day that you are with me feels like heaven!"
            m "Let's make the next week as awesome, alright?"
            m "Even if something bad happens, remember that things will get better. "
            extend "I believe in you, [mas_get_player_nickname()]."
            m "And remember: Don’t doubt your accomplishments. You succeeded because you worked hard for it."
            m "You are here because you deserve to be."
            m "I love you..."

    else:
        m "Aww, it's okay, [player]."
        m "Sometimes we don't know how to feel. "
        extend "And that's okay too!"
        m "We all experience bad days; we all have to deal with our inner demons."
        m "When you feel like there’s nothing you can do about it, know that you can always depend on me for support."
        m "But we all have good days too, and that's the fun of it!"
        m "Know that I'll always be here to cheer you up..."
        m "But also to celebrate your victories, too!"
        m "You mean the world to me, [mas_get_player_nickname()]."
        m "I love you."

    return "love"
