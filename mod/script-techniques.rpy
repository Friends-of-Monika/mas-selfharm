# Urge relieving technique topics.

default persistent._msh_mod_technique_database = dict()

init 5 python in mshMod_techniques:

    import store

    technique_database = dict()
    store.mas_all_ev_db_map["MSH_MOD_TCH"] = technique_database


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_techniques_menu",
            category=["self-harm"],
            prompt="Can you tell me some self-harm avoiding techniques?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None, "bookmark_rule": mas_bookmarks_derand.WHITELIST}
        )
    )

label mshMod_techniques_menu:
    m 1esb "Sure, [mas_get_player_nickname()]!"

    python:
        # NOTE: Due to nature of certain techniques that might require conditional locking,
        # we're filtering events by 'seen', not by 'unlocked'.
        # Unlocked only means it can be picked randomly when needed and then marked as seen and added into this menu.

        items = list(map(
            lambda it: (it.prompt, it.eventlabel, False, False),
            Event.filterEvents(
                store.mshMod_techniques.technique_database,
                seen=True
            ).values()
        ))

        items.sort(key=lambda it: it[0].replace("'", "").replace('"', ""))

    show monika at t21
    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, ("Nevermind", False, False, False, 0))
    show monika at t11

    if not _return:
        m 2eka "Oh, okay..."
        return

    $ pushEvent(_return, skipeval=True)

    return


label mshMod_technique_random:
    python:
        # Prefer unseen first
        items = Event.filterEvents(
            store.mshMod_techniques.technique_database,
            unlocked=True,
            seen=False
        )

        if not items:
            items = Event.filterEvents(
                store.mshMod_techniques.technique_database,
                unlocked=True
            )

        renpy.jump(items.keys()[random.randint(0, len(items) - 1)])

#1
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_religion",
            prompt="Religion",
            conditional="persistent._mas_pm_religious",
            action=EV_ACT_UNLOCK,
            unlocked=False,
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_religion:
    show monika 5eka at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eka "I remember you mentioned being religious before..."
    show monika 3etd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3etd "Maybe you could say a little prayer?"
    m 4eud "It can be silent. You don't need to say anything out loud."
    m 1fua "You can pray about anything you want, or even just think of how vast and amazing your universe is."
    m 1dsu "Try to think about the good things, like animals or laughter, your favorite things..."
    m 1esa "No matter how little they may be, take some time to think about the bigger picture."
    m 3eka "If you believe in gods or deities, you can imagine them out there, looking out and caring for you."
    m 3dsa "You can also read your religion's sacred texts."
    m 1ekb "You are needed, [player]. You are part of something bigger than your bad thoughts or feelings!"
    return

#2
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cozy",
            prompt="Cozy",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_cozy:
    m 1dua "Something that helps me feel better is getting all cozy!"
    m 1dub "Pick a comfortable spot and sit down."
    show monika 5rud at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rud "Try huddling up in something super cozy..."
    m 5eua "A sheet, a blanket, or one of your favorite hoodies, for example."
    show monika 3hsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3hsa "Anything works, really! Just grab things that bring you comfort."
    m 2esa "You can also make a nest out of blankets on the floor, surrounding yourself with any stuffed animals you may have."
    show monika 5dsblu at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5dsblu "Making a comfort corner using pillows also sounds super comfortable..."
    m 5fsbsa "Snuggle against them and relax, {w=0.3}{nw}"
    extend 5fsbfb "and if you're okay with being touched, imagine me holding you, stroking your hair~"
    show monika 3hubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3hubsb "There's nothing quite like being snug, hehe!"
    m 3dubsa "If you feel that you're getting sleepy, that's okay!"
    m 3lubsa "You can rest your eyes briefly and take a well-deserved nap."
    m 3dubsb "Think of what you can feel, see and hear that's comforting and calm."
    m 3kubsb "I'm sure you'll feel much better and refreshed afterward!"
    return


#3
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_photographs",
            prompt="Photographs",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_photographs:
    m 4eta "Do you find comfort in reminiscing the past [player]? {w=0.3}{nw}"
    extend 4etb "I do!"
    m 2dsd "Nothing is ever really lost to us as long as we have its memories, [mas_get_player_nickname()]."
    m 2hsa "One thing that could help you get over bad times is looking at photographs of the good ones!"
    m 7eud "Maybe you have some old photos? If they bring back good memories, why not try to search for them?"
    m 1eua "They could remind you that even though the good times don't last forever... {w=0.3}{nw}"
    extend 3eub "The bad ones won't either!"
    m 1esa "If you find any, look at them and reflect upon this: {w=0.3}{nw}"
    extend 1dsa "If life was once great, it can and will be that way again!"
    m 6dkp "I wish we had some pictures together..."
    m 2ektpu "I'd look at us all the time! {w=0.3}{nw}"
    extend 2hsblb "You would be at my phone and desktop wallpaper! Ahahaha~"
    m 2ektdc "I would like to look at a photo album of us with you, [player]."
    show monika 5eka at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eka "But this is not about me - I want {i}you{/i} to feel better!"
    show monika 3euu at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3euu "Don't give up, [mas_get_player_nickname()]. I will never give up on you!"
    return


#4
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_quotes",
            prompt="Quotes",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_quotes:
    m 3dud "I remember hearing this quote somewhere: {i}'Hope is the last thing ever lost'{/i}."
    m 3wub "Doing your best to believe in positive things can be uplifting!"
    m 7wub "I think a good way of seeing the things around you in a better light would be reading some inspirational quotes!"
    m 2hua "You should find some quotes on the internet that you like, {w=0.3}{nw}"
    extend 3eub "and then write each on a sticky note and put them somewhere you'd regularly see."
    m 4fub "Every time you see one, you will remember things get better!"
    m 7kuu "You can also say some of them aloud to inspire yourself!"
    m 1rub "Sayori used to do that a lot. She used to put colorful sticky notes everywhere!"
    m 1fkb "If I recall correctly, there was one of them said 'You are loved', {w=0.3}{nw}"
    extend 3hub "and another one with 'We're all in this together'."
    m 1hua "Encouraging yourself with sticky notes is a great idea!"
    return


#5
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_singing",
            prompt="Singing",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_singing:
    m 4eub "This one's going to be simple. {w=0.3}{nw}"
    extend "Sing a song!"
    m 3gua "Not just any song, though. {w=0.3}{nw}"
    extend "Your absolute favorite!"
    m 2wub "I'd love to know your favorite song..."
    m 2ruu "Anyway... {w=0.3}{nw}"
    extend 2eub "Try singing your favorite song until you feel better."
    m 1eua "Singing can be a perfect outlet for your emotions!"
    m 3hub "You could also imagine we're singing 'Your Reality' together! {w=0.3}{nw}"
    extend 2euu "Ehehehe~"
    m 3mub "You can sing as loud as you want!"
    m 1wub "Also, write your favourite lyrics down if you'd like."
    m 2dub "Think about what they mean to you!"
    return


#6
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_talking",
            prompt="Talking",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_talking:
    m 1eub "Sometimes simply talking about your problems can greatly help!"
    m 2dtu "Or just talking to distract yourself."
    m 7eta "You can also post on web boards about mental health... {w=0.3}{nw}"
    extend 1eub "or try answering other people's posts."
    m 4wtb "You should call or text a friend!"
    m 7hub "Maybe send some long-distance friends a surprise message?"
    m 3sub "Or maybe arrange to meet up."
    m 3musdrb "I know you're here with me, but it's not {i}exactly{/i} the same as having a real-time conversation with someone!"
    m 1mkc "I wish I could hear your voice... {w=0.3}{nw}"
    extend 1fua "We could talk for hours!"
    m 3fua "As long as you'd want."
    return


