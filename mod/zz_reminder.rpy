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
        now = datetime.datetime.now()

        # Ensure we don't skip over today's Time Of Day (e.g.
        # if requested delay is until 6pm and it's 3am, we shouldn't
        # blindly add delta; in this case, we should subtract 6pm - 3am
        # and return that as the delay.)
        if now < now.replace(hour=hours, minute=minutes):
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
    import datetime

    def _assertReminderActive(ev_label):
        if not isReminderActive(ev_label):
            raise AssertionError("expected reminder to be active")

    def _assertReminderInactive(ev_label):
        if isReminderActive(ev_label):
            raise AssertionError("expected reminder to be inactive")

    def addRecurringReminder(ev_label, delay, delta, latency):
        _assertReminderInactive(ev_label)

        store.persistent._mshMod_active_reminders[ev_label] = (
            datetime.datetime.now() + delay,  # datetime to trigger after
            delta,  # time between triggers
            latency  # time after which reminder should not trigger
        )

    def isReminderActive(ev_label):
        return ev_label in store.persistent._mshMod_active_reminders

    def shouldTriggerReminder(ev_label):
        if not isReminderActive(ev_label):
            return False

        trigger, delta, latency = store.persistent._mshMod_active_reminders[ev_label]

        return trigger <= datetime.datetime.now() <= trigger + latency

    def isReminderMissed(ev_label):
        trigger, delta, latency = store.persistent._mshMod_active_reminders[ev_label]

        return trigger + latency <= datetime.datetime.now()

    def extendCurrentReminder():
        ev_label = store.mas_globals.this_ev.eventlabel

        extendReminder(ev_label)

        # HACK: workaround so that MAS doesn't strip conditional and action from reminder event.
        ev, conditional, action = _reminderEvents[ev_label]
        ev.conditional, ev.action = conditional, action

    def extendReminder(ev_label, keep_up=False):
        _assertReminderActive(ev_label)

        now = datetime.datetime.now()

        while True:
            trigger, delta, latency = store.persistent._mshMod_active_reminders[ev_label]

            store.mas_submod_utils.submod_log.info(str((store.persistent._mshMod_active_reminders[ev_label], now)))
            store.persistent._mshMod_active_reminders[ev_label] = (
                trigger + delta,  # ensure we base new trigger datetime off the initial trigger timedelta
                delta, latency
            )

            if keep_up:
                if store.persistent._mshMod_active_reminders[ev_label][0] <= now:
                    continue
                else:
                    break
            else:
                break

    def stopReminder(ev_label):
        _assertReminderActive(ev_label)

        del store.persistent._mshMod_active_reminders[ev_label]


    ### Missed reminder handling

    def _handleMissedReminders():
        for ev_label in store.persistent._mshMod_active_reminders.keys():
            trigger, delta, latency = store.persistent._mshMod_active_reminders[ev_label]
            if isReminderMissed(ev_label):
                extendReminder(ev_label, keep_up=True)

    _handleMissedReminders()
    store.mas_submod_utils.registerFunction("ch30_day", _handleMissedReminders)


init 4 python in mshMod_reminder:

    _reminderEvents = dict()

    def addReminderEvent(event):
        _reminderEvents[event.eventlabel] = (event, event.conditional, event.action)
        store.addEvent(event)
