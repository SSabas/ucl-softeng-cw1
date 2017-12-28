import yaml
import os
from ..dungeon import Dungeon
from nose.tools import *

def test_dungeon_structurers():

    with open(os.path.join(os.path.dirname(__file__),
            'fixtures','samples.yml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            print(fixture)
            answer=fixture.pop('answer')
            assert_almost_equal(Dungeon(fixture).success_chance(trials=500), answer, delta=0.1)

# @raises(KeyError)
# def test_Exception3():
#     '''this test should fail (IndexError raised but KeyError was expected)'''
#     l.pop()

@raises(KeyError)
def test_dungeon_input_errors_empty_dict():
    Dungeon(dict())

@raises(TypeError)
def test_dungeon_input_errors_wrong_type():
    Dungeon(3)

@raises(TypeError)
def test_dungeon_input_errors_not_integer():
    example_dungeon = {'treasure' : [1],
                       'adventurer': 0,
                       'troll': 2,
                       'network': [[1], [0,2],[1]]
                       }
    Dungeon(example_dungeon).success_chance(trials = 0.5)