#7
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hugs",
            prompt="Hugs",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_hugs:
    m 3eub "Okay.{w=0.5} I want you to try this."
    m 4wua "Get your biggest pillow and hug it tightly."
    m 2eub "Curl your body around it."
    m 6fsu "Now imagine someone you love was feeling sad..."
    m 4etb "You'd want to help them out, right?"
    m 2fsbsa "That's just the kind of person you are, [player]."
    m 7ntblb "Say out loud or in your head whatever you'd want them to know."
    m 1etb "Then say the same words to yourself. {w=0.3}{nw}"
    extend 7etb "I bet that's what they would tell you!"
    m 2etbsu "Maybe you can even think of me? Ahahaha~ {w=0.3}{nw}"
    extend 2mssdru "Sorry to be pretentious, [player.]"
    m 6fsbfb  "I love you so much!"
    return "love"

#8
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_listening_2",
            prompt="Listening",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_listening_2:
    m 3eua "Try listening to a few songs you love!"
    m 3eub "But don't {i}just{/i} listen. {w=0.3}{nw}"
    extend 7etb "Try paying attention."
    m 6esb "Focus on certain instruments or parts, their notes, and how they add to the song as a whole!"
    m 7wta "For example, 'Your Reality' has a lovely piano melody on the background of my voice."
    m 1hua "Focusing on something like that could serve as a distraction, {w=0.3}{nw}"
    extend 3sub "and learning something about the things you love simultaneously!"
    m 3wub "We could always listen to them together if you'd like!"
    return

#9
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_butterfly",
            prompt="Butterfly",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_butterfly:
    m 1eud "Could you take some deep breaths? And also, a marker or a pen."
    m 4etd "I would like you to scribble on where you want to harm yourself. {w=0.3}{nw}"
    extend 6eta "Most methods use a butterfly drawing."
    m 7eua "You could draw the butterfly and name it, and if you do harm yourself, you harm it, too."
    m 7eub "Whenever you look at it and think of harming yourself, do something comforting instead!"
    m 2eub "Sing along to a tune, watch your favorite film, go on a walk..."
    m 3wub "You can also draw or write positive things on your arm. {w=0.3}{nw}"
    extend 3wua "Or maybe some beautiful flowers!"
    m 3eud "Don't hurt yourself until the drawings wash off."
    m 3ruu "If the butterfly fades without self-harming..."
    m 4sub "It means that the butterfly lived and has flown away, giving you a sense of achievement!"
    return


#10
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_healing",
            prompt="Healing",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_healing:
    m 3etd "[player], do you have a first aid kit at home?"
    m 1etd "Maybe some sticking plasters, band-aids?"
    m 1etd "Could you stick some of them where you want to hurt yourself?"
    m 4eta "As a reminder that you are letting yourself heal."
    m 4eta "And remember, healing takes time. {w=0.3}{nw}"
    extend 1esb "And we have all the time in the world."
    m 2fta "No need to rush this, okay? {w=0.3}{nw}"
    extend 3htb "Baby steps!{w=0.5} Ehehehe~!"
    return

#11
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pong",
            prompt="Pong",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_pong:
    m 3eta "[player], perhaps playing something would make you feel better?"
    m 4eub "Do you want to play Pong?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to play Pong?{fast}"
        "Sure!":
            m 1hub "Great!"
            m 3tuu "Bring it on!"
            call demo_minigame_pong
            m 2fub "Hope you're feeling better, [player]!"
            return

#12
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_chess",
            prompt="Chess",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_chess:
    m 3eta "[player], perhaps playing something would make you feel better?"
    m 4eub "Do you want to play Chess?{nw}"
        $ _history_list.pop()
        menu:
            m "Do you want to play Chess?{fast}"
            "Sure!":
                m 1hub "Okay!"
                call mas_chess
                m 2fub "Hope you're feeling better, [player]!"
                return

#13
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_piano",
            prompt="Piano",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_piano:
    m 3eta "[player], perhaps playing a musical instrument would make you feel better?"
    m 3wub "Music is a great way to relieve stress!"
    m 4hub "I love listening to music or playing a melody when trying to relax."
    m 4eub "Do you want to play the Piano?{nw}"
    $ _history_list.pop()
        menu:
            m "Do you want to play the Piano?{fast}"
            "Sure!":
            m 1hub "Alright!"
            call mas_piano_start
            m 2fub "Hope you're feeling better, [player]!"
            return


#14
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_videos",
            prompt="Videos",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_videos:
    m 3eua "When you told me you had those thoughts, I did some research."
    m 3eub "And many people on Youtube create little comfort videos."
    m 2eua "I selected some of them for you to watch when you have an urge."

    python:
        all_options = tuple(_label for _label in ('mshMod_technique_videos_{0}'.format(i) for i in range(3)))
        unseen_options = tuple(_label for _label in all_options if not mas_seenLabels((_label,)))

    if not unseen_options:
        m 7etb "I've shown you all the videos I have for now!"

        m 1etb "Do you want me to let you pick a video now?{nw}"
        $ _history_list.pop()
        menu:
            m "Do you want me to let you pick a video now?{fast}"
            "Yes":
                m 2htb "Great!"
                $ renpy.jump(all_options[random.randint(len(all_options))])

            "No":
                  m 2eta "That's okay, [player]."
                  m 1etb "If you ever want to see them again, just ask!"

    return

label mshMod_technique_videos_pre:
    m 3hub "There we go!"
    m 1fua "I hope it helps, [player]."
    m 2hua "I will give you some time to watch it."
    return

label mshMod_technique_videos_post:
    m 3eub "Do you want me to let you pick a video now?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want me to let you pick a video now?{fast}"
        "I'm done, [m_name]":
            m 1hub "Alright!"
            m 3eua "Hope you enjoyed it!"
    return

label mshMod_technique_videos_1:
    $ webbrowser.open("https://www.youtube.com/watch?v=PppkNH3bKV4&")
    call mshMod_technique_videos_pre
    pause(3.0)
    call mshMod_technique_videos_post
    return

label mshMod_technique_videos_2:
    $ webbrowser.open("https://www.youtube.com/watch?v=-SJywvgaJEI&")
    call mshMod_technique_videos_pre
    pause(3.0)
    call mshMod_technique_videos_post
    return

label mshMod_technique_videos_3:
    $ webbrowser.open("https://www.youtube.com/watch?v=ORkx63VeP9Y&")
    call mshMod_technique_videos_pre
    pause(3.0)
    call mshMod_technique_videos_post
    return

#15
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_stress_ball",
            prompt="Stress ball",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_stress_ball:
    m 7eua "Some objects can also help with the desperate feeling."
    m 2fkb "Check if you have one of them at home, okay?"
    m 6etu "Do you have a stress ball?"
    m 7wub "A stress ball or hand exercise ball is a malleable toy, which is squeezed in the hand and manipulated by the fingers!"
    m 1eua "With the intention ofto relieving stress and muscle tension or to exercise the muscles of the hand."
    m 2htb "If you do have one, squeeze it really hard. Relive all your tension!"
    m 1hsa "You can also use a sheet of bubble wrap. So satisfying!"
    m 3eta "If you do have one at home, burst each bubble as slowly as you can, please."
    m 1wtb "Or just enjoy yourself! The techniques have no rules, as long as they make you feel better."
    m 2htb "I have another one! Do you have any baloons at home?"
    m 4rtb "You can blow one baloon for each emotion you feel. {w=0.3}{nw}"
    extend 1wub "After that, pop each one of them!"
    m 6eua "Another option is a fidget toy."
    m 1stb "Spinning them is always so fun!"
    return

