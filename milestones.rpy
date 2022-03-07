init 5 python:
    _mshMod_deferMilestoneAddEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_streak_1week",
            prompt="1 Week",
            category=["sober"],
            conditional="not _mshMod_isMilestoneSeen('1w')"
            action=EV_ACT_QUEUE,
            random=True,
            rules={"force repeat": None}
        ),
        milestone="1w"
    )

label mshMod_streak_1week:
    m "Congratulations, player! You are on your 1 week streak now! I'm so proud of you, ehehe~"
    $ _mshMod_markMilestoneSeen("1w")
    return "derandom|unlock"
