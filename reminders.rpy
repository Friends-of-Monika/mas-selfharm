label mshMod_remind_medication:
    $ meta = _mshMod_currentReminderMeta
    m "[player], it's time to take your pills!"
    m "By the way, that reminder fired after [meta.delay.seconds] seconds and [meta.delay.microseconds] microseconds."
    return
