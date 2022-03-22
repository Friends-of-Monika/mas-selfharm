# RANDOM SAD/WORRIED MONIKA #1.

default persistent._msh_mod_pm_did_selfharm = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_selfharm5",
            action=EV_ACT_QUEUE
        )
    )

label mas_selfharm5:

    m 5ekc "Hey... [player]?"
    m 5gkd "You probably remember when we were talking about self-harm..."
    m 3ektpc "I never forget when you told me about that, it honestly broke my heart."
    m 2ektdc "I have never felt so strongly towards anyone, and... well..."
    m 6dktsd "The thought of losing you..."
    m 6wktso "I- Well- That makes me feel sick to my stomach!"
    m 5dktdx "...I'm sorry, [mas_get_player_nickname()]."
    m 1ektdc "Please don't forget how much I care about you."
    m 2mktpd "And please, don't leave me..."
    m 2fkd "I can't stand the thought of you wanting to hurt yourself!"
    m 4fkc "I truly want nothing more than your happiness."
    m 1dfx "I feel so angry and disheartened that I'm limited to what I can do for you in this reality!"
    m 4sfu "But no matter what, I'm determined to try my best and make you feel better!"
    m 3esa "I'm always willing to try to help you, [player]..."
    m 1hsa "Like you helped me by installing this mod!"
    m 1lst "I know it's hard for you, not many people are willing to listen or understand..."
    m 5fku "But I hope venting to me helped you at least a bit."
    m 3eua "Also, maybe try talking about your feelings to a friend, or family!"
    m 1hua "I know it's hard to be open about your problems, but they care about you."
    m 1eub "They don't want you to get hurt, I'm sure!"
    m 2fka "I don't want to lose you, [player]. You're all I have left..."
    m 5hub "My only wish is to be with you forever!"
    m 1dsb "To finally be with you, to help you conquer all of your dreams, and forget all of your problems..."
    m 1eka "To shield you from these painful thoughts."
    m 5hubsa "I love you, [mas_get_player_nickname()]."
     
return "love"
