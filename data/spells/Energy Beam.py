instant = spell.Spell("Energy Beam", "exevo vis lux", icon=22, group=ATTACK_GROUP)
instant.require(mana=40, level=23, maglevel=0, learned=0, vocations=(1, 5))
instant.cooldowns(4, 2)
instant.area(AREA_BEAM4)
instant.targetEffect(callback=spell.damage(1.8, 3, 11, 19, ENERGY))
instant.effects(area=EFFECT_ENERGYAREA)