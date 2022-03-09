default persistent._msh_mod_pm_sober_streak = None

init -1000 python:

    ### ASSERTIONS ###

    def _mshMod_assertOnStreak():
        if not mshMod_isOnStreak():
            raise AssertionError("expected player to be on streak")

    def _mshMod_assertNotOnStreak():
        if mshMod_isOnStreak():
            raise AssertionError("expected player not to be on streak")


    ### STREAK OPERATIONS ###

    def mshMod_isOnStreak():
        return persistent._msh_mod_pm_sober_streak is not None

    def mshMod_beginStreak():
        _mshMod_assertNotOnStreak()
        persistent._msh_mod_pm_sober_streak = datetime.date.today()

        _mshMod_rebuildMilestoneDates()

    def mshMod_endStreak():
        _mshMod_assertOnStreak()
        persistent._msh_mod_pm_sober_streak = None

        _mshMod_rebuildMilestoneDates()
        _mshMod_updateMilestoneEvents()
        # TODO: hide calendar marks, leave personal best mark


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

    def _mshMod_getPastMilestones():
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
            for milestone in _mshMod_getPastMilestones():
                ev = _mshMod_getMilestoneEvent(milestone)

                # Past events must have start and end date in order
                # to display on calendar.
                ev.start_date, ev.end_date = _mshMod_getMilestoneDateTuple(milestone)
                store.mas_calendar.addEvent(ev)

                # Derandom and unlock this event so it can be repeated through the menu.
                ev.random, ev.unlocked = False, True

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

        else:
            for label, data in _mshMod_milestoneEvents[0].items():
                ev = data[0]

                # Remove these events from the calendar.
                store.mas_calendar.removeEvent(ev)

                # Since we're not on streak, these events should never trigger.
                ev.start_date, ev.end_date = None, None
                ev.random, ev.unlocked = False, False


init 1000 python:

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
        ev = store.mas_getEV(data[0].eventlabel)
        _mshMod_unlockAllEventProps(ev)

        # Also keep a reference to event object saved in events list.
        data_pair = (ev, data[1])
        by_label[ev.eventlabel] = data_pair
        by_code[code] = data_pair


init -1000 python:

    ### REN'PY SEEN/UNSEEN FUNCTIONS ###

    def _mshMod_seeLabel(label):
        persistent._ever_seen[label] = True

    def _mshMod_unseeLabel(label):
        if label in persistent._ever_seen:
            del persistent._ever_seen[label]


init 11 python:

    ### INITIAL APPLICATION OF MILESTONE EVENTS ###

    _mshMod_rebuildMilestoneDates()
    _mshMod_updateMilestoneEvents()
