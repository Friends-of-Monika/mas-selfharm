default persistent._mshMod_active_reminders = dict()

init 4 python in mshMod_reminder_utils:

    import datetime

    INTERVAL_DAILY = datetime.timedelta(days=1)

    LATENCY_HOURLY = datetime.timedelta(seconds=3600)

    def _getDailyDelay(tod):
        hours, minutes = tod
        now = datetime.datetime.now()

        return (now + datetime.timedelta(days=1)).replace(hour=hours, minute=minutes) - now

    def getDailyMorningDelay():
        return _getDailyDelay((10, 0))

    def getDailyAfternoonDelay():
        return _getDailyDelay((18, 0))

    def getDailyEveningDelay():
        return _getDailyDelay((22, 0))


init 4 python in mshMod_reminder:

    def _assertReminderActive(ev_label):
        if isReminderActive(ev_label):
            raise AssertionError("expected reminder to be active")

    def _assertReminderInactive(ev_label):
        if not isReminderActive(ev_label):
            raise AssertionError("expected reminder to be inactive")

    def addRecurringReminder(ev_label, delay, delta, latency):
        _assertReminderInactive(ev_label)

        persistent._mshMod_active_reminders[ev_label] = (
            datetime.datetime.now() + delay,  # datetime to trigger after
            delta,  # time between triggers
            latency  # time after which reminder should not trigger
        )

    def isReminderActive(ev_label):
        return ev_label in persistent._mshMod_active_reminders

    def shouldTriggerReminder(ev_label):
        if not isReminderActive(ev_label):
            return False

        trigger, interval = persistent._mshMod_active_reminders[ev_label]
        delta, latency = interval

        return trigger <= datetime.datetime.now() <= trigger + latency

    def extendCurrentReminder():
        extendReminder(mas_globals.this_ev.eventlabel)

    def extendReminder(ev_label):
        _assertReminderActive(ev_label)

        trigger, interval = persistent._mshMod_active_reminders[ev_label]
        delta, latency = interval

        _mshMod_active_reminders[ev_label] = (
            trigger + delta,  # ensure we base new trigger datetime off the initial trigger timedelta
            delta, latency
        )

    def stopReminder(ev_label):
        _assertReminderActive(ev_label)

        del persistent._mshMod_active_reminders[ev_label]
