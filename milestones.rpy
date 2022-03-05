default persistent._msh_mod_pm_sober_streak = None

init -9 python:
    def _mshMod_testSetSoberStreak(milestone):
        persistent._msh_mod_pm_sober_streak = datetime.datetime.now() - datetime.timedelta(days=_mshMod_milestonesEnum[milestone])
        _mshMod_resetMilestones()

    def _mshMod_beginStreak():
        persistent._msh_mod_pm_sober_streak = datetime.datetime.now()

    def _mshMod_resetStreak():
        persistent._msh_mod_pm_sober_streak = None
        _mshMod_resetMilestones()

init -10 python:
    def mshMod_isOnStreak():
        return persistent._msh_mod_pm_sober_streak is not None

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

    def mshMod_getMilestoneDate(milestone):
        if not mshMod_isOnStreak():
            return None

        days = _mshMod_milestonesEnum.get(milestone)
        if days is None:
            return None

        date = persistent._msh_mod_pm_sober_streak + datetime.timedelta(days=days)
        date = datetime.datetime(date.year, date.month, date.day)
        return date

    def mshMod_getMilestoneDateEnd(milestone):
        date = mshMod_getMilestoneDate(milestone)
        if date is None:
            return None

        date = datetime.datetime(date.year, date.month, date.day) + datetime.timedelta(days=1)
        return date

    def mshMod_isMilestoneToday(milestone):
        if not mshMod_isOnStreak():
            return False

        days = _mshMod_milestonesEnum.get(milestone)
        if days is None:
            return False

        return (datetime.datetime.now() - persistent._msh_mod_pm_sober_streak).days == days

    def mshMod_isPastMilestone(milestone):
        if not mshMod_isOnStreak():
            return False

        days = _mshMod_milestonesEnum.get(milestone)
        if days is None:
            return False

        return (datetime.datetime.now() - persistent._msh_mod_pm_sober_streak).days >= days

    _mshMod_milestoneDatabase = (dict(), dict())
    _mshMod_milestoneEventsAdded = False

    def _mshMod_deferMilestoneAddEvent(ev, *args, **kwargs):
        data = [ev, kwargs["milestone"]]
        _mshMod_milestoneDatabase[0][ev.eventlabel] = data
        _mshMod_milestoneDatabase[1][kwargs["milestone"]] = data

    def _mshMod_resetMilestones():
        if not mshMod_isOnStreak():
            return

        for _label, data in _mshMod_milestoneDatabase[0].items():
            ev, milestone = data
            past_milestone = mshMod_isPastMilestone(milestone)

            if not past_milestone:
                mas_lockEVL(_label, "EVE")
            else:
                mas_unlockEVL(_label, "EVE")
                ev.random = False

            if not _mshMod_milestoneEventsAdded:
                ev.start_date = mshMod_getMilestoneDate(milestone)
                ev.end_date = mshMod_getMilestoneDateEnd(milestone)

                addEvent(ev, skipCalendar=not past_milestone)
                data[0] = store.evhand.event_database[_label]
                mas_all_ev_db[_label] = data[0]

            else:
                if past_milestone:
                    store.mas_calendar.removeEvent(ev)

                ev.start_date = mshMod_getMilestoneDate(milestone)
                ev.end_date = mshMod_getMilestoneDateEnd(milestone)

                if past_milestone:
                    store.mas_calendar.addEvent(ev)

        if not _mshMod_milestoneEventsAdded:
            global _mshMod_milestoneEventsAdded
            _mshMod_milestoneEventsAdded = True

init 6 python:
    _mshMod_resetMilestones()

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
