# An Adventure In Packaging: An exercise in research software engineering
### An exercise for a course in Research Software Development in Python, at UCL.

The aim of exercise is to convert the already provided solution to the programming challenge defined in a Jupyter notebook, into a proper Python package.

Original source code:
~~~
import random
import copy

def random_move(network, current_loc):
 targets=network[current_loc]
 return random.choice(targets)

def update_dungeon(dungeon):
 dungeon['adventurer']=random_move(dungeon['network'], dungeon['adventurer'])
 dungeon['troll']=random_move(dungeon['network'], dungeon['troll'])

def outcome(dungeon):
 if dungeon['adventurer']==dungeon['troll']:
 return -1
 if dungeon['adventurer'] in dungeon['treasure']:
 return 1
 return 0
        
def run_to_result(dungeon):
 dungeon=copy.deepcopy(dungeon)
 max_steps=1000
 for _ in range(max_steps):
 result= outcome(dungeon)
 if result != 0:
 return result
 update_dungeon(dungeon)
 # don't run forever, return 0 (e.g. if there is no treasure and the troll can't rea
ch the adventurer)
 return result

def success_chance(dungeon):
 trials=10000
 successes=0
 for _ in range(trials):
 outcome = run_to_result(dungeon)
 if outcome == 1:
 successes+=1
 success_fraction = successes/trials
 return success_fraction
~~~