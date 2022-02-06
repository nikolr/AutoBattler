""""Hold information and methods used to manipulate character groups"""
from collections import deque

from character import Character


class BattleGroups():
    def __init__(self, player_squad: list[Character], enemy_squad: list[Character]):
        self.player_squad_queue = deque()
        for i in range(0, len(player_squad)):
            self.player_squad_queue.append(player_squad[i])

    def remove_dead_characters(self):
        for c in self.player_squad_queue:
            if c.alive == False:
                self.player_squad_queue.remove(c)

    def battle(self, ps: Character, es: Character) -> bool:
        """Calculates the trade between the first in line characters of ps and es. Should tirgger on hit / on death effects. Where those are handled is still not determined
        Possibly in battle_state.trigger_events? Just here?
        Returns True if characters died"""
        turn_order = self.speed_check(ps, es)

        attacked_character_died = turn_order[1].take_damage(turn_order[0])
        #Check for character on hit effects.



        if attacked_character_died:
            pass

    def get_list(self):
        l = []
        for c in self.player_squad_queue:
            l.append(c.name)
        return l
    
    def speed_check(self, c1: Character, c2: Character):
        """Returns character tuple, where the faster unit (the one that gets to attack first) is the first entry. c1 wins draws"""
        if c1.speed <= c2.speed:
            return (c1, c2)
        else:
            return (c2, c1)
        