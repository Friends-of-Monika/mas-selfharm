# RANDOM TECHNIQUES TO BE PICKED IN THE NON-RANDOM MAIN EVENT.
# A reminder that I'm going to have to add conditions for things like religion------------------------------------------------
default persistent._mas_technique_database = {}
#1  



init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_religion",
            unlocked=True,
        ),
    ) 

label technique_religion:
    $ technique1 = True
    m "I remember you mentioned having a religion before."
    m "Could you please say a little prayer?"
    m "It can be silent, you don't need to say anything out loud."
    m "You can pray to whatever, or even just think of how big and amazing our universe is."
    m "Try to think about the good things, your favorite things..."
    m "How little they may be. Think about the bigger picture."
    m "If you believe in an actual god or deity, you can imagine them out there, looking out and caring for you."
    m "You are needed, [player]. And you are part of something much bigger than your bad thoughts or bad feelings!"

    return

#2
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_cozy",
            unlocked=True,
        ),
    ) 

label technique_cozy:
    $ technique2 = True
    m "You know what often helps me calm down?"
    m "Staying cozy!"
    m "Try wrapping up in something suuuper cozy!"
    m "A sheet or a favorite jumper for example."
    m "Anything works, really."
    m "As long as you get that calming sensation!"
    m "There's nothing like it!"

    return
#3
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_photographs",
            unlocked=True,
        ),
    ) 

label technique_photographs:
    $ technique3 = True
    m "Nothing is ever really lost to us as long as we remember it."
    m "Do you see where I'm going with this, [player]?"
    m "One thing that could help you get over bad times is look at photographs of the good ones!"
    m "They will remind you that even though the good times don't last forever, the bad ones won't either!" #is this line ok? Might be a little dark for people that need inspiration idk
    m "If you have any around, look at photographs of when you were happy, enjoying life to the fullest!"
    m "I wish we had some together..."
    m "I'd look at us all the time!"

    return

#4
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_quotes",
            unlocked=True,
        ),
    ) 

label technique_quotes:
    $ technique4 = True
    m "I remember hearing this quote somewhere {i}'Hope is the last thing ever lost'{/i}."
    m "Doing your best to believe in positive things can be really uplifting!"
    m "I think a good way of seeing the things around you in a better light would be seeing inspirational quotes!"
    m "You should find some quotes on the internet that you like, write each of them on a sticky note and put them somewhere you'd regularly see." #add a link for some quotes??
    m "Every time you see one, you will remember things get better!"

    return
#5
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_singing",
            unlocked=True,
        ),
    ) 

label technique_singing:
    $ technique5 = True
    m "This one's going to be really simple."
    m "Sing a song!"
    m "Not just any song, though."
    m "Your absolute favorite!"
    m "I'd love to know what your favorite song is..."
    m "Anyway..."
    m "Try singing your favorite song until you feel better."
    m "Singing can be a really good outlet for your emotions!"
    m "You could also imagine we're singing 'Your Reality' together!" # I don't know about this. I'm trying to get Moni more involved SOMEHOW. Since the player is there in the first place it makes sense, right?? Feel free to adjust anything...
    m "Hehe~"

    return

#6
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_talking",
            unlocked=True,
        ),
    ) 

label technique_talking:
    $ technique6 = True
    m "Sometimes simply talking about your problems can help a lot!"
    m "Or just talking to distract yourself."
    m "You should call or text a friend!"
    m "I know you're here with me, but it's not {i}exactly{/i} the same as having a real-time conversation with someone!" #ehhhh, idk about this, Gaby help correct this hehe.
    m "I wish I could hear your voice..."
    m "We could talk for hours!"
    m "As long as you'd want."

    return
#7
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_hugs",
            unlocked=True,
        ),
    ) 

label technique_hugs:
    $ technique7 = True
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

#8
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_listening",
            unlocked=True,
        ),
    ) 

label technique_listening:
    $ technique8 = True
    m "Try listening to a few songs you love!"
    m "But don't {i}just{/i} listen."
    m "Try paying attention."
    m "Focus on certain instruments or parts, their notes, and how they add to the song as a whole!"
    m "That could serve as a distraction and learning something about the things you love at the same time!"
    m "We could always listen to them together if you'd like!"

    return
    
#9
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_butterfly",
            unlocked=True,
        ),
    ) 

label technique_butterfly:
    $ technique9 = True
    m "Could you take some deep breaths? And also, a marker, or a pen."
    m "I would like for you to scribble on the place you want to harm yourself."
    m "Most methods use a butterfly drawing."
    m "You could draw the butterfly and name it, and if you do harm yourself, you harm it, too."
    m "Whenever you look at it and think of harming yourself, do something comforting instead!"
    m "Sing along to a tune, watch your favorite film, go out on a walk..."
    m "Maybe you have some old photos? If they bring back good memories, why not trying to search for them?"
    m "I would really like to look at them with you, [player]."
    m "But that's not about me, I want you to feel better!"
    m "And don't give up, [mas_get_player_nickname()]."

    return
    
#10

init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_healing",
            unlocked=True,
        ),
    ) 

label technique_healing:
    $ technique10 = True
    m "[player], do you have a first aid kit at home?"
    m "Maybe some sticking plasters, band-aids?"
    m "Could you stick some of them where you want to hurt yourself?"
    m "As a reminder that you are letting yourself heal."
    m "And remember, healing takes time."
    m "And we have all the time in the world."
    m "No need to rush this, okay?"
    m "Baby steps!"

    return

#11
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_pong",
            unlocked=True,
        ),
    ) 

label technique_pong:
    $ technique11 = True
    m "[player], perhaps playing something would make you feel better?"
    m "Do you want to play Pong?"
    menu:
        "Sure!":
            m "Great!"
            m "Bring it on!"
            call demo_minigame_pong
            m "Hope you're feeling better, [player]!"

            return
        
        "Maybe next time, [m_name]":
            m "Okay, [player]."
            m "Let's play soon!"

            return


#12

init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_chess",
            unlocked=True,
        ),
    ) 

label technique_chess:
    $ technique12 = True
    m "[player], perhaps playing something would make you feel better?"
    m "Do you want to play Chess?"
    menu:
        "Sure!":
            m "Okay!"
            call mas_chess
            m "Hope you're feeling better, [player]!"

            return

        "Maybe next time, [m_name]":
            m "Okay, [player]."
            m "Let's play soon!"

            return

#13
init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_piano",
            unlocked=True,
        ),
    ) 

label technique_piano:
    $ technique13 = True
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

        "Maybe next time, [m_name]":
            m "Okay, [player]."
            m "Let's play soon!"
            
            return
    
    
