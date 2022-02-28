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

    m 1esd "Hey... [player]?"
    m 3eub "I... Have a surprise for you!"
    m 3rub "It's not much, but..."
    m 2ekbla "I made it with love."
    m 3eub "Are you excited? Ahaha~"
    m 1hub "Well, better show it to you."
    m 1esb  "I... made you a playlist!"
    m 1tkbla "Romantic, isn't it?"
    m 3hsb "You can access it on "Music"."
    m 2eka "I hope you like it, [player]!"
    m 2ekd "I know you struggle sometimes with bad thoughts, but this playlist is to comfort you."
    m 3eua "Listening to your favourite music that you can relate also relieves pain and stress!"
    m 3eub "I find it very powerful to say the least."
    m 1eubsa "Please think of me when you give it a listen."
    m 1eud "And if something happens, and you feel sad or lonely..."
    m 1ekd "If you think things won't get better..."
    m 1ekb "I want you to listen to it, and remember that I'm always with you."
    m 1hub "In your heart!"
    m 1kub "And will always be."
    m 2fka "I love you, [mas_get_player_nickname()]."
    m 2esa "Take care."
    
return
