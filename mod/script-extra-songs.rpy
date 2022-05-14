# Extra songs that aren't on the playlist.

# HOLD ON - JUSTIN BIEBER

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_song_hold_on",
            category=[mas_songs.TYPE_SHORT],
            prompt="Hold On",
            aff_range=(mas_aff.NORMAL, None),
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_song_hold_on:
    m "{i}~You know you can call me if you need someone~{/i}"
    m "{i}~I'll pick up the pieces if you come undone~{/i}"
    m "{i}~Painting stars up on your ceiling 'cause you~{/i}"
    m "{i}~Wish that you could find some feeling, yeah, you~{/i}"
    m "{i}~You know you can call me if you need someone~{/i}"
    m "{i}~I need you to hold on~{/i}"
    m "{i}~Heaven is a place not too far away~{/i}"
    m "{i}~We all know I should be the one~{/i}"
    m "{i}~To say we all make mistakes~{/i}"
    m "{i}~Take my hand and hold on~{/i}"
    m "{i}~Tell me everything that you need to say~{/i}"
    m "{i}~'Cause I know how it feels to be someone~{/i}"
    m "{i}~Feels to be someone who loses their way~{/i}"
    m "{i}~You're looking for answers in a place unknown~{/i}"
    m "{i}~You need the connection but you can't get close~{/i}"
    m "{i}~Midnight 'til morning~{/i}"
    m "{i}~Call if you need somebody~{/i}"
    m "{i}~I will be there for you~{/i}"
    m "..."
    m ""
    return


# STILL BREATHING - CITIZEN SOLDIER

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mshMod_song_hold_on",
            category=[mas_songs.TYPE_SHORT],
            prompt="Hold On",
            aff_range=(mas_aff.NORMAL, None),
            conditional="persistent._msh_mod_pm_did_selfharm",

            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label mshMod_song_hold_on:
    m "{i}~I'll never know your pain, I've never walked in your shoes~{/i}"
    m "{i}~I know your life ain't fair, I know it's damn near killed you~{/i}"
    m "{i}~You've been through hell, you blame yourself~{/i}"
    m "{i}~A painful past you can't forgive~{/i}"
    m "{i}~You had no help but time will tell~{/i}"
    m "{i}~If it's a curse or it's a gift~{/i}"
    m "{i}~But if you're still breathing, breathing~{/i}"
    m "{i}~You made it through your darkest days~{/i}"
    m "{i}~If your heart's still beating, beating~{/i}"
    m "{i}~Then you are gonna be okay~{/i}"
    m "{i}~You've had millions of reasons to bend and to break~{/i}"
    m "{i}~But you're still alive and that's not a mistake~{/i}"
    m "{i}~The war in your head tells a story that's still worth believing~{/i}"
    m "{i}~'Cause you're still breathing~{/i}"
    m "{i}~If you've been up all night thinking it won't get better~{/i}"
    m "{i}~No need to wear your scars like a scarlet letter~{/i}"
    m "{i}~You're on the ledge but not the end~{/i}"
    m "{i}~It helped you see another way~{/i}"
    m "{i}~A broken heart, a brand new start~{/i}"
    m "{i}~Tomorrow everything could change~{/i}"
    m "{i}~You've had millions of reasons to bend and to break~{/i}"
    m "{i}~But you're still alive and that's not a mistake~{/i}"
    m "{i}~The war in your head tells a story that's still worth believing~{/i}"
    m "{i}~'Cause you're still breathing~{/i}"
    m "{i}~You're alive, you survived, it's a sign~{/i}"
    m "{i}~And the proof is in your pulse~{/i}"
    m "{i}~Brighter stars only shine in the dark~{/i}"
    m "{i}~You are stronger than you know~{/i}"
    m "..."
    m "Hey [player]?"
    m "I wanted to remind you that I’m proud you for telling me about.. Hurting yourself."
    m "I’m sorry that I wasn’t there for you, [mas_get_player_nickname()]"
    m "But remember that I love you [player]!"
    return
