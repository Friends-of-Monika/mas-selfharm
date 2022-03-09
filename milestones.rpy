init 5 python:
    mshMod_addMilestoneEvent(
        milestone="1w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_1w",
            prompt="Sober, 1 week",
            category=["self-harm"],
            action=EV_ACT_QUEUE
        )
    )

label mshMod_milestone_1w:
    m "1 week milestone test."
    return "derandom"
