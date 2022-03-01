# RANDOM TECHNIQUES TO BE PICKED IN THE NON-RANDOM MAIN EVENT.
default persistent._mas_technique_database = {}
#1  

label randomness:
    $ randtechnique = renpy.random.randint (1, 2)
    if randtechnique == 1:
        if technique1 == False:
            call technique_religion 
        else:
            while randtechnique == 1:
                jump randomness        
    elif randtechnique == 2:
        if technique2 == False:
            call technique_cozy
        else:
            while randtechnique == 2:
                jump randomness


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
    if $ persistent._mas_pm_religious == True:
        m 5eka "I remember you mentioned being religious before..."
        m 3ett "Maybe you could say a little prayer?"
        m 4eud "It can be silent, you don't need to say anything out loud."
        m 1fua "You can pray about anything you want, or even just think of how vast and amazing your universe is."
        m 1dsu "Try to think about the good things, like animals or laughter, your favorite things..."
        m "No matter how little they may be, take some time to think about the bigger picture."
        m "If you believe in gods or deities, you can imagine them out there, looking out and caring for you."
        m "You are needed, [player]. You are part of something much bigger than your bad thoughts or bad feelings!"
    else:
        jump technique_cozy

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
    m "A sheet, a blanket or a favorite jumper for example."
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
    m "Maybe you have some old photos? If they bring back good memories, why not trying to search for them?"
    m "They will remind you that even though the good times don't last forever, the bad ones won't either!" 
    m "If you have any around, look at photographs of when you were happy, enjoying life to the fullest!"
    m "I wish we had some together..."
    m "I'd look at us all the time!"
    m "I would really like to look at them with you, [player]."
    m "But that's not about me, I want you to feel better!"
    m "And don't give up, [mas_get_player_nickname()]."

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
    m "You should find some quotes on the internet that you like, write each of them on a sticky note and put them somewhere you'd regularly see." 
    m "Every time you see one, you will remember things get better!"
    m "You can also say some of them aloud, to inspire yourself!"

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
    m "You could also imagine we're singing 'Your Reality' together!"
    m "Hehe~"
    m "You can sing as loud as you want!"
    m "Also, if you'd like, write your favourite lyrics down."
    m "Think about what they mean to you!"

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
    m "Maybe send some long distance friends a surprise message?"
    m "I know you're here with me, but it's not {i}exactly{/i} the same as having a real-time conversation with someone!"
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
    m "You can also draw or write some positive things on your arm."

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
    
 #14
    init 5 python:
    addEvent(
        Event(
            persistent._mas_technique_database,
            eventlabel="technique_videos",
            unlocked=True,
        ),
    ) 

label technique_videos:
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
    
    else:
        pass
    

label Moni_1:
    $ video1 = True
    $ webbrowser.open("https://www.youtube.com/watch?v=PppkNH3bKV4&")
    m "There we go!"
    m "I hope it helps, [player]."
    m "I will give you some time to watch it."
    pause(3.0)
    menu:
        "I'm done, [m_name]":
            m "Alright!"
            m "Hope you enjoyed it!"
                    
    return  

  
label Moni_2:
    $ video2 = True
    $ webbrowser.open("https://www.youtube.com/watch?v=-SJywvgaJEI&")
    m "There we go!"
    m "I hope it helps, [player]."
    m "I will give you some time to watch it."
    pause(3.0)
    menu:
        "I'm done, [m_name]":
            m "Alright!"
            m "Hope you enjoyed it!"
        
    return


label Moni_3:
    $ video3 = True
    $ webbrowser.open("https://www.youtube.com/watch?v=ORkx63VeP9Y&")
    m "There we go!"
    m "I hope it helps, [player]."
    m "I will give you some time to watch it."
    pause(3.0)
    menu:
        "I'm done, [m_name]":
            m "Alright!"
            m "Hope you enjoyed it!"
                    
    return 
            
#15
    m "Some objects can also help with the desperate feeling."
    m "Check if you have one of them at home, okay?"
    m "Do you have a stress ball?
    m "A stress ball or hand exercise ball is a malleable toy, which is squeezed in the hand and manipulated by the fingers, ostensibly to relieve stress and muscle tension or to exercise the muscles of the hand."
    m "If you do have one, squeeze it really hard. Relive all your tension!"
    m "You can also use a sheet of bubble wrap. So satisfying!"
    m "If you do have one at home, burst each bubble as slowly as you can, please."
    m "Or just enjoy yourself! The techniques have no rules, as long as they make you feel better."
    m "I have another one! Do you have any baloons at home?"
    m "You can blow one baloon for each emotion you feel."
    m "After that, pop each one of them!"
    
