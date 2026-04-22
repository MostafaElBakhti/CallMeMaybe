import argparse

def parse_args():
    parse = argparse.ArgumentParser(
        description="prompt to jsong "
    )

    parse.add_argument(
        "--input",
        type=str,
        default="data/input/function_calling_tests.jsong"
    )

    parse.add_argument(
        "--function_definitions",
        type=str,
        default="data/input/function_definition.jsong"
    )

def main():
    print("starting...")
    args = parse_args()