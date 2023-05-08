init 11 python:
    if hasattr(store.persistent, "_mshMod_active_reminders") and store.persistent._mshMod_active_reminders is not None:
        if "mshMod_checkup_reminder" in store.persistent._mshMod_active_reminders:
            reminder = store.persistent._mshMod_active_reminders["mshMod_checkup_reminder"]
            store._msh_reminder.queue_reminder(
                store._msh_reminder.Reminder(
                    trigger_at=reminder[0],
                    target_evl="mshMod_checkup_reminder",
                    key="checkup_reminder",
                    interval=reminder[1],
                    grace_period=reminder[2]
                )
            )

        if "mshMod_medication_reminder" in store.persistent._mshMod_active_reminders:
            reminder = store.persistent._mshMod_active_reminders["mshMod_medication_reminder"]
            store._msh_reminder.queue_reminder(
                store._msh_reminder.Reminder(
                    trigger_at=reminder[0],
                    target_evl="mshMod_medication_reminder",
                    key="medication_reminder",
                    interval=reminder[1],
                    grace_period=reminder[2]
                )
            )

        del store.persistent._mshMod_active_reminders

    ev = mas_getEV("mshMod_checkup_reminder")
    if ev is not None:
        ev.action = None
        ev.conditional = None

    ev = mas_getEV("mshMod_medication_reminder")
    if ev is not None:
        ev.action = None
        ev.conditional = None

    ev = mas_getEV("mshMod_medication_reminder_stop")
    if ev is not None:
        ev.conditional = None