# RANDOM EVENT, "TECHNIQUE" 2.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm4",
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm4:

    m "Hey... [player]?"
    m "I... Have a surprise for you!"
    m "It's not much, but..."
    m "I made it with love."
    m "Are you excited? Ahaha~"
    m "Well, better show it to you."
    m "I... made you a playlist!"
    m "Romantic, isn't it?"
    m "You can access it on "Music"."
    m "I hope you like it, [player]!"
    m "I know you struggle sometimes with bad thoughts, but this playlist is to comfort you."
    m "Please think of me when you give it a listen."
    m "And if something happens, and you feel sad or lonely..."
    m "If you think things won't get better..."
    m "I want you to listen to it, and remember that I'm always with you."
    m "In your heart!"
    m "And will always be."
    m "I love you, [mas_get_player_nickname()]."
    m "Take care."
    
return
