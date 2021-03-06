scarab = genMonster("Scarab", 83, 6024)
scarab.health(320, healthmax=320)
scarab.type("slime")
scarab.defense(armor=23, fire=1.18, earth=0, energy=0.9, ice=0.8, holy=1, death=1, physical=0.95, drown=1)
scarab.experience(120)
scarab.speed(170)
scarab.behavior(summonable=395, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=80)
scarab.walkAround(energy=1, fire=1, poison=0)
scarab.immunity(paralyze=1, invisible=0, lifedrain=0, drunk=0)
scarab.melee(75)
scarab.loot( ("scarab coin", 1.0), ("piece of scarab shell", 4.5), (2148, 100, 52), ("meat", 40.0, 2), ("small amethyst", 0.5), ("daramanian mace", 0.25), ("small emerald", 0.25) )