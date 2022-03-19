default persistent._msh_mod_pm_sober_streak = None
default persistent._msh_mod_pm_sober_personal_best = None

init 4 python:

    ### ASSERTIONS ###

    def _mshMod_assertOnStreak():
        if not mshMod_isOnStreak():
            raise AssertionError("expected player to be on streak")

    def _mshMod_assertNotOnStreak():
        if mshMod_isOnStreak():
            raise AssertionError("expected player not to be on streak")

    def _mshMod_assertHasPersonalBest():
        if not mshMod_hasPersonalBest():
            raise AssertionError("personal best is not set")


    ### STREAK OPERATIONS ###

    def mshMod_isOnStreak():
        return persistent._msh_mod_pm_sober_streak is not None

    def mshMod_beginStreak():
        _mshMod_assertNotOnStreak()

        persistent._msh_mod_pm_sober_streak = datetime.date.today()
        _mshMod_rebuildMilestoneDates()

    def mshMod_endStreak():
        _mshMod_assertOnStreak()

        # Update personal best if current streak is longer than the previous.
        if persistent._msh_mod_pm_sober_personal_best is not None:
            since, days = persistent._msh_mod_pm_sober_personal_best
            c_days = (datetime.date.today() - persistent._msh_mod_pm_sober_personal_best[0]).days
            if c_days > days:
                persistent._msh_mod_pm_sober_personal_best = (persistent._msh_mod_pm_sober_streak, c_days)
        else:
            persistent._msh_mod_pm_sober_personal_best = (persistent._msh_mod_pm_sober_streak, (datetime.date.today() - persistent._msh_mod_pm_sober_streak).days)

        # Reset streak initial date and rebuild the calendar and events.
        persistent._msh_mod_pm_sober_streak = None
        _mshMod_rebuildMilestoneDates()
        _mshMod_updateMilestoneEvents()

    def mshMod_hasPersonalBest():
        return persistent._msh_mod_pm_sober_personal_best is not None

    def mshMod_resetPersonalBest():
        persistent._msh_mod_pm_sober_personal_best = None
        _mshMod_updateMilestoneEvents()


    ### MILESTONE DATE DEFINITION ###

    def _mshMod_getEndDateTuple(date):
        return (date, date + datetime.timedelta(days=1))

    def _mshMod_getWeeklyMilestone(weeks, since=None):
        if since is None:
            since = persistent._msh_mod_pm_sober_streak

        return _mshMod_getEndDateTuple(since + datetime.timedelta(days=weeks * 7))

    def _mshMod_getMonthlyMilestone(months, since=None):
        if since is None:
            since = persistent._msh_mod_pm_sober_streak

        new_y, new_m = since.year, since.month + months
        new_y, new_m = new_y + new_m // 12, new_m % 12

        new_d = since.day
        if since.day > 28 and new_m == 2:
            new_d = 29 if ((new_y % 4 == 0 and not new_y % 100 == 0) or new_y % 400 == 0) else 28
        elif since.day > 30 and new_m in (4, 6, 9, 11):
            new_d = 30

        return _mshMod_getEndDateTuple(since.replace(year=new_y, month=new_m, day=new_d))

    def _mshMod_getYearlyMilestone(years, since=None):
        if since is None:
            since = persistent._msh_mod_pm_sober_streak

        return _mshMod_getEndDateTuple(since.replace(year=since.year+years))

    _mshMod_milestoneDates = dict()
    def _mshMod_rebuildMilestoneDates():
        if not mshMod_isOnStreak():
            if _mshMod_milestoneDates:
                _mshMod_milestoneDates.clear()
        else:
            _mshMod_milestoneDates.update({
            # Weeks
                "1w": _mshMod_getWeeklyMilestone(1),
                "2w": _mshMod_getWeeklyMilestone(2),
                "3w": _mshMod_getWeeklyMilestone(3),

            # Months
                "1m": _mshMod_getMonthlyMilestone(1),
                "3m": _mshMod_getMonthlyMilestone(3),
                "6m": _mshMod_getMonthlyMilestone(6),

            # Years
                "1y": _mshMod_getYearlyMilestone(1),
                "2y": _mshMod_getYearlyMilestone(2),
                "3y": _mshMod_getYearlyMilestone(3),
                "4y": _mshMod_getYearlyMilestone(4),
                "5y": _mshMod_getYearlyMilestone(5)}
            )

    def _mshMod_getPersonalBestDateTuple():
        _mshMod_assertHasPersonalBest()

        since, days = persistent._msh_mod_pm_sober_personal_best
        start = since + datetime.timedelta(days=days)
        return start, start + datetime.timedelta(days=1)

    def _mshMod_getMilestoneDateTuple(code):
        date = _mshMod_milestoneDates.get(code)
        if date is not None:
            return _mshMod_milestoneDates[code]
        raise KeyError("unknown milestone code " + code)

    def mshMod_getMilestoneDate(code):
        return _mshMod_getMilestoneDateTuple(code)[0]

    def _get_milestone_date_end(code):
        return _mshMod_getMilestoneDateTuple(code)[1]

    def mshMod_isMilestoneToday(code):
        return mshMod_getMilestoneDate(code) == datetime.date.today()

    def mshMod_isMilestonePast(code):
        return mshMod_getMilestoneDate(code) < datetime.date.today()

    def mshMod_getTodayMilestone():
        for code in _mshMod_milestoneDates.keys():
            if mshMod_isMilestoneToday(code):
                return code
        return None

    def mshMod_getPastMilestones():
        milestones = list()

        for code in _mshMod_milestoneDates.keys():
            if mshMod_isMilestonePast(code):
                milestones.append(code)

        return milestones


    ### EVENT MANAGEMENT ###

    _mshMod_eventProperties = (
        "eventlabel", "prompt", "label", "category", "unlocked",
        "random", "pool", "conditional", "action", "start_date",
        "end_date", "unlock_date", "shown_count", "last_seen",
        "years", "sensitive", "aff_range", "show_in_idle", "flags"
    )

    _mshMod_milestoneEvents = (dict(), dict())
    def mshMod_addMilestoneEvent(event, milestone):
        by_label, by_code = _mshMod_milestoneEvents
        data = (event, milestone)
        by_label[event.eventlabel] = data
        by_code[milestone] = data

        store.addEvent(event)

    def _mshMod_getMilestoneEvent(code):
        ev = _mshMod_milestoneEvents[1].get(code)
        if ev is not None:
            return ev
        raise KeyError("unknown milestone " + code)

    def _mshMod_updateMilestoneEvents():
        if mshMod_isOnStreak():
            for milestone in mshMod_getPastMilestones():
                ev, _ = _mshMod_getMilestoneEvent(milestone)

                # Past events must have start and end date in order
                # to display on calendar.
                ev.start_date, ev.end_date = _mshMod_getMilestoneDateTuple(milestone)
                store.mas_calendar.addEvent(ev)

                # Derandom and unlock this event so it can be repeated through the menu.
                ev.random, ev.unlocked = False, True
                ev.unlock_date, ev.last_seen = None, None

                # Also mark it seen for Ren'Py/MAS.
                _mshMod_seeLabel(ev.eventlabel)

            # Add today's milestone to calendar if possible.
            milestone = mshMod_getTodayMilestone()
            if milestone is not None:
                ev, _ = _mshMod_getMilestoneEvent(milestone)

                ev.start_date, ev.end_date = _mshMod_getMilestoneDateTuple(milestone)

                store.mas_calendar.addEvent(ev)
                if not mas_seenLabels([ev.eventlabel]):
                    ev.random, ev.unlocked = True, False
                    ev.unlock_date, ev.last_seen = None, None
        else:
            for label, data in _mshMod_milestoneEvents[0].items():
                ev = data[0]

                # Remove these events from the calendar.
                store.mas_calendar.removeEvent(ev)

                # Since we're not on streak, these events should never trigger.
                ev.start_date, ev.end_date = None, None
                ev.random, ev.unlocked = False, False

        if persistent._msh_mod_pm_sober_personal_best is not None:
            since, days = persistent._msh_mod_pm_sober_personal_best

            ev = _mshMod_personalBestEvent
            store.mas_calendar.removeEvent(ev)

            ev.start_date, ev.end_date = _mshMod_getPersonalBestDateTuple()
            store.mas_calendar.addEvent(ev)
        else:
            store.mas_calendar.removeEvent(_mshMod_personalBestEvent)


    ### UTILITIES ###

    def _mshMod_seeLabel(label):
        persistent._seen_ever[label] = True

    def _mshMod_unseeLabel(label):
        if label in persistent._ever_seen:
            del persistent._seen_ever[label]


