default persistent._msh_mod_next_reminder_trigger = None

# init 5 python:
#     import datetime
#     addEvent(Event(persistent.event_database,eventlabel="monika_rem",random=True,rules={"force repeat": None}))
#
# label monika_rem:
#     $ persistent._last_topic_run = datetime.datetime.utcnow()
#     $ mas_globals.this_ev.action = EV_ACT_PUSH
#     $ mas_globals.this_ev.conditional = "datetime.datetime.utcnow() - persistent._last_topic_run > datetime.timedelta(minutes=7200)"
#
#     python:
#         time = datetime.datetime.now().hour
#     if 0 <= time < 24:
#         if time == 0:
#             $ time = 24
#         m "Hey, [player]?"
#         m "I just wanna check up on you!"
#         m "Sometimes I get worried about you."
#         m "How have you been doing?"
#         menu:
#             "I'm okay, [m_name].":
#                 m "I'm super happy to hear that!"
#                 m "If anything happens, let me know, okay?"
#                 m "I love you soooo much!"
#
#             "I've been kind of down lately.":
#                 m "I'm so sorry to hear that, [player]."
#                 m "I'm sure everything will be okay!"
#                 m "Your loving girlfriend will forever be here for you!"
#                 m "If you ever want to talk, please let me know."
#                 m "I care for you so much!"
#                 m "I love you!"
#
#
#         return "no_unlock|love"


init 5 python in mshMod_reminder:
    def remind(delay):
        persistent._msh_mod_next_reminder_trigger = datetime.datetime.now() + delay

    def stop():
        persitent._msh_mod_next_reminder_trigger = None


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder",
            conditional="persistent._msh_mod_next_reminder_trigger and "
                        "datetime.datetime.now() >= persistent._msh_mod_next_reminder_trigger",
            action=EV_ACT_PUSH,
            rules={"force repeat": None}
        )
    )

label mshMod_medication_reminder:
    $ store.mshMod_reminder.remind(datetime.timedelta(day=1))
    m "Here's your reminder, [player]; next one will trigger after [persistent._msh_mod_next_reminder_trigger]."
    return "no_unlock"