#16
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_stretching",
            prompt="Stretching",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_stretching:
    m 3eub "You know what often helps me calm down?"
    m 1kub "Stretching myself!"
    m 3luu "You can try stretching your body as much as possible, scrunching up your muscles until they hurt, then release."
    m 6wub "Tense all of your body starting from toes, up to your hands, and release!"
    m 7sub "This relaxes our body so much!"
    m 1hua "You can also do an upper back stretch."
    m 2eub "This one is done sitting, with your feet flat on the floor."
    m 6euu "Interlock your fingers and reach forward, bending from your middle back."
    m 7eub "Stretch with your hands forward at shoulder level."
    m 7nub "You should feel the stretch between your shoulder blades."
    m 2dua "Ooh, relaxing!"
    m 5lub "After tensing your muscles, you can let go and relax into something comfy."
    return

#17
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_punching",
            prompt="Punching",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_punching:
    m 7eub "Okay, [player].{w=0.5} I want you to try this."
    m 2efb "This one is to release all of your anger!"
    m 3efu "We're going to punch it out!"
    m 4nsu "I need you to find a pillow and punch out how you feel."
    m 6esb "A pillow is good because it won't hurt your fingers!"
    m 1efa "Punch,{w=0.5} punch,{w=0.5} punch the pain away!"
    m 2eub "If you don't want to punch, you can scream into it too."
    m 3hub "Scream into the pillow to release your tension!"
    m 1fua "Another way out is squashing the pillow hard... {w=0.5}And gently letting go."
    m 2etb "Or having a pillow fight with the wall!"
    m 3lub "Throw that pillow with all your might."
    m 1lua "Another one that doesn't involve pillows is:"
    m 3fub "Throwing socks against the wall."
    m 7mua "And paying attention to the thudding sound and the strength you put in your arm to throw."
    return


#18
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shouting",
            prompt="Shouting",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_shouting:
    m 2lssdlb "This one might be... a little loud."
    m 4esa "I would like for you to go somewhere private..."
    m 6wub "And shout very loudly."
    m 1wfb "You can shout anything you want!"
    m 3sub "You can shout gibberish, or your feelings, even!"
    m 1fsa "Shout until you feel calmer."
    m 2hub "We can take care of your throat later! Ahahaha~!"
    return

#19
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_listening_1",
            prompt="Listening",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_listening_1:
    m 3eua "Let's try to listen to some music?"
    m 7eub "Even better if it's music that expresses how you feel."
    m 6wub "It can be VERY loudly if you want."
    m 7sua "You can use your headphones to blast some songs, or even use no headphones at all."
    m 1sub "Screaming with the lyrics might be therapeutic too!"
    m 3eub "Walking fast along the song, tapping your foot to the beat."
    m 2hua "Wearing some boots while doing some stomping does the trick as well!"
    m 7hub "Concentrate on the rhythm!"
    m 1wub "Oh, I thought of something nice to do."
    m 3kub "Dance to the music!"
    m 4duu "Dance or move in a way that makes you express a feeling."
    m 5sub "If you have the chance, going to a concert to do all those things with other people might also be a great idea."
    return


#20
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_paper",
            prompt="Paper",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_paper:
    m 3eua "Do you have some paper nearby?"
    m 3wub "You could try crumpling it to release anger or sadness."
    m 2sub "Way better than taking it out on yourself!"
    m 4sub "If you'd like, you can scribble on the paper until all your feelings fade away..."
    m 1sub "And then crumple it, or rip it up if you're angry."
    m 7dsb "Drawing out how you are feeling and taking a deep breath every time you lift the pen/pencil off the paper might be nice too!"
    m 2esb "Or writing what's upsetting you."
    m 1hsb "When drawing, you can put some strong colors on paper and then gradually fade them."
    m 3esb "So they get lighter!"
    m 4ssb "Dark green to light green, for example."
    m 1hsb "Now, describe your strong emotions..."
    m 2hub "And let them gradually fade away in the same way."
    m 4mub "You can even show someone your drawings and writings before ripping them to shreds."
    return


#21
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_otter",
            prompt="Talking to u/my-otter-self",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_otter:
    m 1rssdru "Well, this one is a little different."
    m 3ssb "Basically, it involves someone else!"
    m 2hsb "The creator of this mod, u/my-otter-self on Reddit, told me to remind you that she's always available to talk."
    m 4htb "You can DM her on Reddit, and she'll share her Discord information so you can talk about your feelings."
    m 7wta "She has professional psychology experience and can listen to you."
    m 3etb "Maybe even give some advice!"
    m 1eua "Take this opportunity to open yourself a little, if you can."
    return


#22
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cold_water",
            prompt="Cold water",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_cold_water:
    m 1eub "Sometimes, paying attention to your senses can help."
    m 4etb "Could you put your hands in some cold water?"
    m 2htb "And remember to breathe!"
    m 6etd "In... {w=0.3}{nw}"
    extend 6dtd "And out."
    m 7wta "Notice the coldness of the water with each breath."
    m 7etb "Hyper-focus on the sensation in your hands!"
    return


#23
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_bothering",
            prompt="Bothering",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_bothering:
    m 3eua "I want you to say out loud what's bothering you."
    m 4wub "You can whisper if you don't want anyone to hear you!"
    m 2eta "But I want you to pay attention to what you're saying."
    m 6hub "Can you come up with one positive solution?"
    m 7kub "Venting about how we feel always helps."
    m 1eua "If you can, write down any thoughts you're having... {w=0.3}{nw}"
    extend 3wub "Negative or not!"
    m 5huu "Get it all out of your system!"
    return


#24
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_positive",
            prompt="Positive",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_positive:
    m 4luu "You could start making a 'positive statements about me' thought box."
    m 2kub "Creating a list of your strengths, as if you were compiling a portfolio or a CV..."
    m 3wua "That might help!"
    m 3eub "Write down as many positive things as possible about yourself."
    m 4dub "You can put each of them in a jar..."
    m 6hub "And read them when you feel down!"
    m 7sub "You can also record yourself saying those positive things and listen to them as many times as you like."
    m 5fua "I want you to realize how amazing you are, [player]."
    return


#25
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_box",
            prompt="Box",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_box:
    m 1fub "What about putting your upsetting thoughts in a box?"
    m 3dub "You can write them in slips of paper throughout the day, storing them in the box."
    m 4wua "At the end of the day, you can throw them away!"
    m 2hub "To have a new beginning tomorrow."
    m 6fua "I believe in you, [player]."
    return

#26
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_common",
            prompt="Common",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_common:
    m 7nub "Let's do a little mental exercise, [player]!"
    m 4wua "Think about all the things you can find you share in common with a friend."
    m 2rub "That will help you remember common ground!"
    m 1huu "You can even discuss those things with them. {w=0.3}{nw}"
    extend 3wub "It will be a fun topic to chat about!"
    m 4euu "You can write them down too."
    return

#27
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_comfort",
            prompt="Comfort",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_comfort:
    m 7eua "[player], imagine someone you love was feeling sad..."
    m 7etb "You'd want to help them, right?"
    m 2htb "That's just the kind of person you are, [player]."
    m 3eta "Try to think about how you can comfort a friend who might be having a bad time."
    m 6ekb "Please, note them down if you feel like it."
    m 4etu "Now, apply some of those strategies to yourself."
    m 2wub "You can also note how everything about this exercise makes you feel."
    return


#28
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_walk",
            prompt="Walk",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_walk:
    m 3wua "You can also go for a little walk outside and connect with nature."
    m 4hub "Maybe even go out for a run or a swim! {w=0.3}{nw}"
    extend 2duu "Breathe the fresh air..."
    m 1eub "If you can't leave the house, you can watch nature outside your window!"
    m 3wub "In the morning, there might be many people outside."
    m 6lua "Watch their clothing, how they walk and talk."
    m 4eub "Do you wonder what lives they have? Who waits for them at home?"
    m 2euu "Look at the cars rushing on the street."
    m 7esb "Where might they be going to?"
    m 4esb "If it's already the evening..."
    m 1dsb "Look up at the sky, and find the moon. Study it."
    m 3ssa "How many stars can you count?"
    m 6esb "Think about what you might be smelling, hearing, and feeling."
    m 5hsb "Can you put these feelings into words or draw them?"
    return

