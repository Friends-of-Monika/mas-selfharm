default persistent._mshMod_nextReminderTrigger = None

init 5 python in mshMod_reminder:
    def remind(delay):
        persistent._mshMod_nextReminderTrigger = datetime.datetime.now() + delay

    def stop():
        persitent._mshMod_nextReminderTrigger = None


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder",
            conditional="persistent._mshMod_nextReminderTrigger and "
                        "datetime.datetime.now() >= persistent._mshMod_nextReminderTrigger",
            action=EV_ACT_PUSH,
            rules={"force repeat": None}
        )
    )

label mshMod_medication_reminder:
    $ store.mshMod_reminder.remind(datetime.timedelta(day=1))
    m "Here's your reminder, [player]; next one will trigger after [persistent._mshMod_nextReminderTrigger]."
    return "no_unlock"
