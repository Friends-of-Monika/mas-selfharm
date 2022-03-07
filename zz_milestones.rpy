default persistent._msh_mod_pm_sober_streak = None

init -9 python:
    def _mshMod_testSetSoberStreak(milestone):
        """
        Sets and adjusts sober streak initial date and time so that
        the specified milestone occurs on the present day (e.g. today)
        and resets the milestones.

        IN:
            milestone - milestone code.

        THROWS:
            ValueError - if unknown milestone code is passed.

        NOTE:
            This function must not be used in actual submod logic.
            It is created solely for testing/debugging purposes.
        """

        days = _mshMod_getMilestoneDays(milestone)
        persistent._msh_mod_pm_sober_streak = datetime.datetime.now() - datetime.timedelta(days=days)
        _mshMod_resetMilestones()

    def mshMod_beginStreak():
        """
        Sets sober streak initial date and time to current date and time.

        THROWS:
            ValueError - if player is already on sober streak.
        """

        if mshMod_isOnStreak():
            raise ValueError("player is already on sober streak")

        persistent._msh_mod_pm_sober_streak = datetime.datetime.now()

    def mshMod_breakStreak():
        """
        Unsets sober streak initial date and time and resets the milestones.

        THROWS:
            ValueError - if player is not on sober streak.
        """

        if not mshMod_isOnStreak():
            raise ValueError("player is not on sober streak")

        persistent._msh_mod_pm_sober_streak = None
        _mshMod_resetMilestones()

