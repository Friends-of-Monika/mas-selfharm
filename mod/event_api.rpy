init python in mshMod_utils:

    import store

    ### EVENT PROPERTIES UNLOCK ###

    _lockedProps = (
        "unlocked", "random", "pool", "conditional",
        "action", "start_date", "end_date", "unlock_date",
        "shown_count", "last_seen"
    )

    def unlockAllEventProps(ev):
        """
        Forcibly unlock all attributes of Event. Required for modification
        of start_date/end_date and almost every other attribute.

        NOTE:
            An internal function. Should not be used by other submods.

        IN:
            ev - Event label to unlock attributes of.
        """

        for prop in _lockedProps:
            store.Event.unlockInit(prop, ev=ev)
