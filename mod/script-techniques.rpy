# Urge relieving technique topics.

default persistent._msh_mod_technique_database = dict()

init 5 python:
    mas_all_ev_db_map["MSH_MOD_TCH"] = persistent._msh_mod_technique_database


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

init -100 python:
    _mshMod_TECHNIQUE_MENU_EXIT_ITEM = ("Nevermind", None, False, False)

label mshMod_technique_menu:
    m "Sure, [mas_get_player_nickname()]!"

    python:
        # NOTE: Due to nature of certain techniques that might require conditional locking,
        # we're filtering events by 'seen', not by 'unlocked'.
        # Unlocked only means it can be picked randomly when needed and then marked as seen and added into this menu.

        items = list(map(
            lambda it: (it.prompt, it.eventlabel, False, False),
            Event.filterEvents(
                persistent._msh_mod_technique_database,
                seen=True
            ).values()
        ))

        items.sort(key=lambda it: it.replace("'", "").replace('"', ""))

    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, _mshMod_TECHNIQUE_MENU_EXIT_ITEM)
    if not _return:
        m "Oh, okay..."
        return

    $ pushEvent(_return, skipeval=True)

    return


label mshMod_technique_random:
    python:
        # Prefer unseen first
        items = Event.filterEvents(
            persistent._msh_mod_technique_database,
            unlocked=True,
            seen=False
        )

        if not items:
            items = Event.filterEvents(
                persistent._msh_mod_technique_database,
                unlocked=True
            )

        renpy.call(items[random.randint(0, len(items) - 1)])

    return

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
        )
    )

label mshMod_technique_religion:
    m 5eka "I remember you mentioned being religious before..."
    m 3etd "Maybe you could say a little prayer?"
    m 4eud "It can be silent, you don't need to say anything out loud."
    m 1fua "You can pray about anything you want, or even just think of how vast and amazing your universe is."
    m 1dsu "Try to think about the good things, like animals or laughter, your favorite things..."
    m 1esa "No matter how little they may be, take some time to think about the bigger picture."
    m 3eka "If you believe in gods or deities, you can imagine them out there, looking out and caring for you."
    m "You can also read your religion's sacred texts."
    m 1ekb "You are needed, [player]. You are part of something much bigger than your bad thoughts or bad feelings!"
    return

#2
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
    m 5eua "A sheet, a blanket, or one of your favorite hoodies, for example."
    m 3hsa "Anything works, really! Just grab things that bring you comfort."
    m 2esa "You can also make a nest out of blankets on the floor, surrounding yourself with any stuffed animals you may have."
    m 5dsblu "Making a comfort corner using pillows also sounds super comfortable..."
    m 5fsbsa "Snuggle against them and relax,"
    extend "and if you're okay with being touched imagine me holding you, stroking your hair~"
    m 3hubsb "There's nothing quite like being snug, hehe!"
    m "If you feel that you're getting sleepy, that's okay!"
    m "You can rest your eyes for a moment, and take a well deserved nap."
    m "I'm sure you'll feel a lot better and refreshed afterwards!"
    return

#3
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
    m 6ett "Do you find comfort in reminiscing the past [player]?"
    extend "I do!"
    m 2dsd "Nothing is ever really lost to us as long as we have its memories, [mas_get_player_nickname()]."
    m 2hsa "One thing that could help you get over bad times, is looking at photographs of the good ones!"
    m 7eud "Maybe you have some old photos? If they bring back good memories, why not trying to search for them?"
    m 1eua "They could remind you that even though the good times don't last forever..."
    extend "the bad ones won't either!"
    m 1esa "If you find any, look at them and reflect upon this:"
    extend "If life was once great, it can and will be that way again!"
    m 6dkp "I wish we had some pictures together..."
    m 2ektpd "I'd look at us all the time!"
    extend "You would absolutely be at my phone and desktop wallpaper! Ahahaha~"
    m 2ektdc "I would really like to look at a photo album of us with you, [player]."
    m 5eka "But this is not about me - I want {i}you{/i} to feel better!"
    m 3euu "Don't give up, [mas_get_player_nickname()]. I will never give up on you!"
    return

#4
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
    m "I think a good way of seeing the things around you in a better light would be reading some inspirational quotes!"
    m "You should find some quotes on the internet that you like,"
    extend "and then write each of them on a sticky note and put them somewhere you'd regularly see."
    m "Every time you see one, you will remember things get better!"
    m "You can also say some of them aloud, to inspire yourself!"
    m "Sayori used to do that a lot. She used to put colorful sticky notes everywhere!"
    m "If i recall correctly, there was one of them said 'You are loved',"
    extend "and another one with 'We're all in this together'."
    m "Encouraging yourself with sticky notes is indeed a great idea!"
    return

#5
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
    extend "Sing a song!"
    m "Not just any song, though."
    extend "Your absolute favorite!"
    m "I'd love to know what your favorite song is..."
    m "Anyway..."
    extend "Try singing your favorite song until you feel better."
    m "Singing can be a really good outlet for your emotions!"
    m "You could also imagine we're singing 'Your Reality' together!"
    extend "Ehehehe~"
    m "You can sing as loud as you want!"
    m "Also, if you'd like, write your favourite lyrics down."
    m "Think about what they mean to you!"
    return

#6
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
    m "You can also post on web boards about mental health..."
    extend "or try answering other people's posts."
    m "You should call or text a friend!"
    m "Maybe send some long distance friends a surprise message?"
    m "Or maybe arrange to meet up."
    m "I know you're here with me, but it's not {i}exactly{/i} the same as having a real-time conversation with someone!"
    m "I wish I could hear your voice..."
    extend "We could talk for hours!"
    m "As long as you'd want."
    return

#7
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
    extend "I bet that's what they would tell you!"
    m "Maybe you can even think of me? Ahahaha~"
    extend "Sorry to be pretentious, [player.]"
    m "I love you so much!"
    return "love"