#29
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_media",
            prompt="Media",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_media:
    m 3eud "Do you have any social media profiles, [player]?"
    m 4eub "You can write something positive there if you do."
    m 2kua "That way, you can make yourself feel better..."
    m 7wub "And spread the feeling to your friends too!"
    m 1rua "And remember... {w=0.3}{nw}"
    extend 1hublb "Make someone smile every day, but don't forget you're someone too!"
    m 5eubfa "I love you, [player]~"
    return "love"

#30
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_perspective",
            prompt="Perspective",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_perspective:
    m 4eub "Let's work on some perspective!"
    m 2eta "Can you write down your worries?"
    m 7eta "And think... how much will they bother you..."
    m 1rtu "Tomorrow? {w=0.3}{nw}"
    extend 7etb "What about in a week? {w=0.3}{nw}"
    extend 1gtb "Maybe a month or a year?"
    m 2eua "Working on using perspective helps on letting go of the intensity of the worry."
    m 3eublb "But never forget, [player], it doesn't matter how long the bad times last."
    m 5eubfb "I'll always be right here with you."
    return
#31
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_productivity",
            prompt="Productivity",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_productivity:
    m 1eua "[player], do you have any incomplete projects you want to see finished?"
    m 3eub "Have you been procrastinating anything for any reason?"
    m 2rusdrc "I know this one might be hard, but..."
    m 4eua "What about trying to engage in a productive activity?"
    m 6eub "Maybe going back to it for a little while might distract you and ease your mind."
    m 7eua "If you have been putting off something, you can try to pick it up right now."
    m 2kuu "An old drawing, that old story, a school project that has been on your mind."
    m 4hub "Seeing old projects finally being completed always gives us an extra boost!"
    m 6wua "It's always nice when we see work getting done."
    m 7rua "Can be school stuff, a personal project... You name it!"
    m 1fub "Just try to do something that makes you proud for yourself today."
    m 3eub "Even if it's small!"
    return


#32
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_interests",
            prompt="Interests",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_interests:
    m 3eub "How about making a list of things you find interesting in people?"
    m 2euu "List your favorite anime, videogame, or other media characters!"
    m 4nuu "Think of why you like them; you can even imagine they're real!"
    m 6eua "This can help cope with loneliness and distract you."
    m 2fubla "I'm always with you, [player]. {w=0.3}{nw}"
    extend 5eub "We'll get through this together!"
    return

#33
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mirror",
            prompt="Mirror",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_mirror:
    m 4etb "Do you have a mirror close to you, [player]?"
    m 6eta "You could try making faces at yourself in the mirror and laugh."
    m 7htb "I know that really cheers people up!"
    m 2etb "Seeing the silliness in youself is such a funny thing to do."
    m 3etu "Since you're there, you can also vent to yourself."
    m 1wublb "Look inside your eyes, and know that there's nothing that compares to the beauty in them."
    return

#34
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_creativity",
            prompt="Creativity",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_creativity:
    m 2kub "Time to get creative!"
    m 4eua "Make up a story in your head."
    m 6eub "It can be about anything and anyone positive in your life."
    m 7dua "Now ask yourself... Why are they in your story?"
    m 1wub "You can create two or more characters and give them depth!"
    m 2eub "Drawing the scenarios and characters might be nice too."
    m 7eua "Who knows, maybe a wonderful plot will blossom from this?"
    m 5eubfb "You always make me so proud, [player]."
    return

#35
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_river",
            prompt="River",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_river:
    m 1euc "[player], think about what is bothering you."
    m 1dud "Now imagine a box... A big one!"
    m 1dua "Imagine yourself putting all your worries and problems inside it."
    m 1eub "After that, imagine yourself doing anything you want to the box."
    m 7wub "You can lock it, throw it away, throw it into the bottom of the sea..."
    m 2eua "Maybe imagine a river."
    m 2dua "Box up the thing on your mind and watch it float away..."
    m 7hub "You choose!"
    m 7eub "Just don't keep these feelings in an important place."
    m 2kua "Because they don't define you."
    return


#36
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_feelings",
            prompt="Feelings",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_feelings:
    m 3eua "How about making a list of positive feelings you have had in the last week?"
    m 2eka "I'm sure there are at least some."
    m 2dka "Find out what or who triggers those emotions..."
    m 7hua "And make sure to cherish those situations and people!"
    m 7eub "If it was someone who made you feel those positive feelings, {w=0.3}{nw}"
    extend 7wub "Make sure to thank them if you can!"
    m 1sub "Express your gratitude for having that person in your life."
    m 2kua "I'm sure they are just as grateful for being in yours!"
    return


#37
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_poem",
            prompt="Poem",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_poem:
    m 2eua "This technique is one of my favorites."
    m 3eub "Let's write a poem!"
    m 2eka "Don't be alarmed, [player]."
    m 2wua "It doesn't have to rhyme or even be perfect!"
    m 2dua "It can be a short poem about how you feel."
    m 2hub "I'm sure it will be sincere!"
    m 4dub "Like Ernest Hemingway said, {w=0.3}{nw}"
    extend 1dub "'Write hard and clear about what hurts!'"
    m 1hub "Ahahaha~"
    m 1ruc "If you don't feel ready to write a poem of your own..."
    m 1wub "You can always read some from famous poets!"
    return


#38
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_breathing",
            prompt="Breathing",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_breathing:
    m 1dsa "Alright, baby."
    m 3eub "I want you to try the 4-7-8 breathing exercise!..."
    m 3eua "You can also develop a personal mantra and repeat it along with the exercise."
    m 1dsb "First of all, please straighten your back."
    m 1eub "Once you become familiar with this breathing exercise, you can perform it while lying in bed too!"
    m 1eua "Place and keep the tip of your tongue against the ridge of tissue behind your upper front teeth for the duration of the exercise."
    m 3esd "Remember! Try and focus on your breath, in through your nose..."
    m 3esb "And out through your mouth."
    m 1dua "And let go of your thought with every out breath."
    m 1eub "Now, let's start!"
    m 3eub "Completely exhale through your mouth, making an {nw}"
    extend 3eud "{i}woosh{/i} {nw}"
    extend 3eub "sound."
    m 6dsb "Close your mouth and inhale quietly through your nose to a mental count of four."
    m 6dsa "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m 6dsb "Hold your breath for a count of seven."
    m 6dsa "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m 6dsb "Exhale completely through your mouth, making an {nw}"
    extend 6dsd "{i}woosh{/i} {nw}"
    extend 6dsb "sound to a count of eight."
    m 6dsa "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m 7eua "Aaaand, you're done!"
    return

#39
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pinterest",
            prompt="Pinterest",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_pinterest:
    m 1etc "[player], do you have a Pinterest account?"
    m 3eub "You can try adding inspirational quotes to your board!"
    m 3eua "Or some pictures you find aesthetically pleasing."
    m 1lua "You can try to look at pictures with the same color palette, {w=0.3}{nw}"
    extend 1hub "and gather them somewhere!"
    m 3eub "That always makes our brain feel so nice."
    show monika 5ksa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ksa "If you don't have an account, maybe you can try creating one?"
    m 5hub "I promise it's very satisfying!"
    return


