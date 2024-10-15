def take_magic_damage(health, resist, amp, spell_power):
    damage = (spell_power * amp) - resist
    newHealth = health - damage
    return newHealth