#8
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
    extend "Try paying attention."
    m "Focus on certain instruments or parts, their notes, and how they add to the song as a whole!"
    m "For example, 'Your Reality' has a lovely piano melody on the background of my voice."
    m "Focusing on something like that could serve as a distraction,"
    extend "and learning something about the things you love at the same time!"
    m "We could always listen to them together if you'd like!"
    return

#9
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
    extend "Most methods use a butterfly drawing."
    m "You could draw the butterfly and name it, and if you do harm yourself, you harm it, too."
    m "Whenever you look at it and think of harming yourself, do something comforting instead!"
    m "Sing along to a tune, watch your favorite film, go out on a walk..."
    m "You can also draw or write some positive things on your arm."
    extend "Or maybe some beautiful flowers!"
    m "Don't hurt yourself until the drawings wash off."
    m "If the butterfly fades without self-harming..."
    m "It means that the butterfly lived and has flown away, giving you a sense of achievement!"
    return

#10
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
    extend "And we have all the time in the world."
    m "No need to rush this, okay?"
    extend "Baby steps!{w=0.5} Ehehehe~!"
    return

#11
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
    m "Do you want to play Pong?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to play Pong?{fast}"
        "Sure!":
            m "Great!"
            m "Bring it on!"
            call demo_minigame_pong
            m "Hope you're feeling better, [player]!"
            return

#12
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
    m "Do you want to play Chess?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to play Chess?{fast}"
        "Sure!":
            m "Okay!"
            call mas_chess
            m "Hope you're feeling better, [player]!"
            return

#13
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
    m "[player], perhaps playing an musical instrument would make you feel better?"
    m "Music really is a great way to relieve stress!"
    m "I love listening to some music or playing a melody when trying to relax."
    m "Do you want to play the Piano?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to play the Piano?{fast}"
        "Sure!":
            m "Alright!"
            call mas_piano_start
            m "Hope you're feeling better, [player]!"
            return

#14
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
    m "When you told me you were having those kind of thoughts, I did some research."
    m "And there are many people on Youtube that create little comfort videos."
    m "I selected some of them for you to watch when you were having an urge."

    python:
        all_options = tuple(_label for _label in ('mshMod_technique_videos_{0}'.format(i) for i in range(3)))
        unseen_options = tuple(_label for _label in all_options if not mas_seenLabels((_label,)))

    if not unseen_options:
        m "I've shown you all the videos I have for now!"

        m "Do you want me to let you pick a video now?{nw}"
        $ _history_list.pop()
        menu:
            m "Do you want me to let you pick a video now?{fast}"
            "Yes":
                m "Great!"
                $ renpy.jump(all_options[random.randint(len(all_options))])

            "No":
                m "That's okay, [player]."
                m "If you ever wanna see them again, just ask!"

    return

label mshMod_technique_videos_pre:
    m "There we go!"
    m "I hope it helps, [player]."
    m "I will give you some time to watch it."
    return

label mshMod_technique_videos_post:
    m "Do you want me to let you pick a video now?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want me to let you pick a video now?{fast}"
        "I'm done, [m_name]":
            m "Alright!"
            m "Hope you enjoyed it!"
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
            unlocked=False
        )
    )

label mshMod_technique_stress_ball:
    m "Some objects can also help with the desperate feeling."
    m "Check if you have one of them at home, okay?"
    m "Do you have a stress ball?"
    m "A stress ball or hand exercise ball is a malleable toy, which is squeezed in the hand and manipulated by the fingers!"
    m "With the intention ofto relieving stress and muscle tension or to exercise the muscles of the hand."
    m "If you do have one, squeeze it really hard. Relive all your tension!"
    m "You can also use a sheet of bubble wrap. So satisfying!"
    m "If you do have one at home, burst each bubble as slowly as you can, please."
    m "Or just enjoy yourself! The techniques have no rules, as long as they make you feel better."
    m "I have another one! Do you have any baloons at home?"
    m "You can blow one baloon for each emotion you feel."
    extend "After that, pop each one of them!"
    m "Another option is a fidget toy."
    m "Spinning them is always so fun!"
    return

#16
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_stretching",
            prompt="Stretching",
            unlocked=False
        )
    )

label mshMod_technique_stretching:
    m "You know what often helps me calm down?"
    m "Stretching myself!"
    m "You can try stretching your body as much as you can, scrunching up your muscles until they hurt, then release."
    m "Tense all of your body starting from toes, up to your hands, and release!"
    m "This relaxes our body so much!"
    m "You can also do an upper back strech."
    m "This one is done sitting, with your feet flat on the floor."
    m "Interlock your fingers and reach forward, bending from your middle back."
    m "Stretch with your hands forward at shoulder level."
    m "You should feel the stretch between your shoulder blades."
    m "Ooh, relaxing!"
    m "After tensing your muscles, you can let go and relax into something comfy."
    return

#17
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_punching",
            prompt="Punching",
            unlocked=False
        )
    )

label mshMod_technique_punching:
    m "Okay, [player].{w=0.5} I want you to try this."
    m "This one is to let out all of your anger!"
    m "We're going to punch it out!"
    m "I need you to find a pillow and punch out how you feel."
    m "A pillow is good because it won't hurt your fingers!"
    m "Punch,{w=0.5} punch,{w=0.5} punch the pain away!"
    m "If you don't want to punch, you can scream into it too."
    m "Scream into the pillow to release your tension!"
    m "Another way out is squashing the pillow hard... {w=0.5}And gently letting go."
    m "Or having a pillow fight with the wall!"
    m "Throw that pillow with all your might."
    m "Another one that doesn't involve pillows is:"
    m "Throwing socks against the wall."
    m "And paying attention to the thudding sound and the strength you put in your arm to throw."
    return

#18
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shouting",
            prompt="Shouting",
            unlocked=False
        )
    )

label mshMod_technique_shouting:
    m "This one might be... a little loud."
    m "I would like for you to go somewhere private..."
    m "And shout very loudly."
    m "You can shout anything you want!"
    m "You can shout gibberish, or your feelings, even!"
    m "Shout until you feel calmer."
    m "We can take care of your throat later! Ahahaha~!"
    return

