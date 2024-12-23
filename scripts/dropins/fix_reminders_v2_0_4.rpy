#
# FIX FOR BROKEN (PRE-2.0.4) REMINDERS
#
# Performs reminders deduplication and reset.
# Apply when reminders are stuck and not firing.
#
# How to apply:
#
#   1. Close the game if it's running
#   2. Drop into 'game' folder
#   3. Start the game
#   4. Say goodbye and exit
#   5. Delete this file and corresponding .rpyc file from 'game' folder
#   6. Start the game again
#

init 1000 python:
    _mshMod_fixMasEli() # fix possibly broken ELI with looped milestones
    _mshMod_fixDuplicateReminders() # remove duplicated reminders
    _mshMod_extendReminders() # fix reminders not triggering anymore
    _mshMod_resetReminderDelegateEndDates() # fix end dates
