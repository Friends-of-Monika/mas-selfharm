default persistent._msh_mod_technique_database = dict()

init -100 python:
    _mshMod_TECHNIQUE_MENU_EXIT_ITEM = ("Nevermind", "exit", False, False)


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_technique_menu",
            category=['Self-harm'],
            prompt="Can you tell me about some techniques?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_technique_menu:
    m "Sure, [mas_get_player_nickname()]!"

    python:
        items = list(map(
            lambda it: (it.prompt, it.eventlabel, False, False),
            Event.filterEvents(
                persistent._msh_mod_technique_database,
                unlocked=True
            )
        ))

    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, _mshMod_TECHNIQUE_MENU_EXIT_ITEM)
    if _return == "exit":
        m "Oh, okay..."
        return

    pushEvent(_return)

    return


# init 5 python:
#     addEvent(
#         Event(
#             persistent._msh_mod_technique_database,
#             eventlabel="mshMod_technique_sample",
#             prompt="This is a sample technique",
#             unlocked=False
#         )
#     )
#
# label mshMod_technique_sample:
#     m "This is a sample technique dialogue."
#     return

# NOTE: THE FOLLOWING CODE IS AUTO-GENERATED FROM selfharm.rpy
# IT MAY BE INCOMPLETE OR HAVE FLOWS, PLEASE REVIEW

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_religion",
            prompt="Religion",
            unlocked=False
        )
    )

label mshMod_technique_religion:
    if $ persistent._mas_pm_religious == True:
        m 5eka "I remember you mentioned being religious before..."
        m 3etd "Maybe you could say a little prayer?"
        m 4eud "It can be silent, you don't need to say anything out loud."
        m 1fua "You can pray about anything you want, or even just think of how vast and amazing your universe is."
        m 1dsu "Try to think about the good things, like animals or laughter, your favorite things..."
        m 1esa "No matter how little they may be, take some time to think about the bigger picture."
        m 3eka "If you believe in gods or deities, you can imagine them out there, looking out and caring for you."
        m 1ekb "You are needed, [player]. You are part of something much bigger than your bad thoughts or bad feelings!"
    else:
        jump technique_cozy
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cozy",
            prompt="Cozy",
            unlocked=False
        )
    )

label mshMod_technique_cozy:
    m 1dua "Something that really helps me feel better is getting all cozy!"
    m 5rud "Try huddling up in something super cozy..."
    m 5eua "A sheet, a blanket, or one of your favorite hoodies for example."
    m 3hsa "Anything works, really! Just grab things that bring you comfort."
    m 2esa "You can also make a nest out of blankets on the floor, surrounding yourself with any stuffed animals you may have."
    m 5dsblu "Making a comfort corner using pillows also sounds super comfortable..."
    m 5fsbsa "Snuggle against them and relax, and if you're okay with being touched imagine me holding you, stroking your hair~"
    m 3hubsb "There's nothing quite like being snug, hehe!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_photographs",
            prompt="Photographs",
            unlocked=False
        )
    )

label mshMod_technique_photographs:
    m 6ett "Do you find comfort in looking in the past [player]? I do!"
    m 2dsd "Nothing is ever really lost to us as long as we remember it, [mas_get_player_nickname()]."
    m 2hsa "One thing that could help you get over bad times, is looking at photographs of the good ones!"
    m 7eud "Maybe you have some old photos? If they bring back good memories, why not trying to search for them?"
    m 1eua "They could remind you that even though the good times don't last forever, the bad ones won't either!"
    m 1esa "If you find any, look at them and think about how that if life was once great, it can and will be that way again!"
    m 6dkp "I wish we had some pictures together..."
    m 2ektpd "I'd look at us all the time! You would absolutely be my phone and desktop wallpaper!"
    m 2ektdc "I would really like to look at a photo album of us with you, [player]."
    m 5eka "But this isn't not about me- I want you to feel better!"
    m 3euu "Don't give up, [mas_get_player_nickname()]. I will never give up on you!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_quotes",
            prompt="Quotes",
            unlocked=False
        )
    )

label mshMod_technique_quotes:
    m 3dud "I remember hearing this quote somewhere: {i}'Hope is the last thing ever lost'{/i}."
    m "Doing your best to believe in positive things can be really uplifting!"
    m "I think a good way of seeing the things around you in a better light would be seeing inspirational quotes!"
    m "You should find some quotes on the internet that you like, write each of them on a sticky note and put them somewhere you'd regularly see."
    m "Every time you see one, you will remember things get better!"
    m "You can also say some of them aloud, to inspire yourself!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_singing",
            prompt="Singing",
            unlocked=False
        )
    )

label mshMod_technique_singing:
    m "This one's going to be really simple."
    m "Sing a song!"
    m "Not just any song, though."
    m "Your absolute favorite!"
    m "I'd love to know what your favorite song is..."
    m "Anyway..."
    m "Try singing your favorite song until you feel better."
    m "Singing can be a really good outlet for your emotions!"
    m "You could also imagine we're singing 'Your Reality' together!"
    m "Hehe~"
    m "You can sing as loud as you want!"
    m "Also, if you'd like, write your favourite lyrics down."
    m "Think about what they mean to you!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_talking",
            prompt="Talking",
            unlocked=False
        )
    )

