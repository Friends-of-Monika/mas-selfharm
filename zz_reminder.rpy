default persistent._mshMod_reminders = dict()

init -10 python:
    class _mshMod_CurrentReminderMeta:
        def __init__(self, date, _label, payload):
            self.date = date
            self.evlabel = _label
            self.payload = payload
            self.delay = 0

    _mshMod_currentReminderMeta = None

    def mshMod_createReminder(name, date, _label, payload=None):
        persistent._mshMod_reminders[name] = _mshMod_CurrentReminderMeta(date, _label, payload)

    def mshMod_cancelReminder(name):
        if name in persistent._mshMod_reminders:
            del persistent._mshMod_reminders[name]

    def _mshMod_popTriggeredReminder():
        if not persistent._mshMod_reminders:
            # TODO: throw
            return None

        items = list(persistent._mshMod_reminders.items())
        items.sort(key=lambda it: it[1].date)

        rem = persistent._mshMod_reminders[items[0][0]]
        del persistent._mshMod_reminders[items[0][0]]

        return rem

    def _mshMod_shouldTriggerEvent():
        if not persistent._mshMod_reminders:
            return False

        now = datetime.datetime.now()
        for name, meta in persistent._mshMod_reminders.items():
            if meta.date <= now:
                return True

        return False

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="_mshMod_reminderTriggerHelper",
            conditional="_mshMod_shouldTriggerEvent()",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None},
            random=True
        )
    )

label _mshMod_reminderTriggerHelper:
    python:
        meta = _mshMod_popTriggeredReminder()
        meta.delay = datetime.datetime.now() - meta.date
        _mshMod_currentReminderMeta = meta

        queueEvent(meta.evlabel, notify=True)
    return "no_unlock"
