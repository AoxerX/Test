"""
Initialisation Settings
"""
save_world_view = True
fig_size = 20  # pixel size is fig_size x dpi

world = dict(
    settings=dict(
        seed='rt0_t0-cs_L-001',
        rows=100,
        columns=100,
        fertile_lands=[[[20, 20], [79, 79]]],
        init_food=500,
        init_bugs=100
    ),
    food_spawn_vals=dict(
        energy=20,
        reproduction_threshold=24,
        energy_max=100
        # TODO: food & bug taste
    ),
    bug_spawn_vals=dict(
        energy=20,
        reproduction_threshold=50,
        energy_max=100
    )
)

food_endangered_threshold = 999999999
bug_endangered_threshold = 0

food = dict(
    growth_rate=4,

    # Evolution switches
    evolve_reproduction_threshold=True,
    reproduction_threshold_mutation_limit=5,

    evolve_taste=True,
    taste_mutation_limit=10
)

bug = dict(
    respiration_rate=3,
    eat_tax=1,

    # Evolution switches
    evolve_reproduction_threshold=True,
    reproduction_threshold_mutation_limit=5,

    evolve_taste=True,
    taste_mutation_limit=10
)
