default persistent._msh_mod_pm_sober_streak = None

init -10 python:
    _mshMod_milestones = {
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

    def _mshMod_getMilestoneDate(milestone):
        if persistent._msh_mod_pm_sober_streak is None:
            return None

        days = _mshMod_milestones.get(milestone)
        if days is None:
            return None

        date = persistent._msh_mod_pm_sober_streak + datetime.timedelta(days=days)
        date = datetime.datetime(date.year, date.month, date.day)
        return date

    def _mshMod_getMilestoneDateEnd(milestone):
        date = _mshMod_getMilestoneDate(milestone)
        if date is None:
            return None

        date = datetime.datetime(date.year, date.month, date.day, 23, 59, 59, 99999)
        return date

    def _mshMod_isMilestone(milestone):
        if persistent._msh_mod_pm_sober_streak is None:
            return False

        days = _mshMod_milestones.get(milestone)
        if days is None:
            return False

        return (datetime.datetime.now() - persistent._msh_mod_pm_sober_streak).days == days

init 5 python:
    if persistent._msh_mod_pm_sober_streak is not None:
        addEvent(
            Event(
                persistent.event_database,
                eventlabel='mshMod_streak_1week',
                prompt="1 Week",
                category=["sober"],
                action=EV_ACT_QUEUE,
                start_date=_mshMod_getMilestoneDate("1w")
            ),
            skipCalendar=False
        )

label mshMod_streak_1week:
    m 1etc "1 week test!"
    return "unlock"
