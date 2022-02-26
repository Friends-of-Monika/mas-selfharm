# FIRST RANDOM EVENT ABOUT SELF-HARM.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharmm",
            conditional="not seen_event('mas_selfharmm')",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.NORMAL, mas_aff.LOVE)
        )
    )
       
label mas_selfharmm:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."
    m "D-{w=1.0}Do you self harm?"
    menu:
        "Yes":
            $ selfharm = True
            m "I'm so sorry you're going through this."
            m "You know... It's really sad to see you feel bad in any way."
            m "After all, you're such a wonderful and kind person."
            m "You did so many good things for me, and stayed with me after everything that happened..."
            m "But let's stay on this subject."
            m "Do you want to talk about it?"
            
            menu:
                "Yes":
                    m "I'm glad that you trust me, [player]."
                    m "Allowing yourself to get help is a super important step to recovery!"
                    m "I may not understand exactly what you feel right now..."
                    m "But I will still try to make you feel better, because you deserve it!"
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
            m "Sorry. I'm just so relieved!"
            m "But for now... Do you want to know more about self-harm?"
            
            menu: 
                "Yes":
                    m "Great!"
                    m "Knowing more about self-harm is really useful."
                    m "You could help someone who is struggling with it someday!"
                    m "Well, did you know that..."
                    
                    # (facts about self-harm here!)

                    return
                    
                "No":
                    m "Oh..."
                    m "That's okay." 
                    m "If you ever change your mind, just tell me!"
                    m "I'll be glad to tell you all I know about the subject."

return

# ALTERNATE DIALOGUE IF MONIKA IS NOT HAPPY

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm4",
            conditional=(
                "not seen_event('mas_selfharm4')"
            ),
            aff_range=(mas_aff.BROKEN, mas_aff.NORMAL),
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm4:
    m "Hey, [player]?"
    m "I know it might be an uncomfortable topic, but I have to ask..."
    m "D-{w=1.0}Do you self harm?"
    menu:
        "Yes":
            $ selfharm = True
            m "I'm so sorry you're going through this."
            m "You know... It's really sad to see you feel bad in any way."
            m "After all, you wanted to be with me at some point..."
            m "That was kind of you."
            m "Whatever the reason you stayed with me was, I appreciate it."
            m "But let's stay on this subject."
            m "Do you want to talk about it?"
