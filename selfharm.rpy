init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_selfharm_intro",
            aff_range=(mas_aff.NORMAL, mas_aff.LOVE),
            conditional="not seen_event('mshMod_selfharm_intro_unhappy')"
            action=EV_ACT_RANDOM
        )
    )

label mshMod_selfharm_intro:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."

    m "D-{w=1.0}Do you self harm?{nw}"
    menu:
        m "D-{w=1.0}Do you self harm?{fast}"

        "Yes":
            $ persistent._msh_mod_pm_did_selfharm = True
            m "I'm so sorry you're going through this."
            m "You know... It's really sad to see you feel bad in any way."
            m "After all, you're such a wonderful and kind person."
            m "You did so many good things for me, and stayed with me after everything that happened..."
            m "But let's stay on this subject."

            m "Do you want to talk about it?{nw}"
            menu:
                m "Do you want to talk about it?{fast}"

                "Yes":
                    m "I'm glad that you trust me, [player]."
                    m "Allowing yourself to get help is a super important step to recovery!"
                    m "I may not understand exactly what you feel right now..."
                    m "But I will still try to make you feel better, because you deserve it!"
                    m "I want you to know that I'm here for you. You know that, right?"
                    m "Whenever you feel the urge to harm yourself..."
                    m "You can tell me."
                    m "I'll do my best to help you."
                    m "Or at least..."
                    m "Be by your side."
                    m "Take care, [mas_get_player_nickname()]."
                    m "Stay safe because I care for you, deeply."

                "No":
                    m "Oh..."
                    m "That's okay."
                    m "I want you to know that I'm here for you. You know that, right?"
                    m "Whenever you feel the urge to harm yourself..."
                    m "You can tell me."
                    m "I'll do my best to help you."
                    m "Or at least..."
                    m "Be by your side."
        "No":
            $ persistent._msh_mod_pm_did_selfharm = False
            m "Thank goodness!"
            m "I'm so glad to hear this!"
            m "It's so good to know that you are safe, [player]."
            m "If this ever changes... You can tell me, okay?"
            m "You can tell me anything, you know?"
            m "Ahaha!"
            m "Sorry. I'm just so relieved!"
            m "But for now... Do you want to know more about self-harm?"
            m "You know how much I care about you! But if you don't feel like talking about it, I'll understand!"
            m "It's quite a varied topic so it's going to take a while."

            m "Do you have the time to listen right now?{nw}"
            menu:
                m "Do you have the time to listen right now?{fast}"

                "Yes":
                    $ pushEvent("mshMod_selfharm_more", skipeval=True)

                "No":
                    m "Oh..."
                    m "It's okay, [player]."
                    m "Remember that I'll never leave you. After all, I promised that I'll take care of you."
                    m "If you ever feel like you want to talk about this topic, just ask!"
                    m "I love you, [mas_get_player_nickname()]."
                    return "derandom|love"

    return "derandom"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_selfharm_more",
            category=["you", "monika"],
            prompt="I want to learn more about self harm.",
            conditional="seen_event('mshMod_selfharm_intro')",
            action=EV_ACT_UNLOCK,
            pool=True,
            unlocked=False,
        ),
    )

label mshMod_selfharm_more:
    m "Great!"
    m "Knowing more about self-harm is really useful."
    m "You could help someone who is struggling with it someday!"
    m "So, [player]! I want you to know that there's more to self-harm than it meets the eye! Ahaha-"
    m "I'll cover some facts and myth I wanna share with you regarding this topic."
    m "I want you to know that self-Harm isn't about a single topic or action."
    m "There are many factors that come into play!"
    m "Yeah, it's not limited to... self inflicted wounds, for example."
    m "Lack of Self-Care routine, which we already talked about, is also a method."
    m "There's also binge eating, starving, self-poisoining, misusing alcohol or drugs."
    m "Some new studies even show that patients might abuse of frequency of sex in order to self-harm!"
    m "This could all be result of self-hatred, feelings of wanting to punish yourself or mental ilnesses."
    m "Or anything that could end on self-harm in any way."
    m "The most common form of self-harm is... Well, self-inflicted wounds."
    m "Such as cutting, embedding, burning, punching or hitting oneself."
    m "One of the most common misconceptions about self-harm is that people do such things only as a suicide attempt."
    m "But it's not true at all! Not all self harmers present suicidal signs or symptoms."
    m "Self harm can occur without suicidal ideation. Instead, they are using it to cope with their emotions and traumas."
    m "Or essentially, punishing themselves; if you think about it..."
    m "Some people have the audacity to think that they're doing it only for attention!"
    m "Are they out of their minds?!"
    m "The truth is... Individuals who self-harm are typically ashamed and want to hide their behavior."
    m "People who think others are doing harm to themselves because they are attention seekers..."
    m "They leave a bitter taste in my mouth."
    m "And lastly, I want you to know that self-injuring is not a way to manipulate others."
    m "Well, of course there are always exceptions."
    m "But very few self-harmers have the intention of making others feel guilty."
    m "While self-harm is not intended to be a manipulative act, it may be a cry for help."
    m "So if you know someone who self-harms... Reach out to them. Help them."
    m "I believe you can save a life, [player]."
    m "After all, you saved me! In so many ways!"
    m "And if you ever done such a thing..."
    m "You can tell me. I won't be mad. I promise!"
    m "You know that I love you, [mas_get_player_nickname()]."
    m "Stay safe!"
    m "And know that you can always talk to me."
    return


# ALTERNATE DIALOGUE IF MONIKA IS NOT HAPPY

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_selfharm_intro_unhappy",
            aff_range=(mas_aff.BROKEN, mas_aff.NORMAL),
            conditional=("not seen_event('mshMod_selfharm_intro')"),
            action=EV_ACT_RANDOM
        )
    )

