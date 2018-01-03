from adventure.dungeon import Dungeon
from argparse import ArgumentParser
import yaml


def parse_args():
    parser = ArgumentParser(description="Automatic hunt for the treasure. "
                                        "Runs the script multiple times and "
                                        "outputs the probability of reaching the "
                                        "treasure. Input file must be in YAML "
                                        "format and with correct dungeon structure "
                                        "(see Dungeon class for example).")
    parser.add_argument('file', help='Path to YAML file to load dungeon structure.')
    parser.add_argument('--samples', default=500, type=int,
                        help='Number of samples to be drawn. Must be positive integer.')
    arguments = parser.parse_args()
    cfgdata = {"from_file": arguments.file,
               "sample_size": arguments.samples}
    return cfgdata


def load_config(config_filename):
    cfgfile = open(config_filename, 'r')
    cfgdata = yaml.load(cfgfile)
    cfgfile.close()
    return cfgdata


def run_dungeon():
    cfgdata = parse_args()
    dungeon_structure = load_config(cfgdata["from_file"])
    test_dungeon = Dungeon(dungeon_structure)
    return print(test_dungeon.success_chance(trials=cfgdata["sample_size"]))


if __name__ == "__main__":
    run_dungeon()