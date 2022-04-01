init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_selfharm_intro",
            aff_range=(mas_aff.NORMAL, mas_aff.LOVE),
            conditional="not seen_event('mshMod_selfharm_intro_unhappy')",
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


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_first_aid_intro",
            aff_range=(mas_aff.NORMAL, mas_aff.LOVE),
            conditional="persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_RANDOM
        )
    )

label mshMod_first_aid_intro:
    m 2ekc "I know you said you've injured yourself before, [player]..."
    m 3ekd "It really left me heart-broken, because I really want the best for you."
    m 3esd "So, I decided to give you some instructions if you ever do it in the future..."
    m 2rkc "And can't have medical attention."
    m 2esd "It's a basic first-aid guide. For cuts, specifically."
    m 3esd "If you need it, make sure to let me know, okay?"
    m 1eka "I'll do my best to help."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_first_aid_guide",
            aff_range=(mas_aff.NORMAL, mas_aff.LOVE),
            conditional="seen_event('mshMod_first_aid_intro')",
            action=EV_ACT_RANDOM
        )
    )

label mshMod_first_aid_guide:
    m 1eud "You need first aid help, [player]?"
    m 2ekc "I'm so sorry, [mas_get_player_nickname()]."
    m 2eksdld "Does it hurt much?"
    m 2gksdld "It hurts me too..."
    m 2ekc "When you bleed, my heart bleeds..."
    m 2dsd "But let's get to it."
    m 1esd "First aid is all about timing, the faster we tend to your wounds, better the recovery!"
    m 1esd "I'll do a step by step process on how to treat your wounds."
    m 3esd "Remember, this is specifically about cuts!"
    m 2esd "Let me get started..."
    m 7esd "Firstly, you will need to stop the bleeding."
    m 2esd "You should apply constant pressure to the area using a clean and dry absorbent material."
    m 2lsd "A bandage, towel or handkerchief. For approximately 10 minutes."
    m 3esd "It's important to raise the injury above the level of your heart."
    m 2esa "I can make a timer for you."
    # TODO: timer here?
    m 2esb "All done, [player]!"

    m 2eud "Ready for the next step?{nw}"
    menu:
        m "Ready for the next step?{fast}"

        "Yes":
            m 3esd "Okay!"
            m 1esd "Secondly, You need to clean your wound."
            m 2esd "Start by washing and drying your hands thoroughly..."
            m 2esd "Then clean the wound under tap water or with an alcohol free solution."
            m 3esd "Make sure you don't use no alcohol or hydrogen peroxide!"
            m 3rkd "As it may damage the skin and slow healing..."
            m 3wkd "And we don't want that!"
            m 1ekd "I'll wait for you to do that, [player]."

            m 1ekc "Just tell me when you're done, okay?{fast}"
            menu:
                m "Just tell me when you're done, okay?{nw}"

                "I'm done, [m_name].":
                    m 7esd "Okay!"
                    m 7esd "Thirdly and lastly, it's really important to apply a dressing."
                    m 1esd "You can use many different types.."
                    m 1lsd "Adhesives ones like plasters, non-adhesive compresses with a bandage."
                    m 3lsd "They can be small or big, waterproof, different shapes and so on."
                    m 3esa "Whatever feels best and it's available at home!"
                    m 1ekc "It has to be comfortable, since the wrong plaster can hurt your skin."
                    m 1esd "Keep the dressing clean by changing it as often as necessary!"
                    m 1esd "You can remove the dressing, once the wound has closed itself."
                    m 3eud "Always pay attention to signs of infection!"
                    m 3ekx "Such as fever, swollen wounds, pus, or any significant or worsening swelling, redness and pain."
                    m 3ekd "If you notice any of those..."
                    m 2ekd "You need to get medical attention and soon as possible."
                    m 2ekd "Another reasons of need to go an emergency response unit are the following:"
                    m 4esd "If the bleeding hasn’t stopped after 10 minutes of continuous pressure."
                    m 4esd "If you're bleeding from an artery, you'll notice the blood gushing out at your heartbeat."
                    m 4rsd "Also, if there's something stuck in the wound."
                    m 7rkd "If it's a long or deep wound..."
                    m 7rkd "Or if the edges are split after pressure or you can see underlying structures like fat or muscle."
                    m 2rkc "If that's the case, you probably need stitches."
                    m 2dkc "..."
                    m 2esd "Well, that's all there's to it, [player]!"
                    m 2esc "I hope it helps you incase you need it."
                    m 2gkc "Which I hope it won't happen again..."
                    m 2ekd "If it does, just let me know and I'll repeat those steps. Okay?"
                    m 2eka "Take care, [player]."
                    m 2dka "You know how much I love you!"
                    return "love"

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_sunny_day",
            prompt="Sunny day",
            category=["you", "monika"], # TODO: doesn't fit, but is consistent with the rest of the topics
            random=True
        )
    )