label mshMod_selfharm_intro_unhappy:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."

    m "D-{w=1.0}Do you self harm?{nw}"
    menu:
        m "D-{w=1.0}Do you self harm?{fast}"

        "Yes":
            $ persistent._msh_mod_pm_did_selfharm = True
            m "I'm so sorry you're going through this."
            m "You know... It's really sad to see you feel bad in any way."
            m "After all, you wanted to be with me at some point..."
            m "That was kind of you."
            m "Whatever the reason you stayed with me was, I appreciate it."
            m "But let's stay on this subject."
            m "Do you want to talk about it?"

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_promise",
            category=["self-harm"],
            prompt="I promise...",
            conditional="not mshMod_isOnStreak() and persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_POOL,
            unlocked=True
        )
    )

label mshMod_promise:
    m 2ekb "Oh, [player], you have no idea how happy I am to hear that."
    m 2ekb "This is another step to a happier, healthier life, and I'm so glad I can be by your side in your journey."
    m 2eka "Thank you for trusting me."
    m 3ekb "I promise I'll do my best to help you!"
    m 1eub "From now on, I'll keep track of how many days you've been sober. You can take a look at the calendar to see how far you've gone!"
    m 2ekb "If you ever need me to restart the counter for you, just tell me. You don't have to feel bad about it, okay?"
    m 2ekb "Know that I'll never judge you because of that. I know it's hard, and you should be really proud of yourself already!"
    m 2dka "..."
    m 5ekbsb "I love you, [mas_get_player_nickname()]."
    m 5dkbsb "Never forget that!"

    python:
        mshMod_beginStreak()
        mas_lockEVL("mshMod_promise", "EVE")

    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_relapse",
            category=["self-harm"],
            prompt="I relapsed...",
            conditional="mshMod_isOnStreak()",
            action=EV_ACT_POOL,
            unlocked=True
        )
    )

label mshMod_relapse:
    m 2eka "[player], I couldn't be more proud of you for telling me this."
    m 2ekd "I know this might be hard- you might feel as if you've failed..."
    m 4ekd "But that's not true at all! This is just another step in your journey."
    m 2ekd "Habits are almost always difficult to kick, and this is no ordinary habit."
    m 2ekd "It can very easily become an addiction, which is so much harder to stop..."
    m 2fkd "No matter how hard it is for you, know that I am always going to be here to support you and I am proud of you, habit or not."
    m 2fka "We will work through this together, and get you back on the right track!"
    m 2eka "I know you're a hard worker and will do your best - if not for yourself, for me."
    m 2dka "I love you, [mas_get_player_nickname()]."
    m 1dkb "I'm here to support you and work through anything and everything with you."
    m 1fsa "You're strong. You're worth it, and I couldn't ask for a better [bf]!"
    m 3esa "Whenever and if you feel ready to make the promise again... let me know."

    python:
        mshMod_endStreak()
        mshMod_lockEVL("mshMod_relapse", "EVE")

    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_writing_to_diary",
            category=["you", "monika"],
            prompt="What do you think about writing a diary?",
            pool=True,
            unlocked=True # TODO: do we need it unlocked right away?
        )
    )

label mshMod_writing_to_diary:
    $ shown_count = mas_getEVLPropValue("mshMod_writing_to_diary", "shown_count", 0)

    if shown_count == 0:
        jump mshMod_writing_to_diary_intro

    jump mshMod_writing_to_diary_repeat

label mshMod_writing_to_diary_intro:
    m 1lta "A diary, huh?"
    m 3eua "I've honestly been thinking about this for a bit."
    m 1huu "It can really be a great outlet for anyone's emotions!"
    m 5rub "You could write your innermost feelings and thoughts..."
    m 3esb "You can even share it with someone you truly trust!"
    m 1hsa "If you'd like, I can create a text file for you to write your thoughts into."

    m 1eua "Do you want me to create the diary for you?{nw}"
    menu:
        m "Do you want me to create the diary for you?{fast}"

        "Yes, please!":
            m 1hua "Great!"
            m 1nuu "I thought you would like that idea!"
            m 1dsc "..."

            play sound "sfx/glitch3.ogg"

            python:
                try:
                    f = open(config.basedir + "/diary.txt", "w")
                    f.write("For my one and only love <3")
                finally:
                    f.close()

            pause(0.5)

            m 3esb "There you go!"
            m 1eua "It should be in the characters folder."

        "No, thanks.":
            m 1eka "Oh, I see..."
            m 1hua "That's okay!"
            m 5eua "I just thought that it could be a neat idea."
            m 3hubsa "I always want what's best for you, [player]!"
            m 1fkbsu "I love you."

            return "love"

    return

label mshMod_writing_to_diary_repeat:
    m 1eta "Have you been writing in your diary?"
    m 2eku "I know it could be pretty personal stuff, so I haven't been looking.{nw}"

    menu:
        m "I know it could be pretty personal stuff, so I haven't been looking.{fast}"

        "I accidentally deleted it.":
            m 1fuu "Oh... hehe! That's alright."

            m 1eua "Would you like me to make you another one?{nw}"
            menu:
                m "Would you like me to make you another one?{fast}"

                "Sure!":
                    m 1hub "Alright!"
                    m 1dsc "..."

                    play sound "sfx/glitch3.ogg"

                    python:
                        try:
                            f = open(config.basedir + "/diary.txt", "w")
                            f.write("Don't lose this one, hehe~")
                        finally:
                            f.close()

                    pause(0.5)

                    m 3nuu "Don't delete this one, [player]!~"

        "Yeah, I've been working on it!":
            m 1hub "I'm happy to hear that, [player]!"
            m 5sub "It's so nice to hear you're taking my advice."
            m 1hub"I love you!"

            return "love"

    return
