init -810 python:
    store.mas_history.addMHS(MASHistorySaver(
        "msh_mod_pm",
        datetime.datetime(2019, 1, 1),
        {
            "_msh_mod_pm_did_selfharm": "pm.emotions.did_selfharm",
            "_msh_mod_pm_sober_streak": "pm.emotions.selfharm_sober_streak"
        },
        use_year_before=True,
        dont_reset=True
    ))
