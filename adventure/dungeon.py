import random
import copy


class Dungeon(object):

    """
    The following code is a simpler version (random strategy, no
    intelligence involved) of the famous Hunt the Wumpus game.
    
    For initialisation the class requires a dictionary input with following keys:
    - treasure (starting location of treasure, value must be integer)
    - adventurer (location of adventurer, value must be integer)
    - troll (starting location of troll, value must be integer)
    - network (dungeon structure, value must be a list, where each elements
      specifies a room in the dungeon and the numbers in given element
      exit options, i.e. list[[2], [0,2], [1]] would mean that there are
      3 rooms and room 1 has exit to rooms 0 and 2.)
      
    Main function (success_chance) executes random move strategy
    multiple times (number of trials is optional argument, with default
    trials = 500) and returns the probability of adventurer successfully
    finding the treasure without being eaten by the troll.
    """

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

    def success_chance(self, trials=500, successes=0):
        if not (type(trials) == int) or not trials > 0:
            raise ValueError("The number of samples must be a positive integer!")
        for n in range(trials):
            outcome = self.run_to_result()
            if outcome == 1:
                successes += 1
        success_fraction = successes / trials
        return success_fraction