# Player diary script.

define persistent._mshMod_created_diary = False
define mshMod_diary_path = config.basedir + "/characters/diary.txt"

#intro
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_writing_to_diary",
            category=["mental health"],
            prompt="What do you think about writing a diary?",
            pool=True,
            unlocked=True
        )
    )

label mshMod_writing_to_diary:
    $ shown_count = mas_getEVLPropValue("mshMod_writing_to_diary", "shown_count", 0)

    if shown_count == 0 or not persistent._mshMod_created_diary:
        jump mshMod_writing_to_diary_intro

    jump mshMod_writing_to_diary_repeat

label mshMod_writing_to_diary_intro:
    m 1lta "A diary, huh?"
    m 3eua "I've honestly been thinking about this for a bit."
    m 1huu "It can be a great outlet for anyone's emotions!"
    show monika 5rub at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rub "You could write your innermost feelings and thoughts..."
    show monika 4rub at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rub "Or even make it a mood journal, and write in it every day to observe patterns and possible triggers..."
    # m 3esb "You can even share it with someone you truly trust!"
    m 1hsa "If you'd like, I can create a text file for you to write your thoughts and memoirs into."

    m 1eua "Do you want me to create the diary for you?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want me to create the diary for you?{fast}"

        "Yes, please!":
            m 1hua "Great!"
            m 1nuu "I thought you would like that idea!"
            m 1dsc "..."

            play sound "sfx/glitch3.ogg"

            python:
                try:
                    f = open(mshMod_diary_path, "w")
                    f.write("For my one and only love <3")
                finally:
                    f.close()

            pause(0.5)
            $ persistent._mshMod_created_diary = True

            m 3esb "There you go!"
            m 1eua "It should be in the characters folder."
            m 1fkbsu "Make sure to write on it! I love you."

        "No, thanks.":
            m 1eka "Oh, I see..."
            m 1hua "That's okay!"
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "I just thought that it could be a neat idea."
            show monika 3hubsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 3hubsa "I always want what's best for you, [player]!"
            m 1fkbsu "I love you."

            return "love"

    $ mas_showEVL("mshMod_open_diary", "EVE", unlock=True)
    return

#diary reminder
label mshMod_writing_to_diary_repeat:
    m 3wua "[player]! {w=0.3}{nw}"
    extend 3wub "I just remembered something."
    m 2eku "I know it could be pretty personal stuff, so I haven't been looking..."

    m 1eta "But have you been writing in your diary?{nw}"
    $ _history_list.pop()
    menu:
        m "But have you been writing in your diary?{fast}"

        "I accidentally deleted it.":
            m 1fuu "Oh... hehe! That's alright."

            m 1eua "Would you like me to make you another one?{nw}"
            $ _history_list.pop()
            menu:
                m "Would you like me to make you another one?{fast}"

                # HOW COME it's been almost THREE years and we never noticed there's no
                # alternative, and there is just ONE option?
                "Sure!":
                    m 1hub "Alright!"
                    m 1dsc "..."

                    play sound "sfx/glitch3.ogg"

                    python:
                        try:
                            f = open(mshMod_diary_path, "w")
                            f.write("Don't lose this one, hehe~")
                        finally:
                            f.close()

                    pause(0.5)

                    m 3nuu "Don't delete this one, [player]!~"

                "It's okay.":
                    m 3hksdlb "Ah, alright then~"

        "Yeah, I've been working on it!":
            m 1hub "I'm happy to hear that, [player]!"
            show monika 5sub at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5sub "It's so nice to hear you're taking my advice."
            show monika 1hub at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 1hub"I love you!"

            return "love"

    return

