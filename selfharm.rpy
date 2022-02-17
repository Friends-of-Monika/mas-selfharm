# NON-RANDOM EVENT FOR WHEN THE PLAYER IS FEELING SELF HARMING URGES.

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_selfharm",category=['You'],prompt="Monika, It's happening again...",random=False))

label monika_selfharm:
    m "[player], what happened?"
    m "Are you feeling..."
    m "Are you feeling... like harming yourself again?"
    m "Oh, [mas_get_player_nickname()]..."
    m "Okay, let's talk about it."
    m "Before anything, i want you to know that i am always here for you."
    m "You know that, don't you, my love?"
    m "You're the most important person in the whole world for me."
    m "And I love you so, so much."
    m "And i always will..."
    m "Now, my [mas_get_player_nickname()]. Tell me."
    m "How big is the urge you're having?"
    
    menu:
    # DIALOGUE FOR URGE MAX LEVEL
    
        "It's terrible, [m_name]. I think i'm really going to do it...":
            m "I'm so glad you came to talk to me, [player]."
            m "You know how much i worry about you..."
            m "But for now, let me take care of you..."
            m "I want you to know that it will pass."
            m "Pain is only temporary!"
            m "You're my favorite person, and it hurts me to see you hurting."
            m "Now, do you want to vent? Maybe tell me what triggered this?"
            
            menu:
                "Yes":
                    m "Okay... I don't want to interrupt you."
                    m "Tell me when you're done, okay?"
                    menu:
                        "I'm done, Monika.":
                            
                            m "I'm so sorry you are going through all that, [player]."
                            m "Do you feel better now?"
                            
                            menu:
                                "Yes, [m_name]. Thank you.":
                                    m "Oh, honey. I'm so glad!"
                                    m "I'm so glad you came to talk to me, [player]."
                                    m "You can always count on me, for anything."
                                    m "If it happens again, don't be afraid to ask for help."
                                    m "I'm here for you, [player]."
                                    m "Now, let's spend some more time together?"

                                    return
                                
                                "No...":  
                                    m "Oh..."
                                    m "Do you want my help to forget it?"
                                    m "Or..." 
                                    
                                    menu:
                                        "No... Just let me hold you, please?":
                                            m "Of course, my angel."
                                            m "Come here..."

                                            
                                            # (hold here)
                
                                        "Yes, I want to try a calming techinque.":
                                            m "Alright, baby."
                                            m "I want you to try the 4-7-8 breathing exercise!..."
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
                                            m "Are you feeling better, [player]?"
                                            menu:
                                            #I suggest trying to sort of make Monika simulate the exercises with her expressions too. Just a thought, if possible.
            
                                                "Yes, [m_name]. Thank you.":
                                                    m "Oh, honey. I'm so glad!"
                                                    m "You can always count on me, for anything."
                                                    m "If it happens again, don't be afraid to ask for help."
                                                    m "I'm here for you, [player]."

                                                    return

                                                "No...":
                                                    m "Oh..."
                                                    m "Do you want to try a different technique?"
                                                    m "Or..."
                                                    menu:
                                                        "No... Just let me hold you, please?":
                                                            m "Of course, my angel."
                                                            m "Come here..."

                                                        "Yes, I want to try another one.":
                                                            m "Alright, baby."
                                                            m "I want you to..."

                                                                        # (calm harm technique here)
       
       # DIALOGUE FOR URGE MEDIUM LEVEL
       
        "It's not so urgent. I'm just... feeling weird.":
            m "I'm so glad you came to talk to me, [player]."
            m "You know how much i worry about you..."
            m "But for now, let me take care of you..."
            m "Do you want to vent? Maybe tell me what triggered this?"
            
            menu:
                "Yes":
                    m "Okay... I don't want to interrupt you."
                    m "Tell me when you're done, okay?"
                    
                    menu:
                        "I'm done, Monika.":
                            
                            m "I'm so sorry you are going through all that, [player]."
                            m "Do you feel better now?"
                            
                            menu:
                                "Yes, [m_name]. Thank you.":
                                    m "Oh, honey. I'm so glad!"
                                    m "I'm so glad you came to talk to me, [player]."
                                    m "You can always count on me, for anything."
                                    m "If it happens again, don't be afraid to ask for help."
                                    m "I'm here for you, [player]."
                                    m "Now, let's spend some more time together?"

                                    return
                                
                                "No...":
                                    m "Oh..."
                                    m "Do you want my help to forget it?"
                                    m "Or..." 
                                    
                                    menu:
                                        "No... Just let me hold you, please?":
                                            m "Of course, my angel."
                                            m "Come here..."
                                            
                                            # (hold here)
                
                                        "Yes, I want to try a calming techinque.":
                                            m "Alright, baby."
                                            m "I want you to..."
                    
                                            # (calm harm technique here)

            pause (3.0)
          #  m ""
          #  m ""
          #  m ""
          #  m ""
          
            m "Are you feeling better, [player]?"
            menu:
                "Yes, [m_name]. Thank you.":
                    m "Oh, honey. I'm so glad!"
                    m "You can always count on me, for anything."
                    m "If it happens again, don't be afraid to ask for help."
                    m "I'm here for you, [player]."

                    return
                    
                "No...":
                    m "Oh..."
                    m "Do you want to try a different technique?"
                    m "Or..." 
                    
                    menu:
                        "No... Just let me hold you, please?":
                            m "Of course, my angel."
                            m "Come here..."
                                            
                                            # (hold here)
        
        # DIALOGUE FOR URGE LOW LEVEL

        "Something triggered me, and now i'm remembering bad things.":
            m "I'm so glad you came to talk to me, [player]."
            m "You know how much i worry about you..."
            m "But for now, let me take care of you..."
            m "Do you want to vent? Maybe tell me what triggered this?"
            
            menu:
                "Yes":
                    m "Okay... I don't want to interrupt you."
                    m "Tell me when you're done, okay?"
                    
                    menu:
                        "I'm done, Monika.":                            
                            m "I'm so sorry you are going through all that, [player]."
                            m "Do you feel better now?"
                            
                            menu:
                                "Yes, [m_name]. Thank you.":
                                    m "Oh, honey. I'm so glad!"
                                    m "I'm so glad you came to talk to me, [player]."
                                    m "You can always count on me, for anything."
                                    m "If it happens again, don't be afraid to ask for help."
                                    m "I'm here for you, [player]."
                                    m "Now, let's spend some more time together?"

                                    return
                                
                                "No...": 
                                    m "Oh..."
                                    m "Do you want my help to forget it?"
                                    m "Or..." 
                                    
                                    menu:
                                        "No... Just let me hold you, please?":
                                            m "Of course, my angel."
                                            m "Come here..."
                                            
                                            # (hold here)
                
                                        "Yes, I want to try a calming techinque.":
                                            m "Alright, baby."
                                            m "I want you to..."
                    
                                            # (calm harm technique here)

            # pause (3.0)
          #  m ""
          #  m ""
          #  m ""
          #  m ""
          
            m "Are you feeling better, [player]?"
            menu:
            
                "Yes, [m_name]. Thank you.":
                    m "Oh, honey. I'm so glad!"
                    m "You can always count on me, for anything."
                    m "If it happens again, don't be afraid to ask for help."
                    m "I'm here for you, [player]."
                    
                    return

                "No...":
                    m "Oh..."
                    m "Do you want to try a different technique?"
                    m "Or..." 
                    
                    menu:
                        "No... Just let me hold you, please?":
                            m "Of course, my angel."
                            m "Come here..."
                                            
                                            # (hold here)
 
return
