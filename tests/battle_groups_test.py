import unittest
from collections import deque

from character import Character
from battle_groups import BattleGroups

class TestBattleGroups(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fighter = Character("fighter", 5, 5, 1, True)
        bm = Character("blackmage", 6, 3, 2,  True)
        paladin = Character("paladin", 2, 7, 2, True)

        wolf = Character("wolf", 8, 8, 4, False)

        cls.man = BattleGroups([fighter, bm, paladin])

    def test_battle_groups(self):
        self.assertEqual(self.man.get_list(), ["fighter", "blackmage", "paladin"])
        print(self.man.player_squad_queue.popleft().name)
    
if __name__ == '__main__':
    unittest.main()