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

    parse.add_argument(
        "--output",
        type=str,
        default="data/output/functions_results.json"
    )

    parse.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen3-0.6B"
    )

    return parse.parse_args()

def main():
    print("starting...")
    args = parse_args()

    print(vars(args))
    print(args["input"])

main()