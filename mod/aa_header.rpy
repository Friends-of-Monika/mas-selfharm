init -990 python in mas_submod_utils:
    if not store.mshMod_update.zeroFilesRemoved:
        Submod(
            author="MAS Self Harm Submod Team",
            name="MAS Self Harm Submod",
            description="Awareness about self-harm and support to self-harmers, with different "
                        "techniques, milestones, checkups and new dialogue and spritepacks.",
            version="1.0.7",
            version_updates={
                "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_6": "mas_self_harm_submod_team_mas_self_harm_submod_v1_0_7"
            }
        )

init -989 python:
    if not store.mshMod_update.zeroFilesRemoved:
        if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
            store.sup_utils.SubmodUpdater(
                submod="MAS Self Harm Submod",
                user_name="my-otter-self",
                repository_name="mas_selfharm",
                extraction_depth=3
            )
