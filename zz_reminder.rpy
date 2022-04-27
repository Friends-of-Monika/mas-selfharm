default persistent._mshMod_reminders = dict()

init -10 python in mshMod_reminder:
    class _CurrentReminderMeta:
        def __init__(self, date, _label, payload):
            self.date = date
            self.evlabel = _label
            self.payload = payload
            self.delay = 0

    _currentReminderMeta = None

    def createReminder(name, date, _label, payload=None):
        persistent._reminders[name] = _CurrentReminderMeta(date, _label, payload)

    def cancelReminder(name):
        if name in persistent._reminders:
            del persistent._reminders[name]

    def _popTriggeredReminder():
        if not persistent._reminders:
            raise ValueError("no active reminders")

        items = list(persistent._reminders.items())
        items.sort(key=lambda it: it[1].date)

        rem = persistent._reminders[items[0][0]]
        del persistent._reminders[items[0][0]]

        return rem

    def _shouldTriggerEvent():
        if not persistent._reminders:
            return False

        now = datetime.datetime.now()
        for name, meta in persistent._reminders.items():
            if meta.date <= now:
                return True

        return False


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_reminderTriggerHelper",
            conditional="store.mshMod_reminder._shouldTriggerEvent()",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None},
            random=True
        )
    )

label mshMod_reminderTriggerHelper:
    python:
        meta = _popTriggeredReminder()
        meta.delay = datetime.datetime.now() - meta.date
        _currentReminderMeta = meta

        queueEvent(meta.evlabel, notify=True)
    return "no_unlock"