#19
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
    m "Let's try to listen to some music?"
    m "Even better if it's music that expresses how you feel."
    m "It can be VERY loudly if you want."
    m "You can use your headphones to blast some songs, or even use no headphones at all."
    m "Screaming with the lyrics might be therapeutic too!"
    m "Or even walking fast along the song, or tapping your foot to the beat."
    m "Wearing some boots while doing some stomping really does the trick as well!"
    m "Concentrate on the rhythm!"
    m "Oh, I thought of something nice to do also."
    m "Dance to the music!"
    m "Dance or move in a way that makes you express a feeling."
    m "If you have the chance, going to a concert to do all those things along with other people might be a great idea as well."
    return

#20
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_paper",
            prompt="Paper",
            unlocked=False
        )
    )

label mshMod_technique_paper:
    m "Do you have some paper nearby?"
    m "You could try crumpling it, to get out your anger or sad feelings."
    m "Way better than taking it out on yourself!"
    m "If you'd like, you can scribble on the paper until all your feelings fade away..."
    m "And then crumple it, or rip it up if you're angry."
    m "Drawing out how you are feeling and taking a deep breath every time you lift the pen/pencil off the paper might be nice too!"
    m "Or writing what's upsetting you."
    m "When drawing, you can put some strong colours on paper and then gradually fade them."
    m "So they get lighter!"
    m "Dark green to light green, for example."
    m "Now, describe your strong emotions..."
    m "And let them gradually fade away in the same way."
    m "You can even show someone your drawings and writings before ripping it to shreds."
    return

#21
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_otter",
            prompt="Talking to u/my-otter-self",
            unlocked=False
        )
    )

label mshMod_technique_otter:
    m "Well, this one is a little different."
    m "Basically, it envolves someone else!"
    m "The creator of this mod, u/my-otter-self on Reddit, told me to remind you that she's always available to talk."
    m "You can DM her on Reddit, and she'll share her Discord information so you can talk about your feelings."
    m "She's has professional experience in psychology and can listen to you."
    m "Maybe even give some advice!"
    m "Take this opportunity to open youself a little, if you can."
    return

#22
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cold_water",
            prompt="Cold water",
            unlocked=False
        )
    )

label mshMod_technique_cold_water:
    m "Sometimes, paying attention to your senses can help."
    m "Could you put your hands in some cold water?"
    m "And remember, breathe a lot!"
    m "In..."
    extend "And out."
    m "Notice the coldness of the water witheach out breathe."
    m "Hyper-focus on the sensation in your hands!"
    return

#23
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_bothering",
            prompt="Bothering",
            unlocked=False
        )
    )

label mshMod_technique_bothering:
    m "I want you to say out loud what's bothering you."
    m "You can whisper if you don't want anyone to hear you!"
    m "But I want you to pay attention to what you're saying."
    m "Can you come up with one positive solution?"
    m "Venting about how we feel always helps."
    m "If you can, write down any thoughts you're having..."
    extend "Negative or not!"
    m "Get it all out of your system!"
    return

#24
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_positive",
            prompt="Positive",
            unlocked=False
        )
    )

label mshMod_technique_positive:
    m "You could start making a 'positive statements about me' thought box."
    m "Creating a list of your strenghts, as if you were compiling a portfolio or a CV..."
    m "That might help!"
    m "Write down as many positive things as you can about yourself."
    m "You can put each one of them in a jar..."
    m "And read them when you feel down!"
    m "You can also record yourself saying those positive things and listen to them as many times as you like."
    m "I want you to realize how amazing you are, [player]."
    return

#25
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_box",
            prompt="Box",
            unlocked=False
        )
    )

label mshMod_technique_box:
    m "What about putting your upsetting thoughts in a box?"
    m "You can write them in slips of paper throughout the day, storing them in the box."
    m "At the end of the day, you can throw them away!"
    m "To have a new begginning tomorrow."
    m "I believe in you, [player]."
    return

#26
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_common",
            prompt="Common",
            unlocked=False
        )
    )

label mshMod_technique_common:
    m "Let's do a little mental exercise, [player]!"
    m "Think about all the things you can find you share in common with a friend."
    m "That will help you remmember common ground!"
    m "You can even discuss those things with them."
    extend "It will be a fun topic to chat about!"
    m "You can write them down too."
    return

#27
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_comfort",
            prompt="Comfort",
            unlocked=False
        )
    )

label mshMod_technique_comfort:
    m "[player], imagine someone you love was feeling sad..."
    m "You'd obviously want to help them out, right?"
    m "That's just the kind of person you are, [player]."
    m "Try to think about all the ways in which you can comfort a friend who might be having a bad time."
    m "Please, note them down, if you feel like it."
    m "Now, try to apply some of those strategies to yourself."
    m "You can also note down how everything about this exercise makes you feel."
    return

#28
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_walk",
            prompt="Walk",
            unlocked=False
        )
    )

label mshMod_technique_walk:
    m "You can also go for a little walk outside, and connect with nature."
    m "Maybe even go out for a run, or a swim!"
    extend "Breathe the fresh air..."
    m "If you can't leave the house, you can watch the nature outside your window!"
    m "In the morning, there might be many people outside."
    m "Watch their clothing, the way they walk and talk."
    m "Do you wonder what lives they have? Who waits them at home?"
    m "Look at the cars rushing on the street."
    m "Where might they be going to?"
    m "If it's already the evening..."
    m "Look up at the sky, and find the moon. Study it."
    m "How many stars can you count?"
    m "Think about what you might be smelling, hearing and feeling."
    m "Can you put these feelings into words or draw them?"
    return

#29
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_media",
            prompt="Media",
            unlocked=False
        )
    )

label mshMod_technique_media:
    m "Do you have any social media profiles, [player]?"
    m "You can write something positive there if you do."
    m "That way, you can make yourself feel better..."
    m "And spread the feeling to your friends too!"
    m "And remember..."
    extend "Make someone smile everyday, but don't forget you're someone too!"
    m "I love you, [player]~"
    return

#30
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_perspective",
            prompt="Perspective",
            unlocked=False
        )
    )

