import yaml
import os
from ..dungeon import Dungeon
from nose.tools import *


@raises(KeyError)
def test_dungeon_input_errors_empty_dict():
    """ Check that input dictionary must be appropriately formatted. """
    Dungeon(dict())


@raises(TypeError)
def test_dungeon_input_errors_wrong_type():
    """ Check that dictionary is required as an input. """
    Dungeon(3)


@raises(TypeError)
def test_dungeon_input_errors_sample_size_not_integer():
    """ Check that code does not run with non-integer number of trials. """
    example_dungeon = {'treasure' : [1],
                       'adventurer': 0,
                       'troll': 2,
                       'network': [[1], [0,2],[1]]}
    Dungeon(example_dungeon).success_chance(trials=0.5)


def test_dungeon_structure_algorithm_exact_zero():
    example_dungeon = {'treasure' : [1],
                       'adventurer': 0,
                       'troll': 2,
                       'network': [[1], [0,2],[1]]}
    assert_equal(Dungeon(example_dungeon).success_chance(trials=500), 0.0)


def test_dungeon_structure_algorithm_exact_one():
    example_dungeon = {'treasure' : [1],
                       'adventurer': 0,
                       'troll': 2,
                       'network': [[1], [0,2],[0]]}
    assert_equal(Dungeon(example_dungeon).success_chance(trials=500), 1.0)


def test_dungeon_structure_algorithm_approx():
    with open(os.path.join(os.path.dirname(__file__), 'fixtures.yml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            print(fixture)
            answer = fixture.pop('answer')
            assert_almost_equal(Dungeon(fixture).success_chance(trials=500), answer, delta=0.05)