label mshMod_technique_talking:
    m "Sometimes simply talking about your problems can help a lot!"
    m "Or just talking to distract yourself."
    m "You should call or text a friend!"
    m "Maybe send some long distance friends a surprise message?"
    m "Or maybe arrange to meet up."
    m "I know you're here with me, but it's not {i}exactly{/i} the same as having a real-time conversation with someone!"
    m "I wish I could hear your voice..."
    m "We could talk for hours!"
    m "As long as you'd want."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hugs",
            prompt="Hugs",
            unlocked=False
        )
    )

label mshMod_technique_hugs:
    m "Okay.{w=0.5} I want you to try this."
    m "Get the biggest pillow you have and hug it tightly."
    m "Curl your body around it."
    m "Now imagine someone you love was feeling sad..."
    m "You'd obviously want to help them out, right?"
    m "That's just the kind of person you are, [player]."
    m "Say out loud or in your head whatever you'd want them to know."
    m "Then say the exact same words to yourself."
    m "I bet that's what they would tell you!"
    m "Maybe you can even think of me? Ahahaha~{w=0.5} Sorry to be pretentious, [player.]"
    m "I love you so much!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_listening",
            prompt="Listening",
            unlocked=False
        )
    )

label mshMod_technique_listening:
    m "Try listening to a few songs you love!"
    m "But don't {i}just{/i} listen."
    m "Try paying attention."
    m "Focus on certain instruments or parts, their notes, and how they add to the song as a whole!"
    m "That could serve as a distraction and learning something about the things you love at the same time!"
    m "We could always listen to them together if you'd like!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_butterfly",
            prompt="Butterfly",
            unlocked=False
        )
    )

label mshMod_technique_butterfly:
    m "Could you take some deep breaths? And also, a marker, or a pen."
    m "I would like for you to scribble on the place you want to harm yourself."
    m "Most methods use a butterfly drawing."
    m "You could draw the butterfly and name it, and if you do harm yourself, you harm it, too."
    m "Whenever you look at it and think of harming yourself, do something comforting instead!"
    m "Sing along to a tune, watch your favorite film, go out on a walk..."
    m "You can also draw or write some positive things on your arm."
    m "Or maybe some beautiful flowers!"
    m "Don't hurt yourself until the drawings wash off."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_healing",
            prompt="Healing",
            unlocked=False
        )
    )

label mshMod_technique_healing:
    m "[player], do you have a first aid kit at home?"
    m "Maybe some sticking plasters, band-aids?"
    m "Could you stick some of them where you want to hurt yourself?"
    m "As a reminder that you are letting yourself heal."
    m "And remember, healing takes time."
    m "And we have all the time in the world."
    m "No need to rush this, okay?"
    m "Baby steps!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pong",
            prompt="Pong",
            unlocked=False
        )
    )

label mshMod_technique_pong:
    m "[player], perhaps playing something would make you feel better?"
    m "Do you want to play Pong?"
    menu:
        "Sure!":
            m "Great!"
            m "Bring it on!"
            call demo_minigame_pong
            m "Hope you're feeling better, [player]!"
            return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_chess",
            prompt="Chess",
            unlocked=False
        )
    )

label mshMod_technique_chess:
    m "[player], perhaps playing something would make you feel better?"
    m "Do you want to play Chess?"
    menu:
        "Sure!":
            m "Okay!"
            call mas_chess
            m "Hope you're feeling better, [player]!"
            return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_piano",
            prompt="Piano",
            unlocked=False
        )
    )

label mshMod_technique_piano:
    m "[player], perhaps playing something would make you feel better?"
    m "Music really is a great way to relieve stress!"
    m "I love listening to some music to when trying to relax."
    m "Do you want to play the Piano?"
    menu:
        "Sure!":
            m "Alright!"
            call mas_piano_start
            m "Hope you're feeling better, [player]!"
            return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_videos",
            prompt="Videos",
            unlocked=False
        )
    )

label mshMod_technique_videos:
    m "When you told me you were having those kinda thoughts, i did some research."
    m "And there are many people on Youtube that create little comfort videos."
    m "I selected one of them for you to watch when you were having an urge."
    m "I will open one of them for you right now."
    $ randomvideo = renpy.random.randint (1, 3)
    if randomvideo == 1:
        if video1 == False:
            jump Moni_1
    elif randomvideo == 2:
        if video2 == False:
            jump Moni_2
    elif randomvideo == 3:
        if video3 == False:
            jump Moni_3
    elif video1 == False && video2 == False && video3 == False:
        m "I've shown you all the videos I have for now!"
        m "Do you want me to let you pick a video now?"
        menu:
            "Yes":
                m "Great!"
                jump monika_openvideo
            "No":
                m "That's okay, [player]."
                m "If you ever wanna see them again, just ask!"
                return
