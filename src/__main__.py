import argparse
from .models.validation import function_definition_check, prompt_check
from .models.decoding import system_prompt_builder


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
        "--functions_definition",
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

    functions = function_definition_check(args.functions_definition)
    if not functions:
        raise RuntimeError(f"function definitions file is empty, please check {args.function_definitions}")

    for f in functions:
        print(f)
        print("-" * 20)

    # prompts = prompt_check(args.input)
    # if not prompts:
    #     raise RuntimeError(f"prompt file is empty, please check {args.input}")

    # for p in prompts:
    #     print(p)

    sys_prompt = system_prompt_builder(functions)
    print("\n===== SYSTEM PROMPT =====\n")
    print(sys_prompt)


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print(f"An error occurred: {e}")



