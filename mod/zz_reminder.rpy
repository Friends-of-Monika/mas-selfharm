default persistent._mshMod_active_reminders = dict()

init 4 python in mshMod_reminder_utils:

    import datetime

    INTERVAL_DAILY = datetime.timedelta(days=1)
    INTERVAL_WEEKLY = datetime.timedelta(days=7)

    LATENCY_HOURLY = datetime.timedelta(seconds=3600)
    LATENCY_DAILY = datetime.timedelta(days=1)

    TOD_MORNING = (10, 0)  # 10:00, 10am
    TOD_AFTERNOON = (18, 0)  # 18:00, 6pm
    TOD_EVENING = (22, 0)  # 22:00, 10pm

    def _getDelay(tod, delta):
        hours, minutes = tod
        now = datetime.datetime.utcnow()

        # Ensure we don't skip over today's Time Of Day (e.g.
        # if requested delay is until 6pm and it's 3am, we shouldn't
        # blindly add delta; in this case, we should subtract 6pm - 3am
        # and return that as the delay.)
        if now.hour <= hours and now.minute <= minutes:
            return now.replace(hour=hours, minute=minutes) - now

        return (now + delta).replace(hour=hours, minute=minutes) - now

    def _getDailyDelay(tod):
        return _getDelay(tod, INTERVAL_DAILY)

    def getDailyMorningDelay():
        return _getDailyDelay(TOD_MORNING)

    def getDailyAfternoonDelay():
        return _getDailyDelay(TOD_AFTERNOON)

    def getDailyEveningDelay():
        return _getDailyDelay(TOD_EVENING)

    def _getWeeklyDelay(tod):
        return _getDelay(tod, INTERVAL_WEEKLY)

    def getWeeklyEveningDelay():
        return _getWeeklyDelay(TOD_EVENING)


init 4 python in mshMod_reminder:

    import store

    def _assertReminderActive(ev_label):
        if isReminderActive(ev_label):
            raise AssertionError("expected reminder to be active")

    def _assertReminderInactive(ev_label):
        if not isReminderActive(ev_label):
            raise AssertionError("expected reminder to be inactive")

    def addRecurringReminder(ev_label, delay, delta, latency):
        _assertReminderInactive(ev_label)

        store.persistent._mshMod_active_reminders[ev_label] = (
            datetime.datetime.utcnow() + delay,  # datetime to trigger after
            delta,  # time between triggers
            latency  # time after which reminder should not trigger
        )

    def isReminderActive(ev_label):
        return ev_label in store.persistent._mshMod_active_reminders

    def shouldTriggerReminder(ev_label):
        if not isReminderActive(ev_label):
            return False

        trigger, delta, latency = store.persistent._mshMod_active_reminders[ev_label]

        return trigger <= datetime.datetime.utcnow() <= trigger + latency

    def extendCurrentReminder():
        extendReminder(mas_globals.this_ev.eventlabel)

    def extendReminder(ev_label):
        _assertReminderActive(ev_label)

        trigger, delta, latency = store.persistent._mshMod_active_reminders[ev_label]

        _mshMod_active_reminders[ev_label] = (
            trigger + delta,  # ensure we base new trigger datetime off the initial trigger timedelta
            delta, latency
        )

    def stopReminder(ev_label):
        _assertReminderActive(ev_label)

        del store.persistent._mshMod_active_reminders[ev_label]
