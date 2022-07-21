# This is a 'invalid install trap', script that shows an unignoreable error
# if submod is attempted to compile at wrong install location.

init -10000 python:

    path, line = renpy.get_filename_line()
    if "game/Submods/MAS Self Harm Submod" not in path.replace('\\', '/'):
        raise RuntimeError(""
            "\n\n\n\n\n!!! PLEASE READ THIS !!!\n\n"
            "You have installed MAS Self-Harm Submod into wrong location.\n"
            "Please follow instructions in the README (scroll down on the repository homepage)\n"
            "in order to get this submod to work.\n\n"
            "If you're still having trouble installing mod, feel free to ask us\n"
            "for help on our Discord: https://mon.icu/discord."
            "\n\n\n\n\n\n\n\n\n\n\n\n"
        )