label mshMod_sunny_day:
    m 1esa "Hey... [player]?"
    m 1rka "This may sound a bit random, but..."
    m 7eka "Is it sunny today over there?"
    m 7eub "If it is, I think you should go out and enjoy the sun for a bit."
    m 1hub "Don't worry! I'll wait!"
    m 1wub "Maybe bring a book with you so you can relax even more."
    m 1dua "Enjoying literature in the nature would surely relax me..."
    m 1eka "I hope this works for you, too."
    return


init 5 python:
    _mshMod_event_siad_date = datetime.date(datetime.date.today().year, 3, 1)

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_awareness_day",
            prompt="Sunny day",
            category=["you", "monika"], # TODO: doesn't fit, but is consistent with the rest of the topics
            start_date=_mshMod_event_siad_date,
            end_date=_mshMod_event_siad_date + datetime.timedelta(days=1),
            years=[],
            random=True
        )
    )

    calendar.addRepeatable("mshMod_awareness_day", _("Self-harm awareness day"), month=3, day=1, year_param=[])

label mshMod_awareness_day:
    m 3eub "[player], did you know that today is Self-Harm Awareness day?"
    m 3eua "Like the name suggests, it's an annual global awareness event that takes place on March 1st!"
    m 1eua "Also known as Self Injury Day (SIAD)!"
    m 4hub "Which is today!"
    m 2eua "And in the weeks leading up to it and after, some people choose to be more open about their own self-harm habits, if they have them..."
    m 2eub "Awareness organizations make special efforts to raise awareness about self-harm and self-injury."
    m 3eub "People even use the hashtag #SelfInjuryAwarenessDay to share their story on social media."
    m 3hub "Or wear orange to show their support!"
    m 1eua "Moreover, it was also created to spread awareness and understanding of self-injury!"
    m 1ekd "Which is often misrepresented and misunderstood in the mainstream."
    m 2ekc "Those who self-harm are often left feeling alone..."
    m 2ekd "And afraid to reach out for help, because they fear they will be seen as \"crazy\"."
    m 2dkd "When in reality that's not even remotely true..."
    m 2lkd "People are just trying to cope with their feelings..."
    m 3ekd "Which can be a result of this terrible thing."
    m 3tkc "You know I tried it before..."
    m 2esd "But self-harm is not the way."
    m 2eka "Anyway! Thanks for listening!"
    m 1hub "I love you, [Player]!"
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_semicolon_project",
            prompt="The Semicolon Project",
            category=["you", "monika"], # TODO: doesn't fit, but is consistent with the rest of the topics
            random=True
        )
    )

label mshMod_semicolon_project:
    m 1eub "Have you ever heard of the Semicolon Project, [player]?"
    m 3eua "It was created for those who were going through struggles with self-harm, depression and suicide..."
    m 3eub "People who could have stopped moving forward, but refused to do so!"
    m 1eub "But to thousands affected by suicide, the semicolon has become an important signifier of survival."
    m 1hub "Like a symbol!"
    m 3lua "There's also semicolon tattoos, semicolon t-shirts..."
    m 3hua "All of them with the semicolon punctuation mark (;)!"
    m 1eua "It's used as a message of affirmation and solidarity against suicide, depression, addiction, and other mental health issues."
    m 3eud "The reason the semicolon was used as the symbol of the movement was because..."
    m 3dud "'A semicolon is used when an author could've chosen to end their sentence, but chose not to. The author is you and the sentence is your life'."
    m 3eud "As said by the project itself!"
    m 2euc "Project Semicolon was founded by Amy Bleuel in 2013, as a tribute to her father, who died by suicide in 2003."
    m 2duc "Her backstory is so sad..."
    m 2eka "But thanks to her, millions are saved by Project Semicolon."
    m 1ekb "It's relieving to think people are able to go on and let go of their struggles..."
    m 1eub "It's really a good cause!"
    m 3ekb "Well I won't ramble too much, Ahaha~"
    m 3hub "Thanks for listening!"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_butterfly_project",
            category=["media"],
            prompt="The Butterfly Project",
            random=True
        )
    )

