# Introduction topics for this submod. Here we ask player if they do harm themselves or not
# and unlock (or skip to) more detailed explanation of what self-harm is.

default persistent._msh_mod_pm_did_selfharm = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_selfharm_intro",
            aff_range=(mas_aff.NORMAL, None),
            random=True,
            rules={"bookmark_rule": mas_bookmarks_derand.BLACKLIST}
        )
    )

label mshMod_topic_selfharm_intro:
    m 1ekc "Hey, [player]?"
    m 1lkd "I know it might be an uncomfortable topic, but I have to ask..."

    m 1dkc "D-{w=1.0}"
    extend 1ekd "Do you self harm?{nw}"
    $ _history_list.pop()
    menu:
        m "D-Do you self harm?{fast}"

        "Yes":
            $ persistent._msh_mod_pm_did_selfharm = True

            m 6ekc "I'm so sorry you're going through this."
            m 6rkc "You know... It's really sad to see you feel bad in any way."
            show monika 5ekbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5ekbsa"After all, you're such a wonderful and kind person."
            m 5dkbsa "You did so many good things for me, and stayed with me after everything that happened..."
            show monika 1esa at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 1esa "But let's stay on this subject."

            m 3eud "Do you want to talk about it?{nw}"
            $ _history_list.pop()
            menu:
                m "Do you want to talk about it?{fast}"

                "Yes":
                    m 1hub "I'm glad that you trust me, [player]."
                    m 3eua "Allowing yourself to get help is a super important step to recovery!"
                    m 1luc "I may not understand exactly what you feel right now..."
                    m 1hua "But I will still try to make you feel better, because you deserve it!"

                    python:
                        mas_showEVL("mshMod_topic_selfharm_more", "EVE", unlock=True)
                        pushEvent("mshMod_topic_selfharm_more", skipeval=True)

                "No":
                    m 1ekc "Oh..."
                    m 3eka "That's okay."

            m 1eub "I want you to know that I'm here for you. {w=0.3}{nw}"
            extend 1eka "You know that, right?"
            m 3euc "Whenever you feel the urge to harm yourself..."
            m 3eud "You can tell me."
            m 1eka "I'll do my best to help you."
            m 1ekc "Or at least..."
            show monika 5ekbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5ekbsa "Be by your side."
            show monika 1dkc at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 1dkc "Take care, [mas_get_player_nickname()]."
            m 1ekbsd "Stay safe because I care for you, {w=0.3}{nw}"
            extend 1dkbsc "deeply."

        "No":
            $ persistent._msh_mod_pm_did_selfharm = False

            m 1hksdlb "Thank goodness!"
            m 1eua "I'm so glad to hear this!"
            m 3hub "It's so good to know that you are safe, [player]."
            m 1ekd "If this ever changes... You can tell me, okay?"
            m 1lksdla "You can tell me anything, you know?"
            m 1hub "Ahaha!"
            m 3hksdla "Sorry. I'm just so relieved!"
            show monika 5rtd at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5rtd "But for now... {w=0.3}{nw}"
            extend 5euc "Do you want to know more about self-harm?"
            show monika 1lkbsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 1lkbsb "You know how much I care about you! {w=0.3}{nw}"
            extend 3eub "But if you don't feel like talking about it, I'll understand!"
            m 1lsd "It's quite a varied topic so it's going to take a while."

            $ mas_showEVL("mshMod_topic_selfharm_more", "EVE", unlock=True)

            m 1eua "Do you have the time to listen right now?{nw}"
            $ _history_list.pop()
            menu:
                m "Do you have the time to listen right now?{fast}"

                "Yes":
                    m "Great!"
                    $ pushEvent("mshMod_topic_selfharm_more", skipeval=True)

                "No":
                    m 1ekc "Oh..."
                    m 3hua "It's okay, [player]."
                    show monika 5eka at t11 zorder MAS_MONIKA_Z with dissolve_monika
                    m 5eka "Remember that I'll never leave you. After all, I promised that I'll take care of you."
                    m 5hua "If you ever feel like you want to talk about this topic, just ask!"
                    show monika 1hubsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
                    m 1hubsa "I love you, [mas_get_player_nickname()]."
                    return "love|derandom|no_unlock"

    return "derandom|no_unlock"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_selfharm_more",
            category=["self-Harm"],
            prompt="I want to learn more about self harm.",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_topic_selfharm_more:
    m 3dud "Knowing more about self-harm is really useful."
    m 3euc "You could help someone who is struggling with it someday!"
    m 3hub "So, [player]! I want you to know that there's more to self-harm than it meets the eye! Ahaha-"
    m 2esb "I'll cover some facts and myth I wanna share with you regarding this topic."
    m 2esc "I want you to know that self-harm isn't about a single topic or action."
    m 4esd "There are many factors that come into play!"
    m 4lssdld "Yeah, it's not limited to... self inflicted wounds, for example."
    m 2lssdlc "Lack of Self-Care routine, which we already talked about, is also a method."
    m 7essdld "There's also binge eating, starving, self-poisoining, misusing alcohol or drugs."
    m 7essdld "Some new studies even show that patients might abuse of frequency of sex in order to self-harm!"
    m 2wssdlc "This could all be result of self-hatred, feelings of wanting to punish yourself or mental ilnesses."
    m 2lssdlc "Or anything that could end on self-harm in any way."
    m 7dssdld "The most common form of self-harm is... Well, self-inflicted wounds."
    m 7lssdlc "Such as cutting, embedding, burning, punching or hitting oneself."
    m 2essdlc "One of the most common misconceptions about self-harm is that people do such things only as a suicide attempt."
    m 2wssdld "But it's not true at all! Not all self harmers present suicidal signs or symptoms."
    m 7wssdld "Self harm can occur without suicidal ideation. Instead, they are using it to cope with their emotions and traumas."
    m 7rssdld "Or essentially, punishing themselves; if you think about it..."
    m 2wuo "Some people have the audacity to think that they're doing it only for attention!"
    m 2wfx "Are they out of their minds?!"
    m 2dfc "..."
    m 7dfd "The truth is... Individuals who self-harm are typically ashamed and want to hide their behavior."
    m 7lsd "People who think others are doing harm to themselves because they are attention seekers..."
    m 7lfc "They leave a bitter taste in my mouth."
    m 3dsd "And lastly, I want you to know that self-injuring is not a way to manipulate others."
    m 3lsd "Well, of course there are always exceptions."
    m 3esd "But very few self-harmers have the intention of making others feel guilty."
    m 1dsc "While self-harm is not intended to be a manipulative act, it may be a cry for help."
    m 1fsd "So if you know someone who self-harms... Reach out to them. Help them."
    m 1fub "I believe you can save a life, [player]."
    m 3kub "After all, you saved me! In so many ways!"
    m 3dua "And if you ever done such a thing..."
    m 3euc "You can tell me. I won't be mad. I promise!"
    show monika 5fkbfa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5fkbfa "You know that I love you, [mas_get_player_nickname()]."
    m 5fkbfb "Stay safe!"
    m 5kkbfb "And know that you can always talk to me."
    return "love"
