init 5 python hide:
    if hasattr(store.persistent, "_mshMod_active_reminders"):
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