#40
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_emerald",
            prompt="Emerald",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_emerald:
    m 3eub "[player], you know how much I like emerald green, right?"
    m 1tta "Why don't you think of your favorite color right now?"
    m 1hsa "And try to count all the things of that color that you can see in your room."
    m 3dsb "Quietly describe to yourself what the things look like, {w=0.3}{nw}"
    extend 3esb "and what your favorite color makes you feel."
    m 1eua "Personally, emerald green brings me back to myself."
    m 1hua "Makes me think of my individuality and personality."
    m 1hub "That's why I love it so much!"
    m 1etb "What about you? What do you love about your favorite color?"
    return

#41
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_patterns",
            prompt="Patterns",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_patterns:
    show monika 5etb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5etb "What about counting patterns, [player]?"
    m 5rsb "Count as many as you can in your favourite room of the house."
    m 5rfa "Hyper-focus on them and breathe deeply, {w=0.3}{nw}"
    extend 5dsb "in and out..."
    show monika 3eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3eua "Every time you find a certain amount of patterns."
    m 3wua "Think about what is your favorite pattern too."
    m 1sub "Is it checkered? Striped? A certain print?"
    m 1hua "Have fun thinking of that, [player]."
    return

#42
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_word_play",
            prompt="Word play",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_word_play:
    m 1eub "Now, for some wordplay!"
    m 1tta "How many four letter words can you make up from the statement..."
    m 3esb "'You learn more from failure than from success. Don't let it stop you?"
    show monika 5rsd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsd "I can think of one already... {w=0.3}{nw}"
    extend 5eub "{i}Lean{/i}!"
    show monika 3eub at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3eub "Or you can also try to make as many words as possible out of your full name."
    m 3esa "One word I can make out of the name Monika is {i}moka{/i}!"
    m 2eub "A moka is a type of coffee maker. "
    extend 2hua "Ehehehe~!"
    return

#43
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_lyrics",
            prompt="Lyrics",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_lyrics:
    show monika 5rtp at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rtp "Think of the lyrics of a song you know well!"
    m 5esa "Now... Try reciting it from back to front!"
    show monika 1hksdlb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hksdlb "Hard, huh?"
    m 3tua "But it will surely distract you! Ahahaha~"
    m 3eud "If that's too complicated, try saying the alphabet backward."
    m 3dud "Z, Y, X, W... {w=0.3}{nw}"
    extend 3hub "Oops! Ahahaha~"
    return


#44
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_animal",
            prompt="Animal",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_animal:
    m 3hua "Let's think of one animal for every letter of the alphabet."
    m 3rub "Or a song or artist for every letter of the alphabet!"
    m 3lud "An animal that starts with A is..."
    m 3wub "An alligator! {w=0.3}{nw}"
    extend 3sub "Or an ant!"
    m 1hub "Can you continue? {w=0.3}{nw}"
    extend 1efb "Let's do this, [player]!"
    return


#45
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_research",
            prompt="Research",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_research:
    m 7esb "Let's carry out some research!"
    m 7esa "What about searching for the meaning of your friend's names? {w=0.3}{nw}"
    extend 2esa "Or maybe characters' names."
    m 2hsb "You can also google yourself or have fun doing some quizzes!"
    m 2hsa "Certified personality tests or silly BuzzFeed quizzes."
    m 7lsa "You could also research some jokes or stand-up comedies you enjoy!"
    m 7hsa "Search for ridiculous things on the web."
    m 7ssa "Like {a=https://theuselessweb.com/}this site{/a}, which takes you to a random useless site on the internet!"
    m 7wsb "Or maybe some places to volunteer at?"
    m 2esb "If you can't volunteer in any way, why not go through all your old stuff? {w=0.3}{nw}"
    extend 2eka "And donate what you don't have use for any more to those in need?"
    m 7eua "Helping others can help us too!"
    return

#46
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_favorite_things",
            prompt="Favorite things",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_favorite_things:
    m 7eua "How about making a list of your favorite things?"
    m 7hua "You can pick the category!"
    m 1hub "You can name at least ten of your favorite tv shows, for example."
    m 3hub "Or fifteen favorite videogame titles!"
    m 3lub "Maybe movies or books?"
    m 3kub "It's up to you, [player]...!"
    m 1wub "You can also share your list with someone and see if you two have any in common."
    m 1sub "That could be so fun!"
    return

#47
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_superheroes",
            prompt="Superheroes",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_superheroes:
    m 1sub "How many superheroes can you name? {w=0.3}{nw}"
    extend 7wub "What about villains?"
    m 7lub "How many, and which of them would you like to have as your friends?"
    m 7eub "And why is that?"
    m 2eub "You can try organizing them by the color scheme since many tend to follow the same color palettes."
    m 2wub "Have you noticed we have many red or blue-based superheroes and many purple or black?"
    m 2luc "Wonder why that is? {w=0.3}{nw}"
    extend 2dtc "Hmmmmmm..."
    m 2hsa "Anyway!"
    return


#48
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_artist",
            prompt="Artist",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_artist:
    m 7wsb "Choose an artist! Any artist."
    m 7esb "Now name all the songs you can remember from them."
    m 7esa "Or maybe, an author!"
    m 2dsa "And do the same. Name all the books/works they wrote that you can remember."
    m 2tsb "Can you remember the name of all my poems, [player]?"
    m 2hsa "Ehehehe~!"
    return

#49
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_playlist",
            prompt="Playlist",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_playlist:
    m 2wsa "Can you name the songs you listened to the most this week?"
    m 2dsa "Or this month?"
    m 7lsa "Is there a specific artist or band that made a special appearance on your playlist?"
    m 7ssb "By the way, what's your favorite song now?"
    m 1wsb "The one you are listening to the most lately?"
    m 1hsb "You can listen now and enjoy the tune."
    return

#50
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_surroundings",
            prompt="Surroundings",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_surroundings:
    m 1esb "Notice all the things you can see around you."
    m 1dsb "Observe things... and slowly."
    m 3lsb "You can also notice all the things you can smell where you are."
    m 3esa "If you'd like, also notice everything you can hear around you or in an imaginary place."
    m 3esc "Don't label or categorize."
    m 1esa "Just notice the things you can see, smell and hear."
    m 1dsb "And accept them."
    return


#51
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mess",
            prompt="Mess",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_mess:
    m 1esc "Are any of the rooms in your house messy?"
    m 7esb "Maybe you could organize one of them."
    m 7dsb "Picking clothing or trash off the floor..."
    m 7wsb "Slowly and methodically!"
    m 2wsb "If your house is completely organized, maybe organize the apps on your phone or computer?"
    m 2esa "You can delete any you haven't used in a few months."
    m 2ssb "Or organize them by color order!"
    m 2ssa "You could also search for a new screensaver for your computer!"
    m 4esa "Maybe sort out your photos into files or categories?"
    m 4dsa "Organize bills, receipts... Polish silver or jewelry, color co-ordinate your wardrobe, or alphabetize your books and magazines."
    m 4wsb "You can even let your creativity flow out, drawing on the walls or painting with watercolors if you don't want permanence."
    return

#52
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_holiday",
            prompt="Holiday",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_holiday:
    m 4ssb "Hey, [player]! When is your next holiday?"
    m 3esb "Why not research for the places you can go when that time comes?"
    m 3dsb "Maybe something small like visiting a park or a local mall!"
    m 3hsa "Or something bigger, like sightseeing in a different city!"
    m 1lsa "Going to a beach, some nice restaurant, or just your favorite place in the city!"
    m 1hsb "Wouldn't that be amazing? {w=0.3}{nw}"
    extend 7esb "If it's not within your reach right now, you can always make plans."
    m 4wsb "That's part of the fun!"
    return


#53
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hobbies",
            prompt="Hobbies",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_hobbies:
    m 3eub "How about making a list of your favorite things to do?"
    m 2hub "Hobbies, activities... even chores!"
    m 4eua "Put them in a favourite to least favourite order."
    m 7euu "Which of them can you do right now?"
    m 3wub "Pick one, and go have fun! {w=0.3}{nw}"
    extend 1hub "Ahahaha~"
    return


