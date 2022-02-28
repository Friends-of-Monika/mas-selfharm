init -810 python:
    store.mas_history.addMHS(MASHistorySaver(
        "monika_selfharm_pm",
        datetime.datetime(2019, 1, 1),
        {
            "_mas_pm_did_selfharm": "pm.emotions.did_selfharm"
        },
        use_year_before=True,
        dont_reset=True
    ))
