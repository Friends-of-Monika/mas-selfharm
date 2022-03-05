init 5 python:
    _mshMod_deferMilestoneAddEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_streak_1week",
            prompt="1 Week",
            category=["sober"],
            action=EV_ACT_QUEUE,
            rules={"force repeat": None}
        ),
        milestone="1w"
    )

label mshMod_streak_1week:
    m "Congratulations, player! You are on your 1 week streak now! I'm so proud of you, ehehe~"
    return "derandom|unlock"