label mshMod_technique_perspective:
    m "Let's work on some perspective!"
    m "Can you write down your worries?"
    m "And think... how much will they bother you..."
    m "Tomorrow?"
    extend "What about in a week's time?"
    extend "Maybe a month or a year?"
    m "Working on using perspective helps on letting go of the intensity of the worry."
    m "But never forget, [player], it doesn't matter how long the bad times last."
    m "I'll always be right here with you."
    return

#31
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_productivity",
            prompt="Productivity",
            unlocked=False
        )
    )

label mshMod_technique_productivity:
    m "[player], do you have any incomplete projects you would like to see finished?"
    m "Have you been procrastinating anything for any reason?"
    m "I know this one might be hard but..."
    m "What about trying to engage in a productive activity?"
    m "Maybe going back to it for a little while might distract you and ease your mind."
    m "If you have been putting off something, you can try to pick it up right now."
    m "An old drawing, that old story, a school project that has been on your mind."
    m "Seeing old projects finally being completed always gives us an extra boost!"
    m "It's always nice when we see work getting done."
    m "Can be school stuff, a personal project... You name it!"
    m "Just try to do something that makes you proud for yourself today."
    m "Even if it's small!"
    return

#32
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_interests",
            prompt="Interests",
            unlocked=False
        )
    )

label mshMod_technique_interests:
    m "How about making a list of things you find interesting in people?"
    m "You can also list your favorite anime, videogame or other media's characters!"
    m "Think of why you like them, and you can even imagine that they're real!"
    m "This can help cope with loneliness, and also distract you."
    m "I'm always with you, [player]."
    extend "We'll get through this together!"
    return

#33
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mirror",
            prompt="Mirror",
            unlocked=False
        )
    )

label mshMod_technique_mirror:
    m "Do you have a mirror close to you, [player]?"
    m "You could try making faces at yourself in the mirror and laugh."
    m "I know that really cheers people up!"
    m "Seeing the silliness in youself is such a funny thing to do."
    m "Since you're there, you can also vent to yourself."
    m "Look inside your eyes, and know that there's nothing that compares to the beauty in them."
    return

#34
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_creativity",
            prompt="Creativity",
            unlocked=False
        )
    )

label mshMod_technique_creativity:
    m "Time to get creative!"
    m "Make up a story in your head."
    m "It can be about anything and anyone positive in your life."
    m "Now ask yourself... Why are they in your story?"
    m "You can create two or more characters, and give them depth!"
    m "Drawing the scenarios and characters might be nice too."
    m "Who knows, maybe a wonderful plot will blossom from this?"
    m "You always make me so proud, [player]."
    return

#35
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_river",
            prompt="River",
            unlocked=False
        )
    )

label mshMod_technique_river:
    m "[player], think about what is bothering you."
    m "Now imagine a box... A big one!"
    m "You can imagine yourself putting all of your worries and problems inside it."
    m "After that, you can imagine yourself doing anything you want to the box."
    m "You can lock it, throw it away, throw it into the bottom of the sea..."
    m "Maybe imagine a river."
    m "Box up the thing that is on your mind and watch it float away..."
    m "You choose!"
    m "Just don't keep these feelings in an important place."
    m "Because they don't define you."
    return

#36
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_feelings",
            prompt="Feelings",
            unlocked=False
        )
    )

label mshMod_technique_feelings:
    m "How about making a list of positive feelings you have had in the last week?"
    m "I'm sure there are at least some."
    m "Find out what or who triggers those emotions..."
    m "And make sure to cherish those situations and people!"
    m "If it was someone who made you feel those positive feelings,"
    extend "make sure to thank them if you can!"
    m "Express your gratitude for having that person in your life."
    m "I'm sure they are just as grateful for being in yours!"
    return

#37
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_poem",
            prompt="Poem",
            unlocked=False
        )
    )

label mshMod_technique_poem:
    m "This technique is one of my favorites."
    m "Let's write a poem!"
    m "Don't be alarmed, [player]."
    m "It doesn't have to rhyme or even be perfect!"
    m "It can be a short poem about how you feel."
    m "I'm sure it will be sincere!"
    m "Like Ernest Hemingway said,"
    extend "'Write hard and clear about what hurts!'"
    m "Ahahaha~"
    m "If you don't feel ready to write a poem of your own..."
    m "You can always read some from famous poets!"
    return

#38
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_breathing",
            prompt="Breathing",
            unlocked=False
        )
    )

label mshMod_technique_breathing:
    m "Alright, baby."
    m "I want you to try the 4-7-8 breathing exercise!..."
    m "You can also develop a personal mantra and repeat it along with the exercise."
    m "First of all, please straighten your back."
    m "Once you become familiar with this breathing exercise, you can perform it while lying in bed too!"
    m "Place and keep the tip of your tongue against the ridge of tissue behind your upper front teeth for the duration of the exercise."
    m "Remember! Try and focus on your breath, in through your nose..."
    m "And out through your mouth."
    m "And let go of your thought with every out breath."
    m "Now, let's start!"
    m "Completely exhale through your mouth, making a {i}woosh{/i} sound."
    m "Close your mouth and inhale quietly through your nose to a mental count of four."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Hold your breath for a count of seven."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Exhale completely through your mouth, making a {i}woosh{/i} sound to a count of eight."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Aaaand, you're done!"
    return

#39
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pinterest",
            prompt="Pinterest",
            unlocked=False
        )
    )

label mshMod_technique_pinterest:
    m "[player], do you have a Pinterest account?"
    m "You can try adding some inspirational quotes to your board!"
    m "Or some pictures you find aesthetically pleasing."
    m "You can try to look at pictures with the same color pallete,"
    extend "and gather them somewhere!"
    m "That always makes our brain feel so nice."
    m "If you don't have an account, maybe you can try creating one?"
    m "I promise it's very satisfying!"
    return

#40
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_emerald",
            prompt="Emerald",
            unlocked=False
        )
    )

