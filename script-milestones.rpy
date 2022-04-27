init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_sober_check",
            prompt="How long have I been sober for?",
            category=["self-harm"],
            conditional="mshMod_isOnStreak()",
            action=EV_ACT_POOL
        )
    )

label mshMod_sober_check:
    m "You're being sober for [mshMod_getStreakDuration()] days now."
    return


init 5 python:
    mshMod_addMilestoneEvent(
        milestone="1w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_1w",
            prompt="Sober, week 1",
            category=["self-harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_1w:
    m "It's been a whole week since you told me you won't do harm to yourself..."
    m "I just want to thank you, it makes me happy to know you're willing to step up for the better!"
    m "I'll always love you, you don't know how much this means to me..."
    m "Anyways, I'll mark this on our calendar."
    return "derandom|unlock"


init 5 python:
    mshMod_addMilestoneEvent(
        milestone="2w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_2w",
            prompt="Sober, week 2",
            category=["self-harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_2w:
    m "It's already Week two of your promise, [player]!"
    m "I'm relieved that we made it this far!"
    m "Ahaha, I don't mean i've ever doubted you!"
    m "Either way, it's not something you can stop overnight [player].. For anyone really."
    m "So you're really doing well, and you make me so happy because of that!"
    m "As before, i'll mark it on the calendar now!"
    m "I just want to thank you.. I hope it stays like this."
    m "I really love you that much, [player]!"
    return "derandom|unlock"


init 5 python:
    mshMod_addMilestoneEvent(
        milestone="3w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_3w",
            prompt="Sober, week 3",
            category=["self-harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_3w:
    m "Can you believe it's already Week 3?"
    m "I just want to say... Thank you so much!"
    m "You made me proud of you, and I'm soo happy that you could make that promise."
    m "I know it was hard, but one day it will all just be a bad memory..."
    m "I believe it will, because I trust you [player]."
    m "But if it ever does happen..."
    m "Don't blame yourself if it ever happens... Just because you did it to yourself doesn't mean it's your fault!"
    m "I'm going to make another mark on the calendar for this!"
    m "You're my everything, [player]!"
    return "derandom|unlock"