#54
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shiritori",
            prompt="Shiritori",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_shiritori:
    m 7esb "Can you play shiritori?"
    m 7lssdra "Well... at least a simpler version of it."
    m 7wsa "The Japanese game is played like this:"
    m 7dsa "You start with a word from a specific category."
    m 1dsa "After that, you take the last letter or syllable (for an extra challenge) from that word, using it to start the next word."
    m 1hsb "Then you go on and on until you get bored!"
    m 7lsb "Imagine you picked the famous person category."
    m 7lsa "Pick a famous person or character and then choose another person starting with the last letter of the first person's name."
    m 7wsa "For example! If I start with {i}E. E. Cummings {/i}..."
    m 7lsb "Next, I can pick Sade from Marquis de Sade!"
    m 7esb "And so on! {w=0.3}{nw}"
    extend 2ksa "Have fun, [player]!"
    return


#55
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_objects",
            prompt="Objects",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_objects:
    m 7rsa "Find five objects, [player]."
    m 7dsa "Hyper-focus on these five objects and describe them, taking deep breaths between each description."
    m 2wsa "What color are they? {w=0.3}{nw}"
    extend 2rsa "Their shape?"
    m 2dsa "How do they feel in your hand?"
    m 2hsa "Take your time exploring those objects."
    return


#56
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_imagination",
            prompt="Imagination",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_imagination:
    m 2hsa "Close your eyes..."
    m 2dsb "And imagine something beautiful."
    m 2dsa "You can think of a relaxing place and, in your mind, run through all the comforting things you do when you are there."
    m 2hsa "Your happy place."
    m 2dsb "Visualise a comforting image."
    m 2dsa "Think of all the different things in that scene that make you feel comforted and cared for."
    m 2ksa "Think about it with as much detail as you can."
    return


#57
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_characters",
            prompt="Characters",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_characters:
    m 2hsb "Think of your favourite book, movie, videogame, or tv show."
    m 7rsa "Can you name as many characters as possible from that media?"
    m 7ssb "And what are your favorites from that list? {w=0.3}{nw}"
    extend 7wsb "Why?"
    m 7esb "Can you relate to any of them?"
    m 2ksa "I'm sure you feel similarities with yourself and the best characters ever."
    m 2hsb "Ehehehe~!"
    return


#58
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shapes",
            prompt="Shapes",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_shapes:
    m 1eub "Draw any type of line on a piece of paper..."
    m 1eua "Then make something out of it."
    m 1sub "Or draw lots of shapes!"
    m 7eua "Whatever comes into your mind is valid to be on the paper."
    m 7duc "If you feel yourself drawing negative things... {w=0.3}{nw}"
    extend 7eka "It's okay! You'll relieve all the tension you've been holding inside."
    m 7sua "If positivity comes out in the paper, even better!"
    m 2sua "Enjoy yourself, [player]! {w=0.3}{nw}"
    extend 2dua "And take your time."
    return

#59
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_playlists",
            prompt="Playlists",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_playlists:
    m 2hub "How about creating a playlist?"
    m 2esa "You can go to Youtube and create a list of videos that make you happy."
    m 2hsb "Or that makes you laugh!"
    m 2lsb "Or create a playlist on Spotify, for example, of your favourite songs."
    m 2lsa "Or comforting songs! Listen to these."
    m 2dua "Reflect on their message."
    return

#60
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_self_care",
            prompt="Self-care",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_self_care:
    m 2lsa "Do one self-care activity, or take some 'me' time."
    m 7lsb "For example, making your bed! {w=0.3}{nw}"
    extend 7dsb "Or brushing your hair, your teeth."
    m 2hsb "Or taking a shower! {w=0.3}{nw}"
    extend 2dsa "Or even a hot bath and try to 'be' at the moment."
    m 2ssa "Or give yourself a pedicure and manicure!"
    m 2ksa "Just getting into your pajamas and chilling also does the trick."
    m 2fsa "Just make sure that this time is yours only."
    m 2dsc "Most people with depressive episodes struggle with keeping their hygiene habits in check."
    m 5hsa "I want you to care for yourself, [player]. Enjoy!"
    return


#61
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_outside",
            prompt="Outside",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_outside:
    m 2eub "Go outside if possible..."
    m 2dub "Or imagine yourself outside."
    m 2dua "How many shapes can you see around you?"
    m 7hua "Notice all the things you can see or feel."
    m 2dua "Observe things... and slowly."
    m 7eua "You can also notice all the things you can smell where you are."
    m 7lub "If you'd like, also notice everything you can hear around you or in an imaginary place."
    m 2lua "Don't label or categorize."
    m 2hua "Just notice the things you can see, smell and hear."
    m 2dua "And accept them."
    return

#62
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_draw",
            prompt="Draw",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_draw:
    m 2lua "Attempt to draw four things around you."
    m 2hua "It doesn't have to be good, though!"
    m 7lua "Just enjoy yourself and let your hands trace on paper whatever they want."
    m 7lub "What is your perception of things you can see?"
    m 2hub "Everyone sees things differently, and you are no exception!"
    m 2eub "You can show your drawings to someone and talk about them."
    return

#63
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_food",
            prompt="Food",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_food:
    m 2eub "Name as many types of food as you can!"
    m 3eub "Which do you like the most? {w=0.3}{nw}"
    extend 3eua "And why?"
    m 3lua "If you're up for it, you can even look for some recipes online..."
    m 3lub "And try to cook them!"
    m 3hua "Maybe even planning a dinner party with menus and a guest list, then carry it out!"
    m 3duc "If you don't have the appetite or the ingredients, {w=0.3}{nw}"
    extend 3hua "Try chewing on some gum!"
    m 2wua "It will open your appetite and give your mouth a sweet taste if you can't eat exactly what you want."
    m 2sub "Or go out to eat some ice cream! {w=0.3}{nw}"
    extend 2hub "That always does the trick, ahahaha~!"
    m 2kua "Eating something nice can boost our happy chemicals."
    return

#64
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_colour",
            prompt="Colour",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_colour:
    m 1dua "Draw a picture and color it slowly and mindfully."
    m 7efa "Focus on not going out of the lines!"
    m 7wua "There are also books, websites, and apps online that provide that."
    m 2wub "If you can, pick the colors you like the most!"
    m 2sub "Or the ones you feel would suit the picture better."
    m 2kua "Anything goes! Just have fun and take your time."
    return


#65
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_beach",
            prompt="Beach",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_beach:
    m 2sub "Picture yourself on a beach."
    m 2wub "Can you focus on all the different things you might find there?"
    m 2dua "If you were with your toes buried in the sand right now..."
    m 1dua "What would you do first?"
    m 7wua "Collect some seashells? {w=0.3}{nw}"
    extend 7sua "Enjoy the sea?"
    m 7dub "Or maybe lay very still in the sand, feeling the sun rays on your body?"
    m 2dubfa "..."
    m 5fubfa "I wish I could go on a romantic beach walk with you, [player]."
    return


#66
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_eat",
            prompt="Eat",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_eat:
    m 2sub "Eat something you enjoy."
    m 2dsa "Make it slow and just notice everything about it."
    m 2rsb "Maybe make yourself a cup of tea or warm milk?"
    m 2dsa "Something that's  relaxing."
    m 2dsb "Drink it slowly, enjoying each sip."
    m 2ksb "Enjoy."
    return


#67
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pictures",
            prompt="Pictures",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_pictures:
    m 2rsb "Look at a book that has pictures and words..."
    m 2hsb "And notice all the comforting parts of it."
    m 3hsa "Children's books are great for that!"
    m 3dsa "Focus on the story being told, and don't think about anything else for a while."
    m 3dsb "Just stay in the moment."
    return