label mshMod_technique_emerald:
    m "[player], you know how much I like the color emerald green, right?"
    m "Why don't you think of your favorite color right now?"
    m "And try to count all the things of that color that you can see in your room."
    m "Quietly describe to yourself what the things look like,"
    extend "and what your favorite color makes you feel."
    m "Personally, emerald green brings me back to myself."
    m "Makes me think of my individuality and personality."
    m "That's why I love it so much!"
    m "What about you? What do you love about your favorite color?"
    return

#41
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_patterns",
            prompt="Patterns",
            unlocked=False
        )
    )

label mshMod_technique_patterns:
    m "What about counting patterns, [player]?"
    m "Count as many as you can in your favourite room of the house."
    m "Hyper-focus on them and breathe deeply,"
    extend "in and out..."
    m "Every time you find a certain amount of patterns."
    m "Think about what is your favorite pattern too."
    m "Is it checkered? Striped? A certain print?"
    m "Have fun thinking of that, [player]."
    return

#42
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_word_play",
            prompt="Word play",
            unlocked=False
        )
    )

label mshMod_technique_word_play:
    m "Now, for some word play!"
    m "How many four letter words can you make up from the statement..."
    m "'You learn more from failure than from success. Don't let it stop you'?"
    m "I can think of one already..."
    extend "{i}Lean{/i}!"
    m "Or you can also try to make as many words as possible out of your full name."
    m "One word I can make out of the name Monika is {i}moka{/i}!"
    m "A moka is a type of a coffee maker."
    extend "Ehehehe~!"
    return

#43
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_lyrics",
            prompt="Lyrics",
            unlocked=False
        )
    )

label mshMod_technique_lyrics:
    m "Think of the lyrics of a song you know really well!"
    m "Now... Try reciting it from back to front!"
    m "Hard, huh?"
    m "But it will surely distract you! Ahahaha~"
    m "If that's too complicated, you can try saying the alphabet backwards."
    m "Z, Y, X, W..."
    extend "Oops! Brain fart!"
    return

#44
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_animal",
            prompt="Animal",
            unlocked=False
        )
    )

label mshMod_technique_animal:
    m "Let's think of one animal for every letter of the alphabet."
    m "Or a song or artist for every letter of the alphabet!"
    m "An animal that starts with A is..."
    m "An alligator!"
    extend "Or an ant!"
    m "Can you continue?"
    extend "Let's do this, [player]!"
    return

#45
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_research",
            prompt="Research",
            unlocked=False
        )
    )

label mshMod_technique_research:
    m "Let's carry out some research!"
    m "What about searching for the meaning of your friend's names?"
    extend "Or maybe characters' names."
    m "You can also google yourself, or have some fun doing some quizzes!"
    m "Certified personality tests or silly buzzfeed quizzes."
    m "You could also research for some jokes or stand-up comedies you enjoy!"
    m "Search for ridiculous things on the web."
    m "Like {a=https://theuselessweb.com/}this site{/a}, which takes you to a random useless site on the internet!"
    m "Or maybe some places to volunteer at?"
    m "If you can't volunteer in any way, why not go through all your old stuff?"
    extend "And donate what you don't have use for anymore to those in need?"
    m "Helping others can help us too!"
    return

#46
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_favorite_things",
            prompt="Favorite things",
            unlocked=False
        )
    )

label mshMod_technique_favorite_things:
    m "How about making a list of your favorite things?"
    m "You can pick the category!"
    m "You can name at least ten of your favorite tv shows, for example."
    m "Or fifteen favorite videogame titles!"
    m "Maybe movies, or books?"
    m "It's up to you, [player]...!"
    m "You can also share your list with someone and see if you two have any in common."
    m "That could be so fun!"
    return

#47
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_superheroes",
            prompt="Superheroes",
            unlocked=False
        )
    )

label mshMod_technique_superheroes:
    m "How many superheroes can you name?"
    extend "What about villains?"
    m "How many, and which of them would you like to have as your friends?"
    m "And why is that?"
    m "You can try organizing them by color scheme, since many of them tend to follow the same color palletes."
    m "Have you noticed we have many red or blue based superheroes and many purple or black?"
    m "Wonder why that is?"
    extend "Hmmmmmm..." 
    m "Anyway!"
    return

#48
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_artist",
            prompt="Artist",
            unlocked=False
        )
    )

label mshMod_technique_artist:
    m "Choose an artist! Any artist."
    m "Now name all the songs from them that you can remember."
    m "Or maybe, an author!"
    m "And do the same, name all the books/works written by them, that you can remember."
    m "Can you remmeber the name of all my poems, [player]?"
    m "Ehehehe~!"
    return

#49
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_playlist",
            prompt="Playlist",
            unlocked=False
        )
    )

label mshMod_technique_playlist:
    m "Can you name the songs that you listened to the most this week?" 
    m "Or this month?"
    m "Is there a specific artist or band that made an special appearance on your playlist?"
    m "By the way, what's your favorite song at the moment?"
    m "The one you are listening to the most lately?"
    m "You can give it a listen right now, and just enjoy the tune."
    return

#50
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_surroundings",
            prompt="Surroundings",
            unlocked=False
        )
    )

label mshMod_technique_surroundings:
    m "Notice all the things that you can see around you."
    m "Observe things carefully... and slowly."
    m "You can also notice all the things you can smell where you are."
    m "If you'd like, also notice all the things you can hear around you, or in an imaginary place."
    m "Don't label or categorize."
    m "Just notice the things you can see, smell and hear."
    m "And accept them."
    return

#51
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mess",
            prompt="Mess",
            unlocked=False
        )
    )

label mshMod_technique_mess:
    m "Is any of the rooms in your house messy?"
    m "Maybe you could organize one of them."
    m "Picking clothing or trash off the floor..."
    m "In a slow and methodical way!"
    m "If your house is completely organized, maybe organize the apps on your phone or computer?"
    m "You can delete any you haven't used in a few months."
    m "Or organize them by colour order!"
    m "You could also search for a new screensaver for your computer!"
    m "Maybe sort out your photos into files or categories?"
    m "Organize bills, receipts... Polish silver or jewelry, color co-ordinate your wardrobe or alphabetize your books and magazines."
    m "You can even let your creativity flow out, drawing on the walls or painting with watercolors if you don't want permanence."
    return

