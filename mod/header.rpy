# A tribute to all of the people taking part in making this submod. Thank you, everyone!
# Things were really nice while they lasted, and it was pleasure working with you.
# It's a shame we had to part our ways like that, I hope everyone is alright out there.
#
# Without you, there wouldn't be Self-Harm submod:
#
#   * Otter
#   * dreamscached
#   * DjMayJay
#   * Kitakus
#   * MaliciousSoftware
#   * AmyKawa
#   * charliethecookie
#   * WentPostal
#   * HistoryVariety
#   * FellTheSimp
#   * lukilak
#   * Raider0401
#   * plushika_2137
#   * Tourist_Easy
#   * MysticCreatesGames1
#   * fukawabunny
#   * ImKventis
#   * LOeufmf
#   * Rhea
#   * Feenie
#
# Thank you, MAS Self Harm Submod Team; we'll take it from here.
# - Friends of Monika

init -990 python in mas_submod_utils:
    Submod(
        author="Friends of Monika",
        coauthors=["former MAS Self Harm Submod Team"],
        name="Self Harm Awareness Submod",
        description="Awareness about self-harm and support to self-harmers, with different "
                    "techniques, milestones, checkups and new dialogue and spritepacks.",
        version="2.0.2"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Self Harm Awareness Submod",
            user_name="friends-of-monika",
            repository_name="mas-selfharm",
            extraction_depth=3
        )

init -100 python in mshMod:
    import os

    def get_script_file(fallback=None, relative=False):
        """
        Uses internal Ren'Py function renpy.get_filename_line() to locate
        current script file and get its location, accounting for potential
        erroneous outputs produced by this function.

        IN:
            fallback -> str, default None:
                Path to use as a fallback in case this function fails to find
                appropriate current script location.

            relative -> bool, default False:
                True if function should omit "game/" from detected path to make
                it relative to "game/" folder.

        OUT:
            str:
                Relative (to DDLC directory) path to the .rpy script file that
                is currently being executed, or fallback value (or None if not
                provided) if this function is unable to find appropriate path.

        RAISES:
            ValueError:
                If fallback does not start with "game/" and relative is set to
                False.

        NOTE:
            For consistency between platforms (and further usage in Ren'Py
            functions and related things) paths returned always have "/" as
            folder separator, even on Windows.

            Also note that even though it is possible for script file to be
            located not in "game/" folder for somewhere else, this function
            assumes it is located in "game/" and uses this assumption in its
            path correction logic.

            Proper functionality of this function cannot be guaranteed if called
            from eval() and alike dynamic code execution contexts.
        """

        if (
            fallback is not None and not fallback.startswith("game/") and
            not relative
        ):
            raise ValueError(
                "fallback path does not start with \"game/\" "
                "and relative is not True"
            )

        # Use renpy's developer function get_filename_line() to get current
        # script location. WARNING: THIS IS EXTREMELY UNSTABLE, THE FOLLOWING
        # CODE IS THE WORKAROUND THAT MAKES IT SOMEWHAT RELIABLE! Also replace
        # Windows \ (backslash) folder separators with / (slash) character
        # for consistency.
        path = renpy.get_filename_line()[0].replace("\\", "/")
        if os.path.isabs(path):
            # Returned path may be absolute, relativize it.
            path = os.path.relpath(path, renpy.config.renpy_base)

        # Split current file path into components. Our strategy here:
        # 1. Get path components.
        # 2. Check if path starts with game/ folder.
        # 3. While it does not, drop first i+1 (initially i=0) parts from it
        #    and prepend it with game/.
        # 4a. If new path from 3. exists, we most likely have got the right path.
        # 4b. If new path from 3. doesn't exist, increment i by 1 and drop more
        #     path components from the original path and repeat 3.
        parts = path.split("/")  # (1.)
        if parts[0] != "game":  # (2.)
            for n in range(1, len(parts)):  # (3.)
                parts_proc = parts[n:]
                parts_proc.insert(0, "game")

                rel_path = "/".join(parts_proc)
                if os.path.exists(os.path.join(renpy.config.renpy_base, rel_path)):
                    result = rel_path.replace("\\", "/")  # (4a.)
                    if relative:
                        # Omit "game/" prefix (5 chars.)
                        return result[5:]
                    return result

                # else (4b.)

            if fallback is not None and relative:
                return fallback[5:]  # Omit game/ prefix, its presence is checked above.
            return fallback.replace("\\", "/") if fallback is not None else None

        else:
            if relative:
                # Simply remove leading "game" item frm path parts.
                parts.pop(0)
            return "/".join(parts)

    basedir_rel = os.path.join(*get_script_file(
        fallback="Submods/Self Harm Awareness Submod/aa_header.rpy",
        relative=True
    ).split("/")[:-1])