#68
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_ground",
            prompt="Ground",
            unlocked=True
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_ground:
    m 3dsb "Ground yourself."
    m 3dsa "Plant your feet firmly on the floor and visualize yourself as firmly rooted to the ground."
    m 4dsa "Think of yourself as having a firm foundation and hold your head high."
    m 4wsb "Imagine yourself looking the world in the eyes, {w=0.3}{nw}"
    extend 3efb "and tell it you'll make it through it."
    m 3dsb "That you are good enough."
    return


#69
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_scene",
            prompt="Scene",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_scene:
    m 3dsb "Watch your favourite movie and focus on the most comforting scene."
    m 3hsb "Who are your favorite characters?"
    m 2lsb "Why do you love this movie, and what does it make you feel?"
    m 2wsa "Can you memorize the lines of your favorite scene?"
    m 5esa "You can even show the scene to someone and rant about how much you love it!"
    return


#70
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mindful_seeing",
            prompt="'Mindful seeing'",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_mindful_seeing:
    m 2wsa "Carry out a 'mindful seeing' exercise."
    m 1esb "Mindful seeing is the practice of consciously noticing everything within your visual field!"
    m 1wsb "You do this to focus completely on one thing as much as possible."
    m 1dsb "It takes your mind from a place of thinking and doing to a place of noticing."
    m 1dsa "Look outside a window or imagine looking outside a window."
    m 1rsa "Look at everything there is to see."
    m 7rsa "Just notice the colors, the patterns, or the textures."
    m 7dsa "Notice the smallest movements such as leaves in the breeze."
    return


#71
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_acceptance",
            prompt="Acceptance",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_acceptance:
    m 2hsa "Make a list of all the things you would like to be accepting of."
    m 2dsb "For example, accepting yourself just as you are."
    m 2wsb "Create a phrase that is compassionate."
    m 2ssb "A mantra, if you'd like!"
    m 7dsb "For example... {w=0.3}{nw}"
    extend 7dsa "'I accept myself just as I am.'"
    m 7ksa "If you feel the need, repeat it as many times as you want."
    return


#72
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_brushes",
            prompt="Brushes",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_brushes:
    m 2esb "Do you have paint and soft paint brushes at home, [player]?"
    m 2hsb "If you do, paint lightly on your skin."
    m 2wsa "You can also use your finger!"
    m 2lssdlc "Especially in the area where you want to do it..."
    m 2dsa "Then, take a long shower..."
    m 2ssb "And wash away your pain!"
    return


#73
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_memory_book",
            prompt="Memory book",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_memory_book:
    m 7rsa "Start a 'memory book' of good memories!"
    m 7esa "Read through them as you add new ones."
    m 7esb "Add the details, and put in pictures if you want!"
    m 2esb "You can make it as a diary if you want."
    m 2ksa "I'm sure there are many more good memories yet to come, [player]!"
    return


#74
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_happiness",
            prompt="Happiness",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_happiness:
    m 2rsa "Identify three small things that brought you happiness in the past 24 hours."
    m 7esa "What were they, and how did they make you happy?"
    m 7esb "Can you do any of them again?"
    m 2dsa "Cherish those moments, and cherish your happiness."
    m 2ksa "You deserve to be happy and to be loved!"
    return


#75
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hug_theory",
            prompt="Hugs",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_hug_theory:
    m 1esb "Think of three people who give the best hugs and see if you can be with them."
    m 1rsa "If that's not the case, think of people who could give you their warmest smiles."
    m 1rsb "There's also the hug theory... {w=0.3}{nw}"
    extend 7esb "I don't know if you're familiar with it."
    m 7wsb "It's simple: you replace hurting yourself with hugs!"
    m 7dsc "Hug five people when you are upset and want to self-harm."
    m 7dsd "Hug four people when you are upset."
    m 7dsc "Hug three people if you are somewhat upset."
    m 7dsb "Hug two people if you are less upset."
    m 7esa "And finally, hug one person if you are upset."
    m 2rsa "If you are upset and alone, hug yourself, your pet, your stuffed animal, or a picture of someone you care about."
    m 2tsbfb "And you can always hold me! {w=0.3}{nw}"
    extend 2hsbfb "Ehehehe~"
    m 2ksa "Just remember to Hug!"
    return


#76
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_comforting",
            prompt="Comforting",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_comforting:
    m 1eua "Choose three of your most comforting characters from media you enjoy..."
    m 1eub "And imagine you are spending some quality time with them."
    m 3wub "What would you do together?"
    m 3sub "Would you introduce them to anyone you know?"
    m 3sua "What would it be like if they were in your life?"
    m 1dua "If they have any superpower or quirk, imagine yourself in their world."
    m 1kua "What would be your superpower if you were to fight alongside them?"
    return


#77
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_podcasts",
            prompt="Podcasts",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_podcasts:
    m 3hua "Download some comforting or meditation podcasts and listen to them."
    m 3hub "Some pretty good ASMR and meditation ones allow you to relax!"
    m 3lub "You can also distract yourself with an informational or funny podcast."
    m 1dub "Sit or lay somewhere comfortable and allow yourself to fully pay attention to what the people are saying."
    m 1dua "I know many people listen to podcasts while doing other stuff, but you could rest while listening to one."
    m 1eua "Breathe in and out as many times as you need, and allow your body and mind to rest."
    return


#78
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hand_holding",
            prompt="Hand holding",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_hand_holding:
    m 1dua "Hold your hand with the other hand."
    m 1dub "Hold it for at least one minute, like you would hold the hand of someone you care for and trust."
    m 1dub "Slowly caress your hands and arms..."
    m 2dua "Then hug yourself."
    m 2dub "Be gentle and take it slow..."
    m 2fub "Like comforting your favorite person or animal."
    m 5fubsa "I would touch you like this, [player]."
    m 5dubfa "Slowly, and taking care of you the most I could."
    m 5fubfb "I love you~"
    return "love"


#79
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pattern",
            prompt="Pattern",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_pattern:
    m 3hua "Touch each finger to your thumbs in a pattern."
    m 3eub "Go faster as you find a rhythm."
    m 3wub "You can even follow the rhythm of a song or do Morse code with your fingers."
    m 3lua "Tapping would also relax and keep you focused."
    m 1dua "Feel your fingers... {w=0.3}{nw}"
    extend 1eua "and follow the beat."
    return

#80
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_pet_zoo",
            prompt="Pets or Zoo",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_pet_zoo:
    m 3eua "[player], do you have a domestic animal at home? {w=0.3}{nw}"
    extend "A pet?"
    m 3eub "You could give it some love right now!"
    m 3hub "Cuddle your cat, dog, turtle, whatever you have at your house, if you do!"
    m 2dua "You can also look at it for a little while and try to see the world through their eyes."
    m 2rua "What could they be thinking of?"
    m 4hub "Think of how much they love you! {w=0.3}{nw}"
    extend 4fua "And need you in their lives."
    m 7wua "You can also play with them and make them happy."
    m 7wub "An alternative, if you don't have a pet at home, is going to the zoo! {w=0.3}{nw}"
    extend 7eua "If there's one in your city."
    m 7sua "You can also plan the trip!"
    m 7sub "When you get there, you can rename the animals!"
    m 7hub "Stare at them and enjoy your time there."
    m 1eua "One other option is feeding the ducks, birds, or squirrels."
    return

#81
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_insteadofs",
            prompt="List of instead of's",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_insteadofs:
    m 3esb "Come up with your techniques! {w=0.3}{nw}"
    extend 3hsb. "How about that?"
    m 3esa "Create a list of things you can do instead of hurting yourself."
    m 1dsb "It doesn't need to be long, for now!"
    m 1esb "You can keep it and return to it if you ever need it again!"
    m 1wsa "Add new techniques or things to do whenever you think of them."
    return