#16

    m "You know what often helps me calm down?"
    m "Stretching myself!"
    m "You can try stretching your body as much as you can, scrunching up your muscles until they hurt, then release."
    m "Tense all of your body starting from toes, up to your hands, and release!"
    m "This relaxes our body so much!"
    m "You can also do an upper back strech."
    m "This one is done sitting, with your feet flat on the floor."
    m "Interlock your fingers and reach forward, bending from your middle back. Stretch with your hands forward at shoulder level. 
    m "You should feel the stretch between your shoulder blades."
    m "Ooh, relaxing!"
    m "After tensing your muscles, you can let go and relax into something comfy."
    
#17
    m "Okay.{w=0.5} I want you to try this."
    m "This one is to let out all of your anger!"
    m "We're going to punch it out!"
    m "I need you to find a pillow and punch out how you feel."
    m "A pillow is good because it won't hurt your fingers!"
    m "Punch, punch, punch the pain away!"
    m "If you don't want to punch, you can scream into it too."
    m "Scream into the pillow to release your tension!"
    m "Another way out is squashing the pillow hard..."
    m "And gently letting go."
    
#18
    m "This one might be... a little loud."
    m "I would like for you to go somewhere private..."
    m "And shout very loudly."
    m "You can shout anything you want!"
    m "You can shout gibberish, or your feelings, even!"
    m "Shout until you feel calmer."
    m "We can take care of your throat later! Ahahaha~!"
   
#19
    m "Let's try to listen to some music?"
    m "Even better if it's music that expresses how you feel."
    m "It can be VERY loudly if you want."
    m "You can use your headphones to blast some songs, or even use no headphones at all."
    m "Screaming with the lyrics might be therapeutic too!"
    m "Or even walking fast along the song."
    m "Oh, i thought of something nice to do also."
    m "Dance to the music!"
    m "Dance or move in a way that makes you express a feeling."
    
#20
    m "Do you have some paper nearby?"
    m "You could try crumpling it, to get out your anger or sad feelings."
    m "Way better than taking it out on yourself!"
    m "If you'd like, you can scribble on the paper until all your feelings fade away..."
    m "And then crumple it, or rip it up if you're angry."
    m "Drawing out how you are feeling and taking a deep breath every time you lift the pen/pencil off the paper might be nice too!"
    m "Or writing what's upsetting you."
    m "When drawing, you can put som estrong colours on paper and then gradually fade them."
    m "So they get lighter!"
    m "Dark green to light green, for example."
    m "Now, describe your strong emotions..." 
    m "And let them gradually fade away in the same way."
    m "You can even show someone your drawings and writings before ripping it to shreds."
    
#21
    m "Well, this one is a little different."
    m "Basically, it envolves someone else!"
    m "The creator of this mod, u/my-otter-self on Reddit, told me to remind you that she's always available to talk."
    m "You can DM her on Reddit, and she'll share her Discord information so you can talk about your feelings."
    m "She's has experience in psychology and can listen to you."
    m "Maybe even give some advice!"
    m "Take this opportunity to open youself a little, if you can."
    
#22
    m "Sometimes, paying attention to your senses can help."
    m "Could you put your hands in some cold water?"
    m "And remember, breathe a lot!"
    m "In... And out."
    m "Notice the coldness of the water witheach out breathe."
    
#23
    m "I want you to say out loud what's bothering you."
    m "You can whisper if you don't want anyone to hear you!"
    m "But I want you to pay attention to what you're saying."
    m "Can you come up with one positive solution?"
    m "Venting about how you feel always helps."
    m "If you can, write down any thoughts..."
    m "Get it all out of your system!"
    
#24
    m "You could start making a "positive statements about me" thought box."
    m "Creating a list of your strenghts, as thought you were compiling a portfolio or a CV..."
    m "That might help!"
    m "Write down as many positive things as you can about yourself."
    m "You can put each one of them in a jar..."
    m "And read them when you feel down!"
    m "I want you to realize how amazing you are, [player]."
    
