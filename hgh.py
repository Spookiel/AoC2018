import re
import itertools
from copy import deepcopy
from enum import auto, Enum
from dataclasses import dataclass
from typing import FrozenSet

class Army(Enum):
    IMMUNE_SYSTEM = auto()
    INFECTION = auto()

class Damage(Enum):
    COLD = auto()
    FIRE = auto()
    SLASHING = auto()
    RADIATION = auto()
    BLUDGEONING = auto()

class Stalemate(Exception):
    pass

@dataclass
class Unit:
    army: Army
    count: int
    hp: int
    damage: int
    attack: Damage
    initiative: int
    weaknesses: FrozenSet[Damage] = frozenset()
    immunities: FrozenSet[Damage] = frozenset()

    def __hash__(self): return id(self)  # allow using units in dictionaries

    @classmethod
    def parse(cls, army, val):
        (count, hp, mods, damage, attack, initiative) = re.match(
            r'(\d+) units each with (\d+) hit points(?: \((.*?)\))?'
            r' with an attack that does (\d+) (\w+) damage at initiative (\d+)'
        , val).groups()

        kwargs = {}

        if mods:
            for mod in mods.split('; '):
                modifier, _, types = mod.split(' ', 2)
                damages = frozenset(Damage[damage.upper()] for damage in types.split(', '))
                if modifier == 'weak':
                    kwargs['weaknesses'] = damages
                elif modifier == 'immune':
                    kwargs['immunities'] = damages

        return cls(army=army, count=int(count), hp=int(hp), damage=int(damage),
            attack=Damage[attack.upper()], initiative=int(initiative), **kwargs)

    @property
    def effective_power(self):
        return self.count * self.damage

    def damage_dealt(self, other):
        if self.attack in other.immunities:
            return 0
        elif self.attack in other.weaknesses:
            return self.effective_power * 2
        else:
            return self.effective_power

def round(armies):
    targets = {}
    attacking = {}

    for group in sorted(armies, key=lambda group: (group.effective_power, group.initiative), reverse=True):
        if group.count <= 0:
            continue

        enemies = [enemy for enemy in armies if enemy.army != group.army]
        enemies = sorted(enemies, key=lambda enemy: (group.damage_dealt(enemy), enemy.effective_power, enemy.initiative), reverse=True)
        target = next((enemy for enemy in enemies if enemy.count > 0 and group.damage_dealt(enemy) and enemy not in targets), None)

        if not target:
            continue

        targets[target] = group
        attacking[group] = target

    stalemate = True

    for group in sorted(armies, key=lambda group: group.initiative, reverse=True):
        if group.count > 0 and attacking.get(group):
            target = attacking[group]
            killed = min(group.damage_dealt(target) // target.hp, target.count)

            if killed:
                target.count -= killed
                stalemate = False

    if stalemate:
        raise Stalemate()

    return armies

def fight(armies, boost=0):
    armies = deepcopy(armies)

    for group in armies:
        if group.army == Army.IMMUNE_SYSTEM:
            group.damage += boost

    while all(any(group.count for group in armies if group.army == army) for army in Army):
        armies = round(armies)

    return armies

armies = []
data = """Immune System:
228 units each with 8064 hit points (weak to cold) with an attack that does 331 cold damage at initiative 8
284 units each with 5218 hit points (immune to slashing, fire; weak to radiation) with an attack that does 160 radiation damage at initiative 10
351 units each with 4273 hit points (immune to radiation) with an attack that does 93 bludgeoning damage at initiative 2
2693 units each with 9419 hit points (immune to radiation; weak to bludgeoning) with an attack that does 30 cold damage at initiative 17
3079 units each with 4357 hit points (weak to radiation, cold) with an attack that does 13 radiation damage at initiative 1
906 units each with 12842 hit points (immune to fire) with an attack that does 100 fire damage at initiative 6
3356 units each with 9173 hit points (immune to fire; weak to bludgeoning) with an attack that does 24 radiation damage at initiative 9
61 units each with 9474 hit points with an attack that does 1488 bludgeoning damage at initiative 11
1598 units each with 10393 hit points (weak to fire) with an attack that does 61 cold damage at initiative 20
5022 units each with 6659 hit points (immune to bludgeoning, fire, cold) with an attack that does 12 radiation damage at initiative 15

Infection:
120 units each with 14560 hit points (weak to radiation, bludgeoning; immune to cold) with an attack that does 241 radiation damage at initiative 18
8023 units each with 19573 hit points (immune to bludgeoning, radiation; weak to cold, slashing) with an attack that does 4 bludgeoning damage at initiative 4
3259 units each with 24366 hit points (weak to cold; immune to slashing, radiation, bludgeoning) with an attack that does 13 slashing damage at initiative 16
4158 units each with 13287 hit points with an attack that does 6 fire damage at initiative 12
255 units each with 26550 hit points with an attack that does 167 bludgeoning damage at initiative 5
5559 units each with 21287 hit points with an attack that does 5 slashing damage at initiative 13
2868 units each with 69207 hit points (weak to bludgeoning; immune to fire) with an attack that does 33 cold damage at initiative 14
232 units each with 41823 hit points (immune to bludgeoning) with an attack that does 359 bludgeoning damage at initiative 3
729 units each with 41762 hit points (weak to bludgeoning, fire) with an attack that does 109 fire damage at initiative 7
3690 units each with 36699 hit points with an attack that does 17 slashing damage at initiative 19"""
for group in data.split('\n\n'):
    name, *units = group.splitlines()

    army = Army[name.replace(':', '').replace(' ', '_').upper()]

    armies.extend(Unit.parse(army, line) for line in units)

result = fight(armies)

print('part 1:', sum(group.count for group in result if group.army == Army.INFECTION))

for boost in itertools.count(1):
    try:
        result = fight(armies, boost=boost)
    except Stalemate:
        continue
    else:
        if all(group.count == 0 for group in result if group.army == Army.INFECTION):
            break

print('part 2:', sum(group.count for group in result if group.army == Army.IMMUNE_SYSTEM))