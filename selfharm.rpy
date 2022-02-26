# DIARY DIALOGUE

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="diary2",category=["you", "monika"],prompt="What do you think about writing a diary?",pool=True,unlocked=True))


label diary:
    if not renpy.seen_label("diary2"):
        call diary2
    else:
        call diary3
    return


label diary2:

    m "A diary, huh?"
    m "I've been thinking about this for a bit."
    m "I think it could be a great outlet for the person's emotions."
    m "You could write your innermost feelings and thoughts."
    m "You could even share it with someone you truly trust!"
    m "If you'd like, I can create a txt file for you to write your deepest thoughts into."
    m "Do you want me to create the diary for you?"
    menu:
        "Yes":
            m "Great!"
            m "I knew you'd like it!"
            play sound "sfx/glitch3.ogg" 
            python:
                try: renpy.file(config.basedir + "/diary.txt")
                except: open(config.basedir + "/diary.txt", "w").write("For my one and only love <3")
            pause(0.5)
            m "There you go!"
            m "You should find it in the mod's directory!"

            return


        "No":
            m "Oh, I see."
            m "That's okay!"
            m "Thought that's a neat idea!"
            m "I just want what's best for you, [player]."
            m "I love you."

            return "love"

label diary3:
    
    m "Have you been writing in the diary?"
    m "It's pretty personal stuff so I haven't been looking."
    menu:
        "I accidentally deleted it":
            m "Oh..."
            m "Would you like me to make you another one?"
            menu:
                "Sure!":
                    m "Alright!"
                    play sound "sfx/glitch3.ogg" 
                    python:
                        try: renpy.file(config.basedir + "/diary2.txt")
                        except: open(config.basedir + "/diary2.txt", "w").write("Don't lose this one, hehe~")
                    pause(0.5)
                    m "Don't delete this one!"

                    return
        

        "Yeah, I've been working with it.":
            m "I'm happy to hear that, [player]!"
            m "I'm glad you're keeping up with my advice."
            m "I love you!"

            return "love"