init python:
    class _msh_note_multiline_input_obj(object):
        def __init__(self, initial_text=None, paper="paper", style="chibika_note_text"):
            self.initial_text = initial_text or ""
            self.current_value = initial_text or ""
            self.paper = paper
            self.style = style

        def get_caret_pos(self):
            widget = renpy.get_widget("_msh_note_multiline_input", "text_input", "screens")
            caret_pos = widget.caret_pos
            return caret_pos

        def set_caret_pos(self, new_pos):
            widget = renpy.get_widget("_msh_note_multiline_input", "text_input", "screens")
            widget.caret_pos = new_pos
            self.redraw_input()

        def redraw_input(self):
            widget = renpy.get_widget("_msh_note_multiline_input", "text_input", "screens")
            widget.update_text(widget.content, widget.editable)
            renpy.display.render.redraw(widget, 0)
            renpy.restart_interaction()

        def insert_newline(self):
            caret_pos = self.get_caret_pos()
            self.current_value = self.current_value[:caret_pos] + "\n" + self.current_value[caret_pos:]

            widget = renpy.get_widget("_msh_note_multiline_input", "text_input", "screens")
            widget.content = self.current_value
            widget.caret_pos = caret_pos + 1

            self.redraw_input()

        def update_text(self, new_text):
            self.current_value = new_text
            self.redraw_input()

        def move_to_home(self):
            caret_pos = self.get_caret_pos()
            line_start = self.current_value.rfind("\n", 0, caret_pos) + 1
            self.set_caret_pos(line_start)

        def move_to_end(self):
            caret_pos = self.get_caret_pos()
            line_end = self.current_value.find("\n", caret_pos)
            if line_end == -1:
                line_end = len(self.current_value)
            self.set_caret_pos(line_end)

        def move_caret(self, direction):
            lines = self.current_value.split("\n")
            caret_position = self.get_caret_pos()

            current_line = 0
            char_count = 0
            column = 0

            for i, line in enumerate(lines):
                if char_count + len(line) >= caret_position:
                    current_line = i
                    column = caret_position - char_count
                    break
                char_count += len(line) + 1
            else:
                current_line = len(lines) - 1
                column = len(lines[-1])

            if direction == "up":
                if current_line == 0:
                    self.set_caret_pos(0)
                else:
                    target_line = current_line - 1
                    new_start = sum(len(lines[i]) + 1 for i in range(target_line))
                    new_column = min(column, len(lines[target_line]))
                    self.set_caret_pos(new_start + new_column)

            elif direction == "down":
                if current_line == len(lines) - 1:
                    self.set_caret_pos(len(self.current_value))
                else:
                    target_line = current_line + 1
                    new_start = sum(len(lines[i]) + 1 for i in range(target_line))
                    new_column = min(column, len(lines[target_line]))
                    self.set_caret_pos(new_start + new_column)

# Based on mas_generic_poem
# https://github.com/Monika-After-Story/MonikaModDev/blob/06baf319a34c2ef585bc7c0a1e969a7eaa894b35/Monika%20After%20Story/game/screens.rpy#L3104-L3116
screen _msh_note_multiline_input(obj):
    style_prefix "poem"

    vbox:
        add obj.paper

    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40

        input value FieldInputValue(obj, "current_value") id "text_input":
            style obj.style
            changed obj.update_text
            pixel_width 650

        null height 100

    vbar value YScrollValue(viewport="vp") style "poem_vbar"
    key "K_RETURN" action Function(obj.insert_newline)
    key "K_UP" action Function(obj.move_caret, "up")
    key "K_DOWN" action Function(obj.move_caret, "down")
    key "noshift_K_HOME" action Function(obj.move_to_home)
    key "noshift_K_END" action Function(obj.move_to_end)

label msh_note_multiline_input(_default=None, paper="paper", style="chibika_note_text"):
    # Yes, [player] uses Chibika's font. Hurry to make a game theory based off that :)
    # - dreamscached

    $ _msh_note_obj = _msh_note_multiline_input_obj(_default, paper, style)
    window hide

    show screen _msh_note_multiline_input(_msh_note_obj)
    with Dissolve(1)
    $ pause()

    hide screen _msh_note_multiline_input
    with Dissolve(.5)
    window auto

    return _msh_note_obj.current_value

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_open_diary",
            category=["mental health"],
            prompt="Can I write something to my diary?",
            pool=True,
            rules={"no_unlock": None}
        )
    )

label mshMod_open_diary:
    m 1hua "Sure, give me a moment, I'll bring your diary!~"
    call mas_transition_to_emptydesk

    if os.path.exists(mshMod_diary_path):
        python:
            try:
                f = open(mshMod_diary_path, "r")
                diary_content = f.read()
            finally:
                f.close()

        $ renpy.pause(3.0, hard=True)
        call mas_transition_from_emptydesk("monika 3hua")
        m 3hua "Here!"

    else:
        $ renpy.pause(2.0, hard=True)
        m "Huh? I can't find it anywhere..."
        $ renpy.pause(2.0, hard=True)

        call mas_transition_from_emptydesk("monika 1dkc")
        m 1dkc "I'm sorry, [mas_get_player_nickname()]... {w=0.5}{nw}"
        extend 1lkc "I couldn't find it."

        m 1ekb "I can still give you a new sheet and let you write, what do you think?{nw}"
        $ _history_list.pop()
        menu:
            m "I can still give you a new sheet and let you write, what do you think?{fast}"

            "Sure.":
                $ diary_content = ""

            "No need to, [m_name].":
                m 3hkb "Ah, okay then!~"
                return

label mshMod_open_diary_loop:
    call msh_note_multiline_input(diary_content)
    $ diary_content = _return

    $ quip = renpy.substitute("Done writing, [player]?")
    m 2eub "[quip]{nw}"
    $ _history_list.pop()
    menu:
        m "[quip]{fast}"

        "Yes.":
            m 3eua "Alright, just a moment, I'll save your diary~"
            m 1dua ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"

            python:
                try:
                    f = open(mshMod_diary_path, "w")
                    f.write(diary_content)
                finally:
                    f.close()

            m 1hub "Done~"

        "Just a moment...":
            m 2eka "Ah, okay! Sorry, ehehe~"
            jump mshMod_open_diary_loop

    return
