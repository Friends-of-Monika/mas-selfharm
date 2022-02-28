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

    m 1lta "A diary, huh?"
    m 3eua "I've honestly been thinking about this for a bit."
    m 1huu "It can really be a great outlet for anyone's emotions!"
    m 5rub "You could write your innermost feelings and thoughts..."
    m 3esb "You can even share it with someone you truly trust!"
    m 1hsa "If you'd like, I can create a text file for you to write your thoughts into."
    m 1eua "Do you want me to create the diary for you?"
    menu:
        "Yes, please!":
            m 1hua "Great!"
            m 1nuu "I thought you would like that idea!"
            m 1dsc "..."
            play sound "sfx/glitch3.ogg" 
            python:
                try: renpy.file(config.basedir + "/diary.txt")
                except: open(config.basedir + "/diary.txt", "w").write("For my one and only love <3")
            pause(0.5)
            m 3esb "There you go!"
            m 1eua "It should be in the characters folder."

            return


        "No, thanks.":
            m 1eka "Oh, I see..."
            m 1hua "That's okay!"
            m 5eua "I just thought that it could be a neat idea."
            m 3hubsa "I always want what's best for you, [player]!"
            m 1fkbsu "I love you."

            return "love"

label diary3:
    
    m 1eta "Have you been writing in your diary?"
    m 2eku "I know it could be pretty personal stuff, so I haven't been looking."
    menu:
        "I accidentally deleted it.":
            m 1fuu "Oh... hehe! That's alright."
            m 1eua "Would you like me to make you another one?"
            menu:
                "Sure!":
                    m 1hub "Alright!"
                    m 1dsc "..."
                    play sound "sfx/glitch3.ogg" 
                    python:
                        try: renpy.file(config.basedir + "/diary2.txt")
                        except: open(config.basedir + "/diary2.txt", "w").write("Don't lose this one, hehe~")
                    pause(0.5)
                    m 3nuu "Don't delete this one [player]!"

                    return
        

        "Yeah, I've been working on it!":
            m 1hub "I'm happy to hear that, [player]!"
            m 5sub "It's so nice to hear you're taking my advice."
            m 1hub"I love you!"

            return "love"