init 10 python:

    ### MILESTONE EVENT PROPERTIES UNLOCK ###

    _mshMod_lockedProps = (
        "unlocked", "random", "pool", "conditional",
        "action", "start_date", "end_date", "unlock_date",
        "shown_count", "last_seen"
    )

    def _mshMod_unlockAllEventProps(ev):
        for prop in _mshMod_lockedProps:
            Event.unlockInit(prop, ev=ev)


    by_label, by_code = _mshMod_milestoneEvents
    for code, data in by_code.items():
        ev = mas_getEV(data[0].eventlabel)
        _mshMod_unlockAllEventProps(ev)

        # Keep a reference to event object saved in events list.
        data_pair = (ev, data[1])
        by_label[ev.eventlabel] = data_pair
        by_code[code] = data_pair

    # Make personal best event modifiable.
    _mshMod_personalBestEvent = mas_getEV(_mshMod_personalBestEventLabel)
    _mshMod_unlockAllEventProps(_mshMod_personalBestEvent)


init 11 python:

    ### INITIAL APPLICATION OF MILESTONE EVENTS ###

    _mshMod_rebuildMilestoneDates()
    _mshMod_updateMilestoneEvents()


init 7 python:
    import time

    def _mshMod_dailyUpdaterThread():
        last_checked_day = datetime.date.today().day

        while True:
            time.sleep(5)

            day = datetime.date.today().day
            if last_checked_day != day:
                _mshMod_rebuildMilestoneDates()
                _mshMod_updateMilestoneEvents()

    renpy.invoke_in_thread(_mshMod_dailyUpdaterThread)


init 5 python:

    _mshMod_personalBestEventLabel = "mshMod_milestone_personal_best"
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_milestone_personal_best",
            prompt="Sober, personal best",
            conditional="False",
            action=EV_ACT_QUEUE
        )
    )


label mshMod_milestone_personal_best:
    # This exists just for sake of proper rendering of the personal best
    # event on the calendar. Do not touch this!
    return