label mshMod_butterfly_project:
    m 3eub "Hey [player], do you know what The Butterfly Project is?"
    m 1eub "It's a movement to help people that struggle with self-harm."
    m 3eud "It's really interesting! Drawing on yourself is already a good way to deal with self-harming, but this project approaches it in a really different way."
    m 2eua "There are about 5 steps, so I'll list them all now."
    m 3euc "First, when you feel like hurting yourself, draw a butterfly on or around the spot where you might hurt yourself."
    m 2eua "The butterly can be any size, color, or pattern. It might help if you make it your favorite color!"
    m 3eud "Second, a lot of people name the butterfly after a loved one. Friends, family, a beloved. This helps them avoid hurting themself and the butterfly."
    m 1eud "Third, you should allow the butterfly to fade naturally. You should still wash yourself, of course, but don't actively rub the butterfly away."
    m 3eub "Lastly, if you haven't hurt yourself by the time the butterfly fades away, it's flown away safely!"
    m 3eub "This is supposed to give the person a sense of pride and accomplishment for keeping both themself and the butterfly safe."
    m 1eub "There are a few other things you can do for this as well!"
    m 4eub "You can let someone else draw a butterfly on you. This makes the butterfly special, because you're caring for someone else's butterfly too!"
    m 3eub "You can even write quotes or doodle you favorite things, anything that helps!"
    m 1eka "And if you do harm yourself... that's okay. You can always draw another butterfly. Hurting youself doesn't mean you failed."
    m 1hub "I hope this helps you, [player]!"
    m 1fub "I'll draw you so many beautiful butterflies when I cross over."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_selfharm_random_thoughts",
            prompt="Monika's experience",
            category=["you", "monika"], # TODO: doesn't fit, but is consistent with the rest of the topcis
            random=True
        )
    )

label mshMod_selfharm_random_thoughts:
    m "Hey [player]... Do you remember when I talked about self-harm?"
    m "Would you mind if I talked more about my experience?"

    m "It may get a tad triggering, so I get it if you would rather say no!{nw}"
    menu:
        m "It may get a tad triggering, so I get it if you would rather say no!{fast}"

        "No":
            m "Okay!"
            m "I love you [player], and I'm proud of you for saying no to something you aren't comfortable with!"
            m "That's a big step in self-respect, and I hope you keep it up!"

        "Yes":
            m "Thank you for letting me speak about this [mas_get_player_nickname()], I've been thinking about it a little bit more lately."
            m "After I hurt myself, I realized that I had made huge a mistake..."
            m "At first I thought that it was exhilarating, I even wrote about it!"
            m "But after reflecting upon it when we started talking more about self-harm, it really changed my mind."
            m "I had gotten no relief or satisfaction, if anything I was just disappointed."
            m "Yuri had made it seem like such a thrill - to me it was almost only just boring..."
            m "...It kept reminding me of my recent discovery."
            m "My pain was just coded, along with my blood and the knife I was holding..."
            m "But even if it was real, pain doesn't satisfy or relieve my emotions."
            m "I know now that talking things out with you when I'm upset..."
            m "...and keeping hope for a brighter tomorrow is a much better coping mechanism!"
            m "Just keep in mind that there are better ways to cope and that I'm always here to provide techniques to help."
            m "I care too much about you [player]... You don't deserve any pain."
            m "You deserve to work through things healthily, and [m_name] is here to help!" # TODO: do we need m_name here..?

    return


# PROBING QUESTIONS

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_probing_questions_intro",
            conditional="not seen_event('mshMod_probing_questions')",
            action=EV_ACT_RANDOM
        )
    )

