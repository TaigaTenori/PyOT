instant = spell.Spell("Strong Ice Wave", "exevo gran frigo hur", icon=43, group=ATTACK_GROUP)
instant.require(mana=170, level=40, maglevel=0, learned=0, vocations=(2, 6))
instant.cooldowns(8, 2)
instant.area(AREA_WAVE2)
instant.targetEffect(callback=spell.damage(4.5, 7.6, 20, 48, ICE))
instant.effects(area=EFFECT_ICEAREA)