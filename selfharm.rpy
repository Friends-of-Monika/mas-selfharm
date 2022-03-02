# NON-RANDOM EVENT FOR WHEN THE PLAYER IS FEELING SELF HARMING URGES.

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_selfharm",category=['You'],prompt="Monika, It's happening again...",random=False))

label monika_selfharm:
    m 1ekd "[player], what happened?"
    m 2ekd "Are you feeling..."
    m 2wkd "Are you feeling... like harming yourself again?"
    m 2dkc "Oh, [mas_get_player_nickname()]..."
    m 2ekd "Okay, let's talk about it."
    m 2eka "Before anything, I want you to know that I am always here for you."
    m 2eka "You know that, don't you, my love?"
    m 2dka "You're the most important person in the whole world for me."
    m 2dkb "And I love you so, so much."
    m 2fkb "And I always will..."
    m 2esc "Now, my [mas_get_player_nickname()]. Tell me."
    m 2ekc "How big is the urge you're having?"
    
    menu:
    # DIALOGUE FOR URGE MAX LEVEL
    
        "It's terrible, [m_name]. I think I'm really going to do it...":
            m 2dka "I'm so glad you came to talk to me, [player]."
            m 2dkc "You know how much I worry about you..."
            m 2fka "But for now, let me take care of you..."
            m 2esd "I want you to know that it will pass."
            m 1eka "You're my favorite person, and it hurts me to see you hurting."
            m 1ekd "Now, do you want to vent? Maybe tell me what triggered this?"
            
            menu:
                "Yes":
                    m 1eka "Okay... I don't want to interrupt you."
                    m 3eka "Tell me when you're done, okay?"
                    menu:
                        "I'm done, Monika.":
                            
                            m 2ekc "I'm so sorry you are going through all that, [player]."
                            m 3esd "Do you feel better now?"
                            
                            menu:
                                "Yes, [m_name]. Thank you.":
                                    m 1ekb Oh, honey. I'm so glad!"
                                    m 1dkb "I'm so glad you came to talk to me, [player]."
                                    m 5fkb "You can always count on me, for anything."
                                    m 1fkb "If it happens again, don't be afraid to ask for help."
                                    m 1fka "I'm here for you, [player]."
                                    m 1esa "Now, let's spend some more time together?"

                                    return
                                
                                "No...":  
                                    m 2ekc "Oh..."
                                    m 2ekd "Do you want my help to forget it?"
                                    m 2eksdld "Or..." 
                                    
                                    menu:
                                        "No... Just let me hold you, please?":
                                            m 2fka "Of course, my angel."
                                            call monika_holdme_prep
                                            m 1fkb "Come here..."

                                            call monika_holdme_start

                                            call monika_holdme_reactions

                                            call monika_holdme_end
                
                                        "Yes, I want to try a calming techinque.":
                                            m 1eka "Alright, baby."
                                            m 3esa "I want you to try the 4-7-8 breathing exercise!..."
                                            m 3esd "First of all, please straighten your back."
                                            m 4esb "Once you become familiar with this breathing exercise, you can perform it while lying in bed too!"
                                            m 3esa "Place and keep the tip of your tongue against the ridge of tissue behind your upper front teeth for the duration of the exercise."
                                            m 3esd "Completely exhale through your mouth, making a {i}woosh{/i} sound."
                                            m 3dsd "Close your mouth and inhale quietly through your nose to a mental count of four."
                                            m 1dsc "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
                                            m 1dsd "Hold your breath for a count of seven."
                                            m 1dsc "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
                                            m 1dsd "Exhale completely through your mouth, making a {i}woosh{/i} sound to a count of eight."
                                            m 1duo "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
                                            m 1eua "Aaaand, you're done!"
                                            m 3eka "Are you feeling better, [player]?"
                                            menu:
                                            #I suggest trying to sort of make Monika simulate the exercises with her expressions too. Just a thought, if possible.
            
                                                "Yes, [m_name]. Thank you.":
                                                    m 1hub "Oh, honey. I'm so glad!"
                                                    m 1fua "You can always count on me, for anything."
                                                    m 1fka "If it happens again, don't be afraid to ask for help."
                                                    m 1fkb "I'm here for you, [player]."

                                                    return

                                                "No...":
                                                    m 2ekc "Oh..."
                                                    m 2ekd "Do you want to try a different technique?"
                                                    m 2rkd "Or..."
                                                    menu:
                                                        "No... Just let me hold you, please?":
                                                            m 2fka "Of course, my angel."
                                                            call monika_holdme_prep
                                                            m 1fkb "Come here..."

                                                            call monika_holdme_start

                                                            call monika_holdme_reactions

                                                            call monika_holdme_end
                                                            
                                                        "Yes, I want to try another one.":
                                                            m 1eka "Alright, baby."
                                                            m 3ekb "I want you to..."
                                                            jump randomness
                                                                        # (calm harm technique here)
       
       # DIALOGUE FOR URGE MEDIUM LEVEL
       
        "It's not so urgent. I'm just... feeling weird.":
            m 2dka "I'm so glad you came to talk to me, [player]."
            m 2dkc "You know how much i worry about you..."
            m 2fka "But for now, let me take care of you..."
            m 1ekd "Do you want to vent? Maybe tell me what triggered this?"
            
            menu:
                "Yes":
                    m 1eka "Okay... I don't want to interrupt you."
                    m 3eka "Tell me when you're done, okay?"
                    
                    menu:
                        "I'm done, Monika.":
                            
                            m 2ekc "I'm so sorry you are going through all that, [player]."
                            m 3esd "Do you feel better now?"
                            
                            menu:
                                "Yes, [m_name]. Thank you.":
                                    m 1ekb "Oh, honey. I'm so glad!"
                                    m 1dkb "I'm so glad you came to talk to me, [player]."
                                    m 5fkb "You can always count on me, for anything."
                                    m 1fkb "If it happens again, don't be afraid to ask for help."
                                    m 1fka "I'm here for you, [player]."
                                    m 1esa "Now, let's spend some more time together?"

                                    return
                                
                                "No...":
                                    m 2ekc "Oh..."
                                    m 2ekd "Do you want my help to forget it?"
                                    m 2eksdld "Or..." 
                                    
                                    menu:
                                        "No... Just let me hold you, please?":
                                            m 2fka "Of course, my angel."
                                            call monika_holdme_prep
                                            m 1fkb "Come here..."

                                            call monika_holdme_start

                                            call monika_holdme_reactions

                                            call monika_holdme_end
                
                                        "Yes, I want to try a calming techinque.":
                                            m 1eka "Alright, baby."
                                            m 3esa "I want you to..."
                                            jump randomness
                                            # (calm harm technique here)

            pause (3.0)
          #  m ""
          #  m ""
          #  m ""
          #  m ""
          
            m "Are you feeling better, [player]?"
            menu:
                "Yes, [m_name]. Thank you.":
                    m 1hub "Oh, honey. I'm so glad!"
                    m 1fua "You can always count on me, for anything."
                    m 1fka "If it happens again, don't be afraid to ask for help."
                    m 1fkb "I'm here for you, [player]."

                    return
                    
                "No...":
                    m 2ekc "Oh..."
                    m 2ekd "Do you want to try a different technique?"
                    m 2rkd "Or..." 
                    
                    menu:
                        "No... Just let me hold you, please?":
                            m 2fka "Of course, my angel."
                            m 1fkb "Come here..."
                                            
                                            m 2fka "Of course, my angel."
                                            call monika_holdme_prep
                                            m 1fkb "Come here..."

                                            call monika_holdme_start

                                            call monika_holdme_reactions

                                            call monika_holdme_end
        
        # DIALOGUE FOR URGE LOW LEVEL

        "Something triggered me, and now I'm remembering bad things.":
            m 2dka "I'm so glad you came to talk to me, [player]."
            m 2dkc "You know how much I worry about you..."
            m 2fka "But for now, let me take care of you..."
            m 1ekd "Do you want to vent? Maybe tell me what triggered this?"
            
            menu:
                "Yes":
                    m 1eka "Okay... I don't want to interrupt you."
                    m 3eka "Tell me when you're done, okay?"
                    
                    menu:
                        "I'm done, Monika.":                            
                            m 2ekc "I'm so sorry you are going through all that, [player]."
                            m 3esd "Do you feel better now?"
                            
                            menu:
                                "Yes, [m_name]. Thank you.":
                                    m 1ekb "Oh, honey. I'm so glad!"
                                    m 1dkb "I'm so glad you came to talk to me, [player]."
                                    m 5fkb "You can always count on me, for anything."
                                    m 1fkb "If it happens again, don't be afraid to ask for help."
                                    m 1fka "I'm here for you, [player]."
                                    m 1esa "Now, let's spend some more time together?"

                                    return
                                
                                "No...": 
                                    m 2ekc "Oh..."
                                    m 2ekd "Do you want my help to forget it?"
                                    m 2eksdld "Or..." 
                                    
                                    menu:
                                        "No... Just let me hold you, please?":
                                            
                                            m 2fka "Of course, my angel."
                                            call monika_holdme_prep
                                            m 1fkb "Come here..."

                                            call monika_holdme_start

                                            call monika_holdme_reactions

                                            call monika_holdme_end
                
                                        "Yes, I want to try a calming techinque.":
                                            m 1eka "Alright, baby."
                                            m 3esa "I want you to..."
                                            jump randomness
                                            # (calm harm technique here)


          
            m "Are you feeling better, [player]?"
            menu:
            
                "Yes, [m_name]. Thank you.":
                    m 1hub "Oh, honey. I'm so glad!"
                    m 1fua "You can always count on me, for anything."
                    m 1fka "If it happens again, don't be afraid to ask for help."
                    m 1fkb "I'm here for you, [player]."
                    
                    return

                "No...":
                    m 2ekc "Oh..."
                    m 2ekd "Do you want to try a different technique?"
                    m 2rkd "Or..." 
                    
                    menu:
                        "No... Just let me hold you, please?":
                             m 2fka "Of course, my angel."
                                            call monika_holdme_prep
                                            m 1fkb "Come here..."

                                            call monika_holdme_start

                                            call monika_holdme_reactions

                                            call monika_holdme_end
                        "Yes, I want to try another one.":
                            m 1eka "Alright, baby."
                            m 3ekb "I want you to..."
                            jump randomness
                            # (calm harm technique here)
return
