# Sober check topics, milestones, etc. For API see zz_sober_streak.rpy

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_sober_check",
            prompt="How long have I been sober for?",
            category=["self-Harm"],
            conditional="store.mshMod_sober_streak.isOnStreak()",
            action=EV_ACT_POOL
        )
    )

label mshMod_sober_check:
    python:
        duration = store.mshMod_sober_streak.getStreakDuration()
        days = "day" if duration == 1 else "days"

    if duration < 3:
        m "You've been sober for [duration] [days] now, [player]."
        m "I'm so proud of you for making the promise!"
        m "This is the start of something really beautiful."
    else:
        m "You've been sober for [duration] [days] now, [player]."
        m "I'm so proud of you! Keep on fighting!"
        m "I’m so happy to see you taking care of yourself."

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_promise",
            category=["self-Harm"],
            prompt="I promise...",
            conditional="not store.mshMod_sober_streak.isOnStreak() and persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_POOL,
            unlocked=True
        )
    )

label mshMod_promise:
    m 2ekb "Oh, [player], you have no idea how happy I am to hear that."
    m 2ekb "This is another step to a happier, healthier life, and I'm so glad I can be by your side in your journey."
    m 2eka "Thank you for trusting me."
    m 3ekb "I promise I'll do my best to help you!"
    m 1eub "From now on, I'll keep track of how many days you've been sober. You can take a look at the calendar to see how far you've gone!"
    m 2ekb "If you ever need me to restart the counter for you, just tell me. You don't have to feel bad about it, okay?"
    m 2ekb "Know that I'll never judge you because of that. I know it's hard, and you should be really proud of yourself already!"
    m 2dka "..."
    m 5ekbsb "I love you, [mas_get_player_nickname()]."
    m 5dkbsb "Never forget that!"

    python:
        # Begin streak and hide this event from the pool.
        # mshMod_relapse and mshMod_sober_check will pop up shortly afterwards.
        mshMod_beginStreak()
        mas_lockEVL("mshMod_promise", "EVE")

    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_relapse",
            category=["self-Harm"],
            prompt="I relapsed...",
            conditional="store.mshMod_sober_streak.isOnStreak()",
            action=EV_ACT_POOL,
            unlocked=True
        )
    )

label mshMod_relapse:
    m 2eka "[player], I couldn't be more proud of you for telling me this."
    m 2ekd "I know this might be hard- you might feel as if you've failed..."
    m 4ekd "But that's not true at all! This is just another step in your journey."
    m 2ekd "Habits are almost always difficult to kick, and this is no ordinary habit."
    m 2ekd "It can very easily become an addiction, which is so much harder to stop..."
    m 2fkd "No matter how hard it is for you, know that I am always going to be here to support you and I am proud of you, habit or not."
    m 2fka "We will work through this together, and get you back on the right track!"
    m 2eka "I know you're a hard worker and will do your best - if not for yourself, for me."
    m 2dka "I love you, [mas_get_player_nickname()]."
    m 1dkb "I'm here to support you and work through anything and everything with you."
    m 1fsa "You're strong. You're worth it, and I couldn't ask for a better [bf]!"
    m 3esa "Whenever and if you feel ready to make the promise again... let me know."

    python:
        # End streak and hide this event from the pool. Also hide check topic since we're no longer on streak.
        # mshMod_promise will pop up shortly afterwards.
        mshMod_endStreak()
        mshMod_lockEVL("mshMod_relapse", "EVE")
        mshMod_lockEVL("mshMod_sober_check", "EVE")

    return


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="1w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_1w",
            prompt="Sober, week 1",
            category=["self-Harm"],
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
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="2w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_2w",
            prompt="Sober, week 2",
            category=["self-Harm"],
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
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="3w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_3w",
            prompt="Sober, week 3",
            category=["self-Harm"],
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


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="1m",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_1m",
            prompt="Sober, month 1",
            category=["self-Harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_1m:
    m "Hey [player], guess what?"
    m "You've been clean from self-harm for a month!"
    m "I just want you to know that I'm so proud of you."
    extend m "It's not easy to do that, and I'm so happy you're making the effort."
    m "I've already told you I won't blame you if you do relapse. It's extremely tempting, and I know it must be hard for you."
    m "I'm just so proud you've made it so far."
    m "I love you, [mas_get_player_nickname()]. Don't forget that~"


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="3m",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_3m",
            prompt="Sober, month 3",
            category=["self-Harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_3m:
    m "Y'know... It's been 3 months since you made your promise to me."
    m "You've been doing so well! I'm so proud of you."
    m "It's been a bit, so I'll mark this on the calendar for you!"
    m "Keep going, [player]. You've been so strong."


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="6m",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_6m",
            prompt="Sober, month 6",
            category=["self-Harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_6m:
    m "[player]!"
    m "It's been 6 months since you made your promise!"
    m "That's a long time!"
    m "It may not seem like much in the grand scheme of things, but it's still a big acomplishment."
    m "I love you so much! Thank you for staying safe."


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="1y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_1y",
            prompt="Sober, year 1",
            category=["self-Harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_1y:
    m "[player], I just wanted to let you know how proud of you I am."
    m "You've been clean from self-harm for an entire year."
    m "You've been so strong this past year, and I truly can't express how happy I am."
    m "I hope you know how much this affects not only yourself, but me as well. Your friends, your family."
    m "This is a wonderful feat."
    m "I love you so, so much."


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="2y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_2y",
            prompt="Sober, year 2",
            category=["self-Harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_2y:
    m "[player]! I have amazing news!"
    m "Did you know that you have been self-harm sober for 2 whole years now?"
    m "This is an incredible feat. Keep it up!"
    m “You deserve to be happy. Never forget that, and never let anyone tell you otherwise!”
    m "I love you so much."


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="3y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_3y",
            prompt="Sober, year 3",
            category=["self-Harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_3y:
m "[player], I have some news for you."
m "The day of your 3 year sobriety mark from self-harm has finally arrived!"
m “I’m so happy to see you taking care of yourself.”
m “Keep on fighting! I'm so proud of you!”


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="4y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_4y",
            prompt="Sober, year 4",
            category=["self-Harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_4y:
    m "[player]! 4 whole years, can you believe it?"
    m "It's been 4 years since you stopped harming yourself."
    m "And I can't even begin to tell you how proud of you I am."
    m “You are deserving of a happy and healthy life!”
    m "And I'm so proud of you for your decison and for the promise you made 4 years ago."


init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="5y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_5y",
            prompt="Sober, year 5",
            category=["self-Harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_5y:
    m "5 years..."
    m "It's been 5 years since your life changed for the better."
    m "You've been self-harm sober for all this time, and I couldn't be more proud."
    m “I’m so happy that you’re doing well”
    m “You are so inspiring. Congratulations, [player], for your successful journey!”