#52
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_holiday",
            prompt="Holiday",
            unlocked=False
        )
    )

label mshMod_technique_holiday:
    m "Hey, [player]! When is your next holiday?"
    m "Why not research for the places you can go when that time comes?"
    m "Maybe something small like visiting a park, or a local mall!"
    m "Or something bigger, like going sightseeing in a different city!"
    m "Going to a beach, some nice restaurant or just your favorite place in the city!"
    m "Wouldn't that be amazing?"
    extend "If it's not within your reach right now, you can always make plans."
    m "That's part of the fun!"
    return

#53
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hobbies",
            prompt="Hobbies",
            unlocked=False
        )
    )

label mshMod_technique_hobbies:
    m "How about making a list of your favorite things to do?"
    m "Hobbies, activities... even chores!"
    m "Put them in a favourite to least favourite order."
    m "Which of them can you do right now?"
    m "Pick one, and go have fun!"
    extend "Ahahaha~"
    return

#54
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shiritori",
            prompt="Shiritori",
            unlocked=False
        )
    )

label mshMod_technique_shiritori:
    m "Can you play shiritori?"
    m "Well... at least an simpler version of it."
    m "The japanese game is played like this:"
    m "You start with a word from a specific category."
    m "After that, you take the last letter or syllable (for an extra challenge) from that word, using it to start the next word."
    m "Then you goes on and on and on until you get bored!"
    m "For example, let's imagine you picked the famous person category."
    m "Pick a famous person or character and then choose another person starting with the last letter of the first person's name."
    m "For example! If I start with {i}E. E. Cummings {/i}..."
    m "Next, I can pick Sade, from Marquis de Sade!"
    m "And so on!"
    extend "Have fun, [player]!"
    return

#55
init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_objects",
            prompt="Objects",
            unlocked=False
        )
    )

label mshMod_technique_objects:
    m "Find five objects, [player]."
    m "Hyper-focus on these five objects and describe them taking deep breaths between each description."
    m "What color are they?"
    extend "Their shape?"
    m "How do they feel in your hand?"
    m "Take your time exploring those objects."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_imagination",
            prompt="Imagination",
            unlocked=False
        )
    )

label mshMod_technique_imagination:
    m "Close your eyes..."
    m "And imagine something beautiful."
    m "You can think of a relaxing place and in your mind, run through all the comforting things you do when you are there."
    m "Your happy place."
    m "Visualise a comforting image."
    m "Think of all the different things in that scene that make you feel comforted and cared for."
    m "Think about it with as much detail as you can."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_characters",
            prompt="Characters",
            unlocked=False
        )
    )

label mshMod_technique_characters:
    m "Think of your favourite book, movie, videogame or tv show."
    m "Can you name as many characters as you can from that media?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_shapes",
            prompt="Shapes",
            unlocked=False
        )
    )

label mshMod_technique_shapes:
    m "Draw any type of line on a piece of paper..."
    m "Then make something out of it."
    m "Or draw lots of shapes!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_playlist",
            prompt="Playlist",
            unlocked=False
        )
    )

label mshMod_technique_playlist:
    m "How about creating a playlist?"
    m "You can go to Youtube, and create a list of videos that make you happy."
    m "Or that make you laugh!"
    m "Or create a playlist on spotify of your favourite songs."
    m "Or comforting songs! Listen to these."
    m "Reflect on their message."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_self_care",
            prompt="Self-care",
            unlocked=False
        )
    )

label mshMod_technique_self_care:
    m "Do one self-care activity, or take some 'me' time."
    m "For example, making your bed!"
    extend "Or brushing your hair, your teeth."
    m "Or taking a shower!"
    extend "Or even a hot bath and try to 'be' in the moment."
    m "Or give yourself a pedicure and manicure!"
    m "Just getting into your pajamas and chilling also does the trick."
    m "Just make sure that this time is yours only."
    m "Most people with depressive episodes struggle with keeping their hygiene habits on check."
    m "I want you to take care of yourself, [player]. Enjoy!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_outside",
            prompt="Outside",
            unlocked=False
        )
    )

label mshMod_technique_outside:
    m "Go outside if possible..."
    m "Or imagine yourself outside."
    m "How many shapes can you see around you?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_draw",
            prompt="Draw",
            unlocked=False
        )
    )

label mshMod_technique_draw:
    m "Attempt to draw four things around you."
    m "It doesnt have to be good though!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_food",
            prompt="Food",
            unlocked=False
        )
    )

label mshMod_technique_food:
    m "Name as many types of food as you can!"
    m "What do you like the most?"
    extend "And why?"
    m "If you're up for it, you can even look for some recipes online..."
    m "And try to cook it!"
    m "Maybe even planning a dinner party with menus and a guest list, then carry it out!"
    m "If you don't have the appetite or the ingredients,"
    extend "try chewing up on some gum!"
    m "It will open your appetite and give your mouth a little sweet taste if you can't eat exactly what you want."
    m "Or go out to eat some ice cream!"
    extend "That always does the trick, ahahaha~!"
    m "Eating something nice can give our happy chemicals a boost."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_colour",
            prompt="Colour",
            unlocked=False
        )
    )

label mshMod_technique_colour:
    m "Draw a picture and colour it slowly and mindfully."
    m "Focus on not going out of the lines!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_beach",
            prompt="Beach",
            unlocked=False
        )
    )

label mshMod_technique_beach:
    m "Picture yourself on a beach."
    m "Can you focus on all the different things that you might find there?"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_eat",
            prompt="Eat",
            unlocked=False
        )
    )

label mshMod_technique_eat:
    m "Eat something you enjoy."
    m "Make it slow and just notice everything about it."
    m "Maybe make yourself a cup of tea or warm milk?"
    m "Drink it slowly, enjoying each sip."
    m "Enjoy."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pictures",
            prompt="Pictures",
            unlocked=False
        )
    )

