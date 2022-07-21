init 10000 python:

    ## Undo full unlock on events and only unlock start_date and end_date ##

    for ev_label in (ev_label for ev_label in mas_all_ev_db.keys() if ev_label.startswith("mshMod_sober_milestone_")):
        # Reset to template
        persistent._mas_event_init_lockdb[ev_label] = persistent._mas_event_init_lockdb_template

        # Unlock start_date and end_date
        Event.unlockInit("start_date", ev_label=ev_label)
        Event.unlockInit("end_date", ev_label=ev_label)


python early:

    ## Delete 00_-files and replace with aa_ ones.

    import os

    for cd, _, files in os.walk(renpy.config.gamedir):
        # Ensure we don't touch any other data
        if "MAS Self Harm Submod" not in cd:
            continue

        for _file in files:
            # Ensure we have aa_ file
            new_file = os.path.join(cd, "aa_" + _file[3:])
            if not _file.startswith("00_") or not os.path.exists(new_file):
                continue

            # Delete 00_ file
            os.remove(os.path.join(_file))