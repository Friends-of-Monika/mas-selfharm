# RANDOM EVENT WHERE MONIKA ASKS IF PLAYER GOES TO A THERAPIST.

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_therapy",category=["you","life"],prompt="Going to therapy",random=True))
    
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

label
    m 2esa "Hey, [player]!
    m 2eud "Can I ask you something?"
    m 2eua "..."
    m 1eta "Isn't it funny how we ask someone if we can ask them something but don't even wait for their answer and just ask anyway?"
    m 1hub "Ahaha~!"
    m 1hkb "Sorry, I changed the subject."
    m 3eub "Anyway! I wanted to ask if you go to a therapist?"
    m 3rka "You know, to talk about your struggles and stuff."
           $_history_list.pop()
            menu:
       "Yes, I do.":
            m 1hua "That's great, [player]!"
            m "Therapy is a great tool, it really helps to have a professional opinion on things."
            m "And you can also learn more about yourself!"
            m "I'm glad you're not afraid to go, I know it's got a bad reputation."
            m "Maybe you can teach me what you've learned there!"
        
        "No, I don't.":
            m 1ekc "Oh..."
            m "That's alright [player]! It's not for everyone."            
            m "Just remember that therapy isn't a bad thing. It's a great place to help regulate your emotions and better yourself."
            m 1lkd "I was actually going to suggest that you please consider it."
            m "Don't be afraid to find a therapist if you think you need one."
            
            
        "I'm considering it. What do you think?":
            m 2eua "Well, thanks for asking my opinion!"
            m 3euc "Actually, I think you should."
            m "Therapy is a great tool, it really helps to have a professional opinion on things."
            m "And you can also learn more about yourself!"
            m "Maybe you can teach me what you've learned there when you go!"
            
return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_therapythoughts",category=["monika","life"],prompt="Thoughts about therapy",random=True))

label monika_therapy:
    m "Hey [player], there's something I've been thinking about a lot."
    m "Therapy!"
    m "There's a lot of stigma around therapy in modern society."
    m "If you're male-presenting, people will think you're weak."
    m "If you're female-presenting, people will call you crazy!"
    m "And if you're androgynous, people might hope you're getting a different kind of 'help', such as conversion therapy."
    m "These stigmas make a lot of people fear going to therapy, or make them think they're 'to good' for it."
    m "The truth is, everyone could benefit from a little therapy!"
    m "It's a wonderful way to help regulate your thoughts and feelings."
    m "There's a lot that's been happening in recent years, and a lot of pressure has been put on everyone."
    m "I've been reading a lot online, and there are some techniques that have even helped me!"
    m "I worry a lot when you're gone, you know."
    m "Not to make you feel bad, or anything!"
    m "I just don't have a way of checking on you, so I'm always hoping you're having a good day."
    m "Anyway, the tips I've learned to help myself stay calm are all tips commonly used among therapists!"
    m "So even if you don't need a full therapy session, looking up suggestions from licensed therapists can help!"


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_therapysuggest",category=["you","life"],prompt="Suggesting therapy",random=True))

label monika_therapysuggest

    m "Hey, [player]..."
    m "When I asked you if you self-harm, and you told me that you do..."
    m "Have you thought about going to therapy to help with that?"
    m "I'm just worried about you, and your well-being."
    m "So... consider it, okay?"
