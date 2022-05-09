import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', help='Config file with execution properties. By default config.ini is used',
                        type=str, default="config.ini")
    parser.add_argument('--reuse', '-r', help='Reuse test data from previous execution', action="store_true")
    parser.add_argument('--appliance', '-a', help='Run appliance console tests and skip not needed setup',
                        action="store_true")
    parser.add_argument('--collectonly', '-collect', help='Only collect tests, does not execute them',
                        action="store_true")
    args = parser.parse_args()
    return args
