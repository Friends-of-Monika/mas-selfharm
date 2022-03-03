# FIRST-AID DIALOGUE

#RANDOM EVENT, SELF-HARM TRUE, MAKES FIRST AID DIALOGUE AVAILABLE

    m "I know you said you've injured yourself before, [player]..."
    m "It really left me heart-broken, because I really want the best for you."
    m "So, I decided to give you some insteuctions if you ever do it in the future..."
    m "And can't have medical attention."
    m "It's a basic first-aid guide. For cuts, specifically."
    m "If you need it, make sure to let me know, okay?"
    m "I'll do my best to help."
    
#FIRST AID NON-RANDOM DIALOGUE

    m "You need first aid help, [player]?"
    m "I'm so sorry, [mas_get_player_nickname()]."
    m "Does it hurt much?"
    m "It hurts me too..."
    m "When you bleed, my heart bleeds..."
    m "But let's get to it."
    m "First aid is all about timing, the faster we tend to your wounds, better the recovery!"
    m "I'll do step by step process on how to treat your wounds."
    m "Remember, this is spesifically about cuts!"
    m "Let me get started..."
    m "Firstly, you will need to stop the bleeding."
    m "You should apply constant pressure to the area using a clean and dry absorbent material."
    m "A bandage, towel or handkerchief. For approximately 10 minutes."
    m "It's Important to raise the injury above the level of your heart."
    m "I can make a timer for you."
    # timer here?
    m "All done, [player]!"
    m "Ready for the next step?"
        menu:
            "Yes":
                m "Okay!"
                m "Secondly, You need to clean your wound."
                m "Start by washing and drying your hands thoroughly..."
                m "Then clean the wound under tap water or with an alcohol free solution."
                m "Make sure you don't use no alcohol or hydrogen peroxide!"
                m "As it may damage the skin and slow healing..."
                m "And we don't want that!"
                m "I'll wait for you to do that, [player]."
                m "Just tell me when you're done, okay?"
                    menu:
                        "I'm done, Monika."
                            m "Okay!"
                            m "Thirdly and lastly, it's really important to apply a dressing."
                            m "You can use many different types.."
                            m "Adhesives ones like plasters, non-adhesive compresses with a bandage." 
                            m "They can be small or big, waterproof, different shapes and so on."
                            m "Whatever feels best and it's available at home!"
                            m "It has to be comfortable, since the wrong plaster can hurt your skin."
                            m "Keep the dressing clean by changing it as often as necessary!"
                            m "You can remove the dressing, once the wound has closed itself."
                            m "Always pay attention to signs of infection!"
                            m "Such as fever, swollen wounds, pus, or any significant or worsening swelling, redness and pain."
                            m "If you notice any of those..."
                            m "You need to get medical attention and soon as possible."
                            m "Another reasons of need to go an emergency response unit are the following:"
                            m "If the bleeding hasn’t stopped after 10 minutes of continuous pressure."
                            m "If you're bleeding from an artery, you'll notice the blood gushing out at your heartbeat."
                            m "Also, if there's something stuck in the wound."
                            m "If it's a long or deep wound..."
                            m "Or if the edges are split after pressure or you can see underlying structures like fat or muscle."
                            m "If that's the case, you probably need stitches."
                            m "..."
                            m "Well, that's all there's to it, [Player]!"
                            m "I hope it helps you incase you need it."
                            m "Which I hope it won't happen again..."
                            m "If it does, just let me know and I'll repeat those steps. Okay?"
                            m "Take care, [player]."
                            m "You know how much I love you!"
