default persistent._msh_mod_technique_database = dict()

# init 5 python:
#     addEvent(
#         Event(
#             persistent._msh_mod_technique_database,
#             eventlabel="mshMod_technique_sample",
#             prompt="This is a sample technique",
#             unlocked=False
#         )
#     )
#
# label mshMod_technique_sample:
#     m "This is a sample technique dialogue."
#     return

init -100 python:
    _mshMod_TECHNIQUE_MENU_EXIT_ITEM = ("Nevermind", "exit", False, False)


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_technique_menu",
            category=['Self-harm'],
            prompt="Can you tell me about some techniques?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_technique_menu:
    m "Sure, [mas_get_player_nickname()]!"

    python:
        items = list(map(
            lambda it: (it.prompt, it.eventlabel, False, False),
            Event.filterEvents(
                persistent._msh_mod_technique_database,
                unlocked=True
            )
        ))

    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, _mshMod_TECHNIQUE_MENU_EXIT_ITEM)
    if _return == "exit":
        m "Oh, okay..."
        return

    pushEvent(_return)

    return
