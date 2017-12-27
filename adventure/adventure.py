'''
The following code is a simpler version (random strategy, no intelligence involved) of the famous Hunt the Wumpus game.
'''

import random
import copy

class dungeon(object):

    def __init__(self, dungeon):
        self.treasure = dungeon['treasure']
        self.adventurer = dungeon['adventurer']
        self.troll = dungeon['troll']
        self.network = dungeon['network']

    def describe_network(self):
        print("Treasure at ", self.treasure,
              ".\n Adventurer at ", self.adventurer,
              ".\n Troll at ", self.troll,
              ".\n Current network is ", self.network,
              sep = "")

    def random_move_adventurer(self):
        self.adventurer = random.choice(self.network[self.adventurer])

    def random_move_troll(self):
        self.troll = random.choice(self.network[self.troll])

    def update_dungeon(self):
        self.random_move_adventurer()
        self.random_move_troll()

    def outcome(self):
        if self.adventurer == self.troll:
            return -1
        if self.adventurer in self.treasure:
            return 1
        return 0

    def copy_dungeon(self):
        return copy.deepcopy(self)

    def run_to_result(self, max_steps=1000):
        iterable = self.copy_dungeon()
        for x in range(max_steps):
            result = iterable.outcome()
            if result != 0:
                return result
            iterable.update_dungeon()
        # don't run forever, return 0 (e.g. if there is no treasure and the troll can't reach the adventurer)
        return result

    def success_chance(self, trials=10000, successes=0):
        for n in range(trials):
            outcome = self.run_to_result()
            if outcome == 1:
                successes += 1
        success_fraction = successes / trials
        return success_fraction


dungeon1 = {
 'treasure' : [1], # Room 1 contains treasure
 'adventurer': 0, # The adventurer starts in room 0
 'troll': 2, # The troll starts in room 2
 'network': [[1], #Room zero connects to room 1
 [0,2], #Room one connects to rooms 0 and 2
 [1] ] #Room 2 connects to room 1
}


dungeon2 = {
 'treasure' : [1], # Room 1 contains treasure
 'adventurer': 0, # The adventurer starts in room 0
 'troll': 2, # The troll starts in room 2
 'network': [[1], #Room zero connects to room 1
 [0,2], #Room one connects to rooms 0 and 2
 [1,3], #Room 2 connects to room 1 and 3
 [2]] # Room 3 connects to room 2
}