init -10 python:
    ### Assertions ###

    def _mshMod_assertOnStreak():
        """
        Assert function to check is player is on sober streak and throw
        an exception if not.

        THROWS:
            ValueError if player is not on sober streak.
        """

        if not mshMod_isOnStreak():
            raise ValueError("player is not on sober streak")

    ### Milestones/streak operations ###

    # TODO: This is too simple and does not actually reflect definitions
    # of months and years.
    # E.g. February has 28/29 days and April has 30 instead of 31,
    # as well as leap years having 366 days instead of 365.
    _mshMod_milestonesEnum = {
        "1w": 7,
        "1m": 31,
        "3m": 3 * 31,
        "6m": 6 * 31,
        "1y": 365,
        "2y": 2 * 365,
        "3y": 3 * 365,
        "4y": 4 * 365,
        "5y": 5 * 365
    }

    def _mshMod_getMilestoneDays(milestone):
        """
        Fetches amount of days since the first streak day to the specified
        milestone.

        IN:
            milestone - milestone code (i.e. "1w", "1m", "1y" etc.)

        OUT:
            Days until the milestone as integer number.

        THROWS:
            ValueError - if unknown milestone code is passed.
        """

        days = _mshMod_milestonesEnum.get(milestone)
        if days is None:
            raise ValueError("unknown milestone code " + milestone)
        return days

    def mshMod_isOnStreak():
        """
        Performs a check if sober streak initial date and time is set.

        OUT:
            True if player is on sober streak, False otherwise.
        """

        return persistent._msh_mod_pm_sober_streak is not None

    def mshMod_getMilestoneDate(milestone):
        """
        Computes appropriate start date (datetime.datetime instance with time
        values set to zero) for the specified milestone.

        IN:
            milestone - milestone code.

        OUT:
            An appropriate start date for a milestone.

        THROWS:
            ValueError - if unknown milestone code is passed or player is not
                         on sober streak.
        """

        _mshMod_assertOnStreak()
        return (persistent._msh_mod_pm_sober_streak + datetime.timedelta(days=_mshMod_getMilestoneDays(milestone))).replace(hour=0, minute=0, second=9)

    def mshMod_getMilestoneDateEnd(milestone):
        """
        Computes appropriate end date for the specified milestone (effectively,
        it is a return value of mshMod_getMilestoneDate call with day value
        increased by 1.)

        IN:
            milestone - milestone code.

        OUT:
            An appropriate end date for a milestone.

        THROWS:
            ValueError - if unknown milestone code is passed.
        """

        return mshMod_getMilestoneDate(milestone) + datetime.timedelta(days=1)

    def mshMod_isMilestoneToday(milestone):
        """
        Performs a check if today is the specified milestone. Player must be on
        a sober streak in order for this function to work.

        IN:
            milestone - milestone code.

        OUT:
            True if today is a specified milestone, False otherwise.

        THROWS:
            ValueError - if unknown milestone code is passed or player is not
                         on sober streak.
        """

        _mshMod_assertOnStreak()
        days = _mshMod_getMilestoneDays(milestone)
        return (datetime.datetime.now() - persistent._msh_mod_pm_sober_streak).days == days

    def mshMod_isPastMilestone(milestone):
        """
        Performs a check if today is past the specified milestone. Player must be
        on a sober streak in order for this function to work.

        IN:
            milestone - milestone code.

        OUT:
            True if today is past the specified milestone, False otherwise.

        THROWS:
            ValueError - if unknown milestone code is passed or player is not
                         on sober streak.
        """

        _mshMod_assertOnStreak()
        days = _mshMod_getMilestoneDays(milestone)
        return (datetime.datetime.now() - persistent._msh_mod_pm_sober_streak).days >= days

    ### Event registration / calendar handing internal routines and variables ###

    _mshMod_milestoneDatabase = (dict(), dict())
    _mshMod_milestoneEventsAdded = False

    def _mshMod_deferMilestoneAddEvent(ev, *args, **kwargs):
        """
        Defers milestone addEvent call until _mshMod_resetMilestones call
        and registers milestone event object internally.

        IN:
            ev - event object to defer addEvent call for.
            *args - currently unused.
            **kwargs - currently only used with "milestone" key which must be
                       a milestone code.
        """

        data = [ev, kwargs["milestone"]]
        _mshMod_milestoneDatabase[0][ev.eventlabel] = data
        _mshMod_milestoneDatabase[1][kwargs["milestone"]] = data

    def _mshMod_resetMilestones():
        """
        Resets milestones, possibly removing (and setting up) calendar marks
        for unachieved/achieved milestones correspondingly.

        NOTE:
            Only works with events whose addEvent calls were deferred with
            _mshMod_deferMilestoneAddEvent call.
        """

        if not mshMod_isOnStreak():
            # Lock all milestones and remove them from calendar.
            for _label, data in _mshMod_milestoneDatabase[0].items():
                mas_lockEVL(_label, "EVE")
                data[0].random = True
                store.mas_calendar.removeEvent(data[0])
        else:
            for _label, data in _mshMod_milestoneDatabase[0].items():
                ev, milestone = data
                past_milestone = mshMod_isPastMilestone(milestone)

                if not past_milestone or mshMod_isMilestoneToday(milestone):
                    # Lock milestones that are not achieved yet (and make
                    # them random.)
                    mas_lockEVL(_label, "EVE")
                    ev.random = True
                else:
                    # Past milestones should unlock, but should not pop up
                    # randomly.
                    mas_unlockEVL(_label, "EVE")
                    ev.random = False

                if not _mshMod_milestoneEventsAdded:
                    ev.start_date = mshMod_getMilestoneDate(milestone)
                    ev.end_date = mshMod_getMilestoneDateEnd(milestone)

                    # NOTE: directly updating mas_all_ev_db or else deferred
                    # addEvent calls cause exceptions on calendar interactions.
                    addEvent(ev, skipCalendar=not past_milestone)
                    data[0] = store.evhand.event_database[_label]
                    mas_all_ev_db[_label] = data[0]

                else:
                    # If it's a past milestone, we should remove it, modify it
                    # and then add it to calendar again.

                    if past_milestone:
                        store.mas_calendar.removeEvent(ev)

                    ev.start_date = mshMod_getMilestoneDate(milestone)
                    ev.end_date = mshMod_getMilestoneDateEnd(milestone)

                    if past_milestone:
                        store.mas_calendar.addEvent(ev)

            if not _mshMod_milestoneEventsAdded:
                global _mshMod_milestoneEventsAdded
                _mshMod_milestoneEventsAdded = True
                mas_rebuildEventLists()

init 6 python:
    # Actually call all deferred addEvent's for all milestones.
    _mshMod_resetMilestones()

    # TODO: No idea if this actually works, but it's worth a shot.
    # Need to test it though.

    # Run delayed milestone reset action once per day to ensure
    # current milestone is always visible on the calendar.
    _mshMod_milestoneDailyResetActionId = 1
    mas_delayed_action_map[_id] = store.MASDelayedAction.makeWithLabel(
        _mshMod_milestoneDailyResetActionId,
        "mshMod_streak_1week",
        "True",
        _mshMod_resetMilestones,
        store.MAS_FC_IDLE_DAY
    )

    if _mshMod_milestoneDailyResetActionId not in persistent._mas_delayed_action_list:
        persistent._mas_delayed_action_list.append(_mshMod_milestoneDailyResetActionId)