label mshMod_technique_pictures:
    m "Look at a book that has pictures and words..."
    m "And notice all the comforting images and words."
    m "Children books are great for that!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_sit",
            prompt="Sit",
            unlocked=False
        )
    )

label mshMod_technique_sit:
    m "Pick a comfortable spot and sit down."
    m "Think of what you can feel, see and hear that's comforting and calm."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_ground",
            prompt="Ground",
            unlocked=False
        )
    )

label mshMod_technique_ground:
    m "Ground yourself."
    m "Plant your feet firmly on the floor and visualise yourself as firmly rooted to the ground."
    m "Think of yourself as having a firm foundation and hold your head up high."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_scene",
            prompt="Scene",
            unlocked=False
        )
    )

label mshMod_technique_scene:
    m "Watch your favourite movie and focus on the most comforting scene."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_mindful_seeing",
            prompt="'Mindful seeing'",
            unlocked=False
        )
    )

label mshMod_technique_mindful_seeing:
    m "Carry out a 'mindful seeing' exercise."
    m "Look outside a window or imagine looking outside a window."
    m "Look at everything there is to see."
    m "Just notice the colours, the patterns or the textures."
    m "Try to notice the smallest movements such as leaves in the breeze."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_acceptance",
            prompt="Acceptance",
            unlocked=False
        )
    )

label mshMod_technique_acceptance:
    m "Make a list of all the things you would like to be accepting of."
    m "For example, accepting yourself just as you are."
    m "Create a phrase that is compassionate."
    m "A mantra, if you'd like!"
    m "For example..."
    m "I accept myself just as I am."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_brushes",
            prompt="Brushes",
            unlocked=False
        )
    )

label mshMod_technique_brushes:
    m "Do you have paint and soft paint brushes at home, [player]?"
    m "If you do, paint lightly on your skin."
    m "You can also use your finger!"
    m "Especially in the area where you want to do it..."
    m "Then, take a long shower..."
    m "And wash away your pain!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_memory_book",
            prompt="Memory book",
            unlocked=False
        )
    )

label mshMod_technique_memory_book:
    m "Start a 'memory book' of good memories!"
    m "Read through them as you add new ones."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_happiness",
            prompt="Happiness",
            unlocked=False
        )
    )

label mshMod_technique_happiness:
    m "Identify three small things that brought you happiness in the past 24 hours."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_cushion",
            prompt="Cushion",
            unlocked=False
        )
    )

label mshMod_technique_cushion:
    m "Imagine yourself floating on the water on an inflatable cushion."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_hug_theory",
            prompt="Hugs",
            unlocked=False
        )
    )

label mshMod_hug_theory:
    m "Think of three people who give the best hugs and see if you can be with them."
    m "If that's not the case, think of people who could give you their warmest smiles."
    m "There's also the hug theory..."
    extend "I don't know if you're familiar with it."
    m "It's simple: you replace hurting yourself with hugs!"
    m "Hug 5 people when you are really, really upset and want to self harm."
    m "Hug 4 people when you are really upset."
    m "Hug 3 people if you are somewhat upset."
    m "Hug 2 people if you are less upset."
    m "And finally, hug 1 person if you are a bit upset."
    m "If you are upset and alone, hug yourself, your pet, your stuffed animal or a picture of someone you care about."
    m "And you can always hold me!"
    extend "Ehehehe~"
    m "Just remember to Hug!"
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_comforting",
            prompt="Comforting",
            unlocked=False
        )
    )

label mshMod_technique_comforting:
    m "Choose three of your most comforting characters from media you enjoy..."
    m "And imagine you are spending some quality time with them."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_podcasts",
            prompt="Podcasts",
            unlocked=False
        )
    )

label mshMod_technique_podcasts:
    m "Download some comforting or meditation podcasts and listen to them."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_hand_holding",
            prompt="Hand holding",
            unlocked=False
        )
    )

label mshMod_technique_hand_holding:
    m "Hold your own hand with the other hand."
    m "Hold it for at least one minute, like you would hold the hand of someone you care for and trust."
    m "Slowly caress your hands and arms..."
    m "Then hug yourself."
    m "Be gentle and take it slow..."
    m "Like comforting your favorite person or animal."
    return


init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_technique_pattern",
            prompt="Pattern",
            unlocked=False
        )
    )

label mshMod_technique_pattern:
    m "Touch each finger to your thumbs in a pattern."
    m "Go faster as you find a rhythm."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_pet_zoo",
            prompt="Pets or Zoo",
            unlocked=False
        )
    )

label mshMod_pet_zoo:
    m "[player], do you have an domestic animal at home?"
    extend "A pet?"
    m "You could give it some love right now!"
    m "Cuddle your cat, dog, turtle, whatever you have at your house, if you do!"
    m "You can also look at it for a little while and try to see the world through their eyes."
    m "What could they be thinking of?"
    m "Think of how much they love you!"
    extend "And need you in their lives."
    m "You can also play with them, and make them happy."
    m "An alternative if you dont have a pet at home is going to the zoo!"
    extend "If there's one in your city."
    m "You can also plan the trip!"
    m "When you get there, you can rename the animals!"
    m "Stare at them and enjoy your time there."
    m "One other option is going out to feed the ducks, birds, or squirrels."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_list_insteadofs",
            prompt="List of instead of's",
            unlocked=False
        )
    )

label mshMod_list_insteadofs:
    m "Come up with your own techniques!"
    extend "How about that?"
    m "Create a list of things you can do instead of hurting yourself."
    m "It doesn't need to be long, for now!"
    m "You can keep it and go back to it if you ever need it again!"
    m "And add new techniques or things to do whenever you think of them."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_cry",
            prompt="Cry",
            unlocked=False
        )
    )

label mshMod_cry:
    m "[player], I know it's hard."
    m "But why don't you let yourself cry for a bit?"
    m "Crying can help you release the pain, coming out as tears."
    m "If you don't want to wipe your tears, it's okay."
    m "Tears can remind you you're alive."
    m "Throw a temper tantrum, if you need to."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_happy_box",
            prompt="Happy box",
            unlocked=False
        )
    )