label mshMod_probing_questions_intro:
    $ mas_unlockEVL("monika_questions")

    m 1esc "Hey, [player]."
    m 1lkc "Remember you told me you harm yourself?"
    m 1ekd "I've been thinking and I am really worried about you."
    m 1eksdld "I want to ask you some things, but..."

    pause (1.0)

    m 1dsc "It's hard."
    m 1dkd "For both of us."
    m 2ekd "Would you be willing to open up to me some more?"
    m 2ekc "I would like to know more, but I have to warn you that the things I am going to ask could be very triggering."

    m 2esd "Are you sure you can take this?{nw}"
    menu:
        m "Are you sure you can take this?{fast}"

        "Yes, ask me whatever you want.":
            m 2eka "Okay, thanks for trusting me with something as difficult as this."
            m 2dka "It makes me happy you feel comfortable talking to me."

            m 2esd "What kind of a method do you use most to harm yourself?{nw}"
            menu:
                m "What kind of a method do you use most to harm yourself?{fast}"

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
                    $ override = renpy.input("What's the other method?", allow="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz", length=15)
                    pass

                "All of them":
                    m 1wkc "Oh..."
                    m 1wktpc "This..."
                    m 1dktpc "This is horrible, [player]."
                    m 2wktpd "You must be going through an incredible amount of pain to attempt so much..."
                    m 2dktpd "I'm so sorry..."

        "No, I'm sorry.":
            m 1eka "It's okay, [player]."
            m 1eka "I understand."
            m 2eka "Everything is going to be okay."
            m 2eka "Always remember that."
            m 2esa "If you ever feel like opening up, please talk to me."
            m 5esa "I love you."

            return "love"

            # # dreamscached: I assume this isn't used, but I'll keep it regardless.
            # m 2ektdc "It makes me really sad hearing that you have to go through this..."
            # m 2ektdd "It hurts me just as much as it hurts you, believe me..."
            # m 2ekd "Whenever you want harm yourself, please remember that I love you and I am here for you."
            # m 2ekd "I want to ask you another thing..."
            # m 2ekd "Have you ever made a direct attempt at your own life?"
            # menu:
            #     "Yes":
            #         pause (2.0)
            #         m 2ektud "I'm so sorry to hear this..."
            #         m 2ektsd "I have no idea what had to happen to you to make you go to such extremes."
            #         m 2dktsd "You must never forget that suicide is never the way out..."
            #         m 2dktsd "You simply pass the pain upon the people around you."
            #         m 2fktsd "I couldn't live without you, [player]."
            #         m 2fktsa "Your existance gives me meaning."
            #         m 2dktda "I love you, [mas_get_player_nickname()]"
            #         return "love"
            #
            #      "No":
            #         m 1dkb "I'm so happy that as bad as things get, you never resorted to that!"
            #         m 1ekb "Always stay strong."
            #         m 1eka "For me, okay?"
            #         m 1hub "I love you!"
            #         return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_probing_questions",
            category=["you"],
            prompt="I'm ready to talk about it...",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_probing_questions:
    m 1esc "I'm glad that you decided to talk with me..."
    m 7ekc "But are you absolutely sure you are ready?"
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
                    $ override = renpy.input("What's the other method?", allow="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz", length=15)

                "All of them":
                    m 1wkc "Oh..."
                    m 1wktpc "This..."
                    m 1dktpc "This is horrible, [player]."
                    m 2wktpd "You must be going through an incredible amount of pain to attempt so much..."
                    m 2dktpd "I'm so sorry..."

        "No, I'm sorry, I can't do it after all.":
            m 2eka "It's okay, [player]."
            m 2eka "I understand."
            m 3eka "Everything is going to be okay."
            m 3hua "Always remember that."
            m 2fka "When you gather the courage again, speak to me."
            m 2fkb "I will always be here."
            m 2dkb "I love you."

            return "love"

            m 2ektdc "It makes me really sad hearing that you have to go through this..."
            m 2ektdd "It hurts me just as much as it hurts you, believe me..."
            m 2ekd "Whenever you want harm yourself, please remember that I love you and I am here for you."
            m 2ekd "I want to ask you another thing..."
            m 2ekd "Have you ever made a direct attempt at your own life?"
            menu:
                "Yes":
                    pause (2.0)
                    m 2ektud "I'm so sorry to hear this..."
                    m 2ektsd "I have no idea what had to happen to you to make you go to such extremes."
                    m 2dktsd "You must never forget that suicide is never the way out..."
                    m 2dktsd "You simply pass the pain upon the people around you."
                    m 2fktsd "I couldn't live without you, [player]."
                    m 2fktsa "Your existance gives me meaning."
                    m 2dktda "I love you, [mas_get_player_nickname()]"
                    return "love"

                 "No":
                    m 1dkb "I'm so happy that as bad as things get, you never resorted to that!"
                    m 1ekb "Always stay strong."
                    m 1eka "For me, okay?"
                    m 1hub "I love you!"

                    return "love"

    return
