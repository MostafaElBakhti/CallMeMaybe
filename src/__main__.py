import argparse
from .models.validation import function_definition_check, prompt_check


def parse_arguments():
    parse = argparse.ArgumentParser(
        description="prompt to json "
    )

    parse.add_argument(
        "--input",
        type=str,
        default="data/input/function_calling_tests.json"
    )

    parse.add_argument(
        "--function_definitions",
        type=str,
        default="data/input/functions_definition.json"
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
    args = parse_arguments()

    ft_def = function_definition_check(args.function_definitions)
    if not ft_def:
        raise RuntimeError(f"function definitions file is empty, please check {args.function_definitions}")

    for f in ft_def:
        print(f)

    prompts = prompt_check(args.input)
    if not prompts:
        raise RuntimeError(f"prompt file is empty, please check {args.input}")

    for p in prompts:
        print(p)


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print(f"An error occurred: {e}")