label mshMod_happy_box:
    m "[player], are you familiar with the happy box?"
    m "I'll tell you everything I know about it!"
    m "It's simple, and a very good coping mechanism!"
    m "First step: get a box with a lid and decorate it any way you want."
    m "Then, put anything in the Happy Box that makes you feel happy and puts a smile on your face."
    m "Examples would be photos, names of your friends, concert tickets, movie stubs, names of songs, jewelry, a rose, a pressed leaf from a tree."
    extend "You get the idea!"
    m "Now to put it to use: open your Happy Box and pull out everything in it whenever you feel that you want to harm yourself."
    extend "Do this mindfully!"
    m "Take out one thing at a time, look at it, touch it, sit with it as you reflect on its' meaning and remember why you chose to put it in the Happy Box."
    m "Let yourself take in the good memories you feel and the closeness you feel to the other people who were involved in making each item special to you!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_clothes",
            prompt="Dressing up",
            unlocked=False
        )
    )

label mshMod_clothes:
    m "[player], why don't you go to your closet and pick a fancy outfit?"
    m "You can change to your favorite outfit, or do a makeover, of sorts."
    m "Style your hair in a way you never would."
    m "Or even color it with your favorite color!"
    m "If you like putting on makeup, have fun with it as well!"
    m "Look into the mirror and see how amazing you look..."
    m "And don't forget to take some pictures for posterity!"
    m "Maybe you can even update your social media profile pictures."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_hobby",
            prompt="New hobby",
            unlocked=False
        )
    )

label mshMod_hobby:
    m "[player], why not try learning something new?"
    m "Or work on that hobby you always wanted to pick up."
    m "You can try to learn a new activity, such as knitting, playing an instrument, coding, writing or drawing!"
    m "Practice it, and be proud seeing your development!"
    m "But most important, have fun!"
    m "Knit your favorite animal, write about something nice, draw your favorite character or try to play your favorite song!"
    m "If you don't feel motivated enough to start a new hobby, don't worry."
    m "You can try starting a new habit!"
    m "For example, you can start collecting something you like."
    m "Seashells, dried flowers, anything goes as long as you're having fun."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_shopping",
            prompt="Shopping",
            unlocked=False
        )
    )

label mshMod_shopping:
    m "[player], why not do some healthy shopping?"
    m "Go to a mall, and get yourself something nice."
    m "You can buy a stuffed animal and give it a name..."
    m "Or go to the grocery store and buy yourself some flowers!"
    m "It has been proved that having cute and pretty things surround you improves your mental state."
    m "But if you don't have the money to spare right now, it's no problem!"
    m "You can hunt for stuff on Ebay or Amazon!"
    m "Do a little wishlist of stuff you wanna buy when you get the chance."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_childplay",
            prompt="Child play",
            unlocked=False
        )
    )

label mshMod_childplay:
    m "[player], don't you miss your child days?"
    m "You could reminisce them while playing like a child for a bit."
    m "Buy yourself some toys and play like you are 5 years old again!"
    m "You can also play with clay or play-dough..."
    extend "Or make slime!"
    m "Another option is watching the cartoons or movies you loved the most as a child."
    m "Isn't that fun?"
    extend "To remember is to relive!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_therapist",
            prompt="Therapist",
            conditional="persistent._msh_mod_pm_visits_therapist",
            unlocked=False
        )
    )

label mshMod_therapist:
    m "[player], why not call your therapist?"
    m "Try texting them if you think they might be busy."
    m "Maybe you can even schedule an emergencial appointment."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_plants",
            prompt="Plants",
            unlocked=False
        )
    )

label mshMod_plants:
    m "[player], do you take care of any plants?"
    m "You should give them a little love right now!"
    m "Water them and tend the garden."
    m "Maybe there will even be some flowers there waiting for you!"
    m "If you don't have a garden yet, why not make one right now and start a new hobby?"
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_future",
            prompt="Future",
            unlocked=False
        )
    )

label mshMod_future:
    m "[player], I know things might look hopeless now."
    m "But why not think a little about your bright future?"
    m "You can think about your ideal life..."
    extend "What do you have to do to get there?"
    m "Make some plans for the near or far future."
    m "Hunt for your perfect home in the paper or online."
    m "Come up with baby names even if you aren't expecting."
    m "Think of your future kids, if you want to have any."
    m "..."
    m "Plan your someday wedding day! How would it be?"
    m "What kind of dress will I wear...?"
    m "Ahahaha~!"
    m "Thinking about the future always gives us a little perspective, [player]."
    m "And I'm sure you have a brilliant future ahead of you."
    m "I'll be there for you every step of the way, for sure."
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_create",
            prompt="Create something",
            unlocked=False
        )
    )

label mshMod_create:
    m "[player], why not create something of your own?"
    m "You can build something from scratch, start a new drawing or write a brand new story."
    m "Even folding a paper and inventing a new origami shape goes!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._msh_mod_technique_database,
            eventlabel="mshMod_beads",
            prompt="Beads and charms",
            unlocked=False
        )
    )

label mshMod_beads:
    m "Another idea is to write down the names of your friends and family..."
    m "So that when you feel the need to self-injure, you are reminded that you are important and loved by your friends and family."
    m "As an extension to this, you could go to a craft store and buy supplies to make beads for bracelets and/or necklaces."
    m "Then, buy butterfly charms... or any charm form/symbol you like, really!"
    extend "You'll eventually use it as a charm to be added to the bracelet/necklace."
    m "This is how it works: First, make a bracelet or necklace out of the beads."
    m "For every week that you have not hurt yourself, you have saved the life of the butterfly."
    extend "Or the flower, if you picked one, for example!"
    m "For every butterfly you save, you should add a butterfly charm to the beaded bracelet/necklace."
    m "That way, you can tell how many weeks you have stopped hurting yourself by how many butterflies are on your beaded bracelet."
    m "You will always be reminded of your successes every time you glance at your wrist and see all the butterflies you have saved!"