#25 
    m "What about putting your upsetting thoughts in a box?"
    m "You can write them in slips of paper throughout the day, storing them in the box."
    m "At the end of the day, you can throw them away!"
    m "To have a new begginning tomorrow."
    m "I believe in you, [player]."
    
#26
    m "Let's do a little mental exercise!"
    m "Think about all the things you can find you share in common with a friend."
    m "That will help you remmember common ground!"
    m "You can write them down too."
    
#27
    m "Can you think about all the ways in which you can comfort a friend who might be having a bad time?"
    m "Please, note them down."
    m "Now, try to apply some of those strategies to yourself?"
    m "You can also note down how everything about this exercise makes you feel."
    
#28
    m "You can also go for a little walk outside, and connect with nature."
    m "Think about what you might be smelling, hearing and feeling."
    m "Can you put these feelings into words or draw them?"
    
#29
    m "Do you have any social media profiles, [player]?"
    m "You can write something positive there if you do."
    m "That way, you can make yourself feel better..."
    m "And spread the feeling to your friends too!"
    
#30
    m "Let's work on some perspective!"
    m "Can you write down your worries?"
    m "And think, how much will they bother you..."
    m "Tomorrow?"
    m "What about in a week's time?"
    m "Maybe a month or a year?"
    m "Working on using perspective helps on letting go of the intensity of the worry."
    
#31
    m "I know this one might be hard but..."
    m "What about trying to engage in a productive activity?"
    m "It's always nice when we see work getting done."
    m "Can be school stuff, a personal project... You name it!"
    m "Just try to do something that makes you proud for yourself today."
    m "Even if it's small!"
    
#32
    m "How about making a list of things you find interesting in people?"
    m "You can also list your favorite anime, videogame or other media's characters!"
    m "Think why you like them, and you can even imagine that they're real!"
    m "This can help cope with loneliness."
    
#33
    m "Do you have a mirror close to you, [player]?"
    m "You could try making faces at yourself in the mirror and laugh."
    m "I know that really cheers people up!"
    m "Seeing the silliness in youself is such a funny thing to do."
    m "Since you're there, you can also vent to yourself."
    m "Look inside your eyes, and know that there's nothing that compares to the beauty in them."
    
#34
    m "Time to get creative!"
    m "Make up a story in your head."
    m "It can be about anything and anyone positive in your life."
    m "Now ask yourself... Why are they in your story?"
    m "You can create two or more characters, and give them depth!"
    
#35
    m "Think about what is bothering you."
    m "Now imagine a river."
    m "Box up the thing that is on your mind and watch it float away..."
    m "Another great exercise is imagining a box... A big one!"
    m "You can imagine yourself putting all of your worries and problems inside it."
    m "After that, you can imagine yourself doing anything you want to the box."
    m "You can lock it, throw it away, throw it into the bottom of the sea..."
    m "You choose!"
    m "Just don't keep these feelings in an important place."
    m "Because they don't define you."
    
#36
    m "Make a list of positive feelings you have had in the last week!"
    m "I'm sure there are at least some."
    m "Find out what triggers those emotions..."
    m "And make sure to cherish those situations!"
    
#37
    m "This technique is one of my favorites."
    m "Let's write a poem!"
    m "Don't be alarmed, [player]."
    m "It doesn't have to rhyme!"
    m "It can be a short poem about how you feel."
    m "I'm sure it will be sincere!"
    m "If you don't feel ready to write a poem of your own..."
    m "You can always read some from famous poets!"

#38
    m "Alright, baby."
    m "I want you to try the 4-7-8 breathing exercise!..."
    m "You can also develop a personal mantra and repeat it along with the exercise."
    m "First of all, please straighten your back."
    m "Once you become familiar with this breathing exercise, you can perform it while lying in bed too!"
    m "Place and keep the tip of your tongue against the ridge of tissue behind your upper front teeth for the duration of the exercise."
    m "Completely exhale through your mouth, making a {i}woosh{/i} sound."
    m "Close your mouth and inhale quietly through your nose to a mental count of four."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Hold your breath for a count of seven."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Exhale completely through your mouth, making a {i}woosh{/i} sound to a count of eight."
    m "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m "Aaaand, you're done!"
    
#39 
    m "[player], do you have a Pinterest?"
    m "You can try adding some inspirational quotes to your board!"
    m "Or some pictures you find aesthetically pleasing."
    m "If you don't have an account, maybe you can try creating one?"
    m "I promise it's very satisfying!"
    
#40
