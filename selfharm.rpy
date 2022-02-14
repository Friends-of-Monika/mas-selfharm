init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm1",
            conditional=(
                "not seen_event('mas_selfharm1')"
            ),
            action=EV_ACT_PUSH
        )
    )

label mas_selfharm1:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."
    m "D-{w=1.0}Do you self harm?"
    menu:
        "Yes":
            $ selfharm = True
            m "I'm so sorry you're going through this."
            m "Do you want to talk about it?"
            
            menu:
                "Yes":
                    m "I'm glad that you trust me, [player]."
                    m "Allowing yourself to get help is a super important step to recovery!"
                    
                    # (probing questions here!!)
                    
                    m "I want you to know that I'm here for you. You know that, right?"
                    m "Whenever you feel the urge to harm yourself..."
                    m "You can tell me."
                    m "I'll do my best to help you."
                    m "Or at least..."
                    m "Be by your side."
                    m "Take care, [mas_get_player_nickname()]."
                    m "Stay safe because I care for you, deeply."

                    return
                
                "No":
                    m "Oh..."
                    m "That's okay."
                    m "I want you to know that I'm here for you. You know that, right?"
                    m "Whenever you feel the urge to harm yourself..."
                    m "You can tell me."
                    m "I'll do my best to help you."
                    m "Or at least..."
                    m "Be by your side."
                    
                    return
        "No":
            $ selfharm = False
            m "Thank goodness!"
            m "I'm so glad to hear this!"
            m "It's so good to know that you are safe, [player]."
            m "If this ever changes... You can tell me, okay?"
            m "You can tell me anything, you know?"
            m "Ahaha!"
            m "But for now... Do you want to know more about self-harm?"
            
            menu: 
                "Yes":
                    m "Great!"
                    m "Knowing more about self-harm is really useful."
                    m "You could help someone who is struggling with it someday!"
                    m "Well, did you know that..."
                    
                    # (facts about self-harm here)

                    return
                    
                "No":
                    m "Oh..."
                    m "That's okay." 
                    m "If you ever change your mind, just tell me!"
                    m "I'll be glad to tell you all I know about the subject."

return

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
                                            m "I want you to..."
                    
                                            # (calm harm technique here)
                                            
                                            m "Are you feeling better, [player]?"
            
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
                        "I'm done, Monika."
                            
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