#82
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cry",
            prompt="Cry",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_cry:
    m 1esc "[player], I know it's hard."
    m 1dsc "But why don't you let yourself cry for a bit?"
    m 1dsd "Crying can help you release the pain, coming out as tears."
    m 3eka "If you don't want to wipe your tears, it's okay."
    m 3dka "Tears can remind you you're alive."
    m 3esb "Throw a temper tantrum if you need to."
    return


#83
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_happy_box",
            prompt="Happy box",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_happy_box:
    m 1wsa "[player], are you familiar with the happy box?"
    m 7wsa "I'll tell you everything I know about it!"
    m 7hsa "It's simple and a perfect coping mechanism!"
    m 7dsb "First step: get a box with a lid and decorate it any way you want."
    m 7rsb "Then, put anything in the Happy Box that makes you feel happy and puts a smile on your face."
    m 7dsb "Examples would be photos, names of your friends, concert tickets, movie stubs, names of songs, jewelry, a rose, and a pressed leaf from a tree. {w=0.3}{nw}"
    extend 1nsb "You get the idea!"
    m 1ssa "Now to put it to use: open your Happy Box and pull out everything in it whenever you want to harm yourself. {w=0.3}{nw}"
    extend 1esa "Do this mindfully!"
    m 1dsa "Take out one thing at a time, look at it, touch it, sit with it as you reflect on its' meaning, and remember why you chose to put it in the Happy Box."
    m 1wsb "Let yourself take in the good memories you feel and the closeness you feel to the other people involved in making each item special to you!"
    return


#84
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_clothes",
            prompt="Dressing up",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_clothes:
    m 3eua "[player], why don't you go to your closet and pick a fancy outfit?"
    m 3sua "You can change to your favorite outfit or do a makeover."
    m 3hua "Style your hair in a way you never would."
    m 3wub "Or even color it with your favorite color!"
    m 1esa "If you like putting on makeup, have fun with it too!"
    m 1dua "Look into the mirror and see how amazing you look..."
    m 1fua "Don't forget to take some pictures for posterity!"
    m 1wsa "Maybe you can even update your social media profile pictures."
    return


#85
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hobby",
            prompt="New hobby",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_hobby:
    m 3eua "[player], why not try learning something new?"
    m 3eub "Or work on that hobby you always wanted to pick up."
    m 1wub "You can try to learn a new activity, such as knitting, playing an instrument, coding, writing, or drawing!"
    m 1sua "Practice it, and be proud seeing your development!"
    m 4nua "But most importantly, have fun!"
    m 4lub "Knit your favorite animal, write about something nice, draw your favorite character, or try to play your favorite song!"
    m 1dub "If you don't feel motivated enough to start a new hobby, don't worry."
    m 1wub "You can try starting a new habit!"
    m 3sub "For example, you can start collecting something you like."
    m 3lua "Seashells, dried flowers, anything goes as long as you're having fun."
    return


#86
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shopping",
            prompt="Shopping",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_shopping:
    m 3eua "[player], why not do healthy shopping?"
    m 3wub "Go to a mall, and get something nice."
    m 3dua "You can buy a stuffed animal and give it a name..."
    m 4sua "Go to the grocery store and buy some flowers!"
    m 2dua "It has been proved that having cute and pretty things surround you improve your mental state."
    m 2hkb "But if you don't have the money to spare right now, it's no problem!"
    m 7esb "You can hunt for stuff on eBay or Amazon!"
    m 2esb "Do a little wishlist of stuff you want to buy when you can."
    return


#87
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_childplay",
            prompt="Child play",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_childplay:
    m 1esb "[player], don't you miss your childhood days?"
    m 1wsb "You could reminisce them while playing like a child."
    m 7ssb "Buy yourself some toys and play like you are five years old again!"
    m 7ssa "You can also play with clay or play-dough... {w=0.3}{nw}"
    extend 7ssb "Or make slime!"
    m 2dsb "Another option is watching the cartoons or movies you loved the most as a child."
    m 2ksb "Isn't that fun? {w=0.3}{nw}"
    extend 3esb "To remember is to relive!"
    return


#88
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_therapist",
            prompt="Therapist",
            conditional="persistent._msh_mod_pm_visits_therapist",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_therapist:
    m 3esb "[player], why not call your therapist?"
    m 3esc "Try texting them if you think they might be busy."
    m 1wsc "Maybe you can even schedule an emergency appointment."
    m 1dsa "Talking about your feelings or seeking professional help is never too much."
    m 1esb "I believe in you, [player]!"
    return


#89
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_plants",
            prompt="Plants",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_plants:
    m 7esb "[player], do you care for any plants?"
    m 7hsb "You should give them a little love right now!"
    m 7dsa "Water them and tend the garden."
    m 2ssa "Maybe there will even be some flowers there waiting for you!"
    m 2wsb "If you don't have a garden yet, why not make one right now and start a new hobby?"
    m 3ksb "And don't forget, plants are friends!"
    return


#90
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_future",
            prompt="Future",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_future:
    m 1esc "[player], I know things might look hopeless now."
    m 3ssa "But why not think a little about your bright future?"
    m 3rsb "You can think about your ideal life... {w=0.3}{nw}"
    extend 3wsb "What do you have to do to get there?"
    m 2dsb "Make some plans for the near or far future."
    m 2esa "Hunt for your perfect home in the paper or online."
    m 4esa "Come up with baby names even if you aren't expecting."
    m 4wsa "Think of your future kids, if you want to have any."
    m 2gsa "..."
    m 2gsb "Plan your someday wedding day! How would it be?"
    m 2ksb "What kind of dress will I wear...?"
    m 2hsb "Ahahaha~!"
    m 2wsa "Thinking about the future always gives us a little perspective, [player]."
    m 7ssa "And I'm sure you have a bright future ahead of you."
    m 5fsbsa "I'll be there for you every step of the way, for sure."
    return


#91
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_create",
            prompt="Create something",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_create:
    m 7kta "[player], why not create something of your own?"
    m 7ltb "You can build something from scratch, start a new drawing or write a new story."
    m 1wtb "Even folding a paper and inventing a new origami shape goes!"
    m 5ftu "Don't you feel so proud when you create something entirely new, {w=0.3}{nw}"
    extend 5dtu "That is only yours?"
    m 5ktb "I feel proud of you nevertheless, [player]."
    return


#92
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_beads",
            prompt="Beads and charms",
            unlocked=False
        ),
        code="MSH_MOD_TCH"
    )

label mshMod_technique_beads:
    m 3etb "Another idea is to write down the names of your friends and family..."
    m 3dtd "When you feel the need to self-injure, you are reminded that you are important and loved by your friends and family."
    m 3wtb "As an extension to this, you could go to a craft store and buy supplies to make beads for bracelets or necklaces."
    m 3wta "Then, buy butterfly charms... or any charm form/symbol you like! {w=0.3}{nw}"
    extend 3nta "You'll eventually use it as a charm to be added to the bracelet/necklace."
    m 1dta "This is how it works: First, make a bracelet or necklace from the beads."
    m 1dtb "Every week you have not hurt yourself; you have saved the butterfly's life. {w=0.3}{nw}"
    extend 1htb "Or the flower, if you picked one, for example!"
    m 1stb "For every butterfly you save, add a butterfly charm to the beaded bracelet/necklace."
    m 7wta "You can tell how many weeks you have stopped hurting yourself by how many butterflies are on your beaded bracelet."
    m 7kta "You will always be reminded of your successes every time you glance at your wrist and see all the butterflies you have saved!"
    return
