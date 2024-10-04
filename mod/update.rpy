default persistent._msh_mod_sha_migrated = False
default persistent._msh_mod_was_installed = False
define _msh_mod_migrated_now = False

init -980 python:
    if "MAS Self Harm Submod" in persistent._mas_submod_version_data:
        persistent._msh_mod_was_installed = True

    ## Since SHA (anni update) REALLY does conflict with MSH (< v2)
    ## need to warn people NOT to mix them together; and do it as soon as possible
    ## after startup

    if store.mas_submod_utils.isSubmodInstalled("MAS Self Harm Submod"):
        raise RuntimeError("Self Harm Awareness Submod (previously named MAS Self Harm Submod) "
                           "is in conflict with its older version that is already installed.\n"
                           "Please uninstall MAS Self Harm Submod before installing Self Harm Awareness Submod.")

init 5 python:
    def _mshMod_migrateReminder(evl, key):             # No-op if:
        if not (persistent._msh_mod_was_installed and  # 1. MSH was never installed
                not persistent._msh_mod_sha_migrated and  # 2. SHA migration not done yet
                hasattr(store.persistent, "_mshMod_active_reminders") and  # 3. Reminders weren't used at all
                store.persistent._mshMod_active_reminders is not None):    # 4. There are no reminders active
            return

        ## Since we'll remove it from OG map when done,
        ## need to be safe here.
        reminder = store.persistent._mshMod_active_reminders.get(evl)
        if reminder is None:
            return

        ## Perform actual migration here
        store._msh_reminder.queue_reminder(
            store._msh_reminder.Reminder(
                trigger_at=reminder[0],
                target_evl=evl,
                key=key,
                interval=reminder[1],
                grace_period=reminder[2]
            )
        )

        ## Remove from OG map not to do it again
        del store.persistent._mshMod_active_reminders[evl]

    def _mshMod_migrateResetTopic(evl, action=False, conditional=False):
        ## Don't do anything if MSH was never installed or already migrated
        if not (persistent._msh_mod_was_installed and not persistent._msh_mod_sha_migrated):
            return

        ## Make sure we actually have this topic
        ev = mas_getEV(evl)
        if ev is None:
            return

        ## Reset what's requested
        if action:
            ev.action = None
        if conditional:
            ev.conditional = None

    def _mshMod_migrateSetStartDayAnnually(evl, date):
        ## Don't do anything if MSH was never installed or already migrated
        if not (persistent._msh_mod_was_installed and not persistent._msh_mod_sha_migrated):
            return

        ## Ensure this exists
        ev = mas_getEV(evl)
        if ev is None:
            return

        ev.start_date = date
        ev.end_date = date + datetime.timedelta(days=1)
        ev.years = []

    def _mshMod_migrateSetConditionalIfLocked(evl, conditional, action=EV_ACT_RANDOM):
        ## Don't do anything if MSH was never installed or already migrated
        if not (persistent._msh_mod_was_installed and not persistent._msh_mod_sha_migrated):
            return

        ## Ensure this exists
        ev = mas_getEV(evl)
        if ev is None:
            return

        if not ev.unlocked:
            ev.conditional = conditional
            ev.action = action

    def _mshMod_migrateUnlockIfLockedAndSeen(evl):
        ## Don't do anything if MSH was never installed or already migrated
        if not (persistent._msh_mod_was_installed and not persistent._msh_mod_sha_migrated):
            return

        ev = mas_getEV(evl)
        if ev is None:
            return

        if not ev.unlocked and ev.last_seen is not None:
            ev.unlocked = True

    def _mshMod_migrateBrokenReminder(key):
        rem_idx = store._msh_reminder.get_reminder(key)
        if rem_idx is None:
            return

        rem = store._msh_reminder.queue[rem_idx]
        if isinstance(rem.trigger_at, datetime.timedelta):
            store._msh_reminder.pop_reminder(rem_idx, remove=True)
            rem.trigger_at = datetime.datetime.now() + rem.trigger_at
            store._msh_reminder.queue_reminder(rem)

    def _mshMod_fixMasEli():
        ev_labels = list(store.mshMod_sober_streak.by_label.keys())
        for evl in ev_labels:
            store.mshMod_sober_streak.remove_from_eli(evl, dedupe=True)

    def _mshMod_fixDuplicateReminders():
        def count_reminders(key):
            return len(filter(lambda it: it.key == key,
                              store._msh_reminder.queue))

        def dedupe_reminders(key):
            while count_reminders(key) > 1:
                store._msh_reminder.dequeue_reminder(key)

        dedupe_reminders("checkup_reminder")
        dedupe_reminders("medication_reminder")

    def _mshMod_extendReminders():
        today = datetime.date.today()
        for reminder in list(store._msh_reminder.queue):
            if reminder.interval is not None and reminder.trigger_at.date() < today:
                store._msh_reminder.pop_reminder(reminder)

init 10 python:

    ## Introduction does no_unlock previously, not needed

    _mshMod_migrateUnlockIfLockedAndSeen("mshMod_topic_selfharm_intro")

    ## Since we have updated SIAD topic, need to force these updates
    ## on locked properties here

    _mshMod_migrateSetStartDayAnnually("mshMod_topic_awareness_day", datetime.date(2022, 3, 1))

    ## We also need to update healthy routine tips so that they use
    ## proper conditionals and all that

    _mshMod_migrateSetConditionalIfLocked("mshMod_topic_excercises", "seen_event('mshMod_topic_morning_routine')")
    _mshMod_migrateSetConditionalIfLocked("mshMod_topic_morning_excercises", "seen_event('mshMod_topic_excercises')")
    _mshMod_migrateSetConditionalIfLocked("mshMod_topic_going_outside", "seen_event('mshMod_topic_morning_excercises')")


init 11 python:

    ## Since SHA uses new TRM reminder core, need to migrate existing implementation
    ## data to new API; do so here.

    _mshMod_migrateReminder("mshMod_checkup_reminder", "checkup_reminder")
    _mshMod_migrateReminder("mshMod_medication_reminder", "medication_reminder")
    if "_mshMod_active_reminders" in persistent.__dict__:
        del persistent.__dict__["_mshMod_active_reminders"]

    _mshMod_migrateResetTopic("mshMod_checkup_reminder", action=True, conditional=True)
    _mshMod_migrateResetTopic("mshMod_medication_reminder", action=True, conditional=True)
    _mshMod_migrateResetTopic("mshMod_medication_reminder_stop", conditional=True)


init 996 python:

    ## In order to properly mark state as migrated, need some prechecks.
    ## Also, only set _msh_mod_migrated_now once, if we'll need it

    if not persistent._msh_mod_sha_migrated and persistent._msh_mod_was_installed:
        persistent._msh_mod_sha_migrated = True
        _msh_mod_migrated_now = True


init 996 python:

    ## Fix reminder that was broken until 2.0.0

    _mshMod_migrateBrokenReminder("checkup_reminder")


## After v2.0.0 we can use normal update approaches

label friends_of_monika_self_harm_awareness_submod_v2_0_3(version="v2_0_3"):
    return

label friends_of_monika_self_harm_awareness_submod_v2_0_4(version="v2_0_4"):
    $ _mshMod_fixMasEli() # fix possibly broken ELI with looped milestones
    $ _mshMod_fixDuplicateReminders() # remove duplicated reminders
    $ _mshMod_extendReminders() # fix reminders not triggering anymore
    return
