import argparse
import json
from typing import Dict
from pydantic import BaseModel

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


# def function_definition_check(path):
#     try:
#         with open(path, "r") as f:
#             data = json.load(f)
#     except Exception as e:
#         print(f"Error occurred while reading {path}: {e}")
#         raise Exception("file not found , or permissions denied")

#     if not isinstance(data, list):
#         print(f"Invalid format: Expected a list "
#               f"of function definitions in {path}")
#         raise ValueError(f" format error ")

#     for value in data:
#         if not isinstance(value, dict):
#             print(f"Invalid format: Each function definition should be a dictionary in {path}")
#             raise ValueError(f" format error ")

#         if "name" not in value or not isinstance(value["name"], str):
#             print(f"Invalid format: Each function definition should have a 'name' key of type string in {path}")
#             raise ValueError(f" format error ")
        
#         if "description" not in value or not isinstance(value["description"], str):
#             print(f"Invalid format: Each function definition should have a 'description' key of type string in {path}")
#             raise ValueError(f" format error ")

#         if "parameters" not in value or not isinstance(value["parameters"], dict):
#             print(f"Invalid format: Each function definition should have a 'parameters' key of type dictionary in {path}")
#             raise ValueError(f" format error ")
        
#         for item, item_value in value["parameters"].items():
#             if not isinstance(item, str):
#                 print(f"Invalid format: Each parameter name should be a string in {path}")
#                 raise ValueError(f" format error ")
#             if not isinstance(item_value, dict):
#                 print(f"Invalid format: Each parameter description should be a dictionary in {path}")
#                 raise ValueError(f" format error ")
            
#             if not "type" in item_value or not isinstance(item_value["type"], str):
#                 print(f"Invalid format: Each parameter description should have a 'type' key of type string in {path}")
#                 raise ValueError(f" format error ")
        
#         if "returns" not in value or not isinstance(value["returns"], dict):
#             print(f"Invalid format: Each function definition should have a 'returns' key of type dictionary in {path}")
#             raise ValueError(f" format error ")
        
#         if "type" not in value["returns"] or not isinstance(value["returns"]["type"], str):
#             print(f"Invalid format: The 'returns' key should have a 'type' key of type string in {path}")
#             raise ValueError(f" format error ")

#     return data 
class Parameter(BaseModel):
    type: str

class Returns(BaseModel):
    type: str

class Function(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Parameter]
    returns: Returns


def function_definition_check(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error occurred while reading {path}: {e}")
        raise Exception("file not found , or permissions denied")
    
    validated = []

    for item in data:
        try:
            func = Function.model_validate(item)
            validated.append(func)
        except Exception as e:
            print(f"Error occurred while validating function definition: {e}")
            raise Exception("format error")

    return validated

def main():
    print("starting...")
    args = parse_arguments()

    print(args.input)
    print(args.output)
    print(args.function_definitions)
    # print(vars(args))
    # print(args["input"])
    # try:
    #     with open(args.input, "r") as f:
    #         inputs = json.load(f)
    #     print(f"inputs : {inputs}")
    # except Exception as e :
    #     print(e)

    # try:
    #     with open(args.function_definitions, "r") as f:
    #         function_definitions = json.load(f)
    #     print(f"function_definitions : {function_definitions}")
    # except Exception as e:
    #     print(e)
    try :
        ft_def = function_definition_check(args.function_definitions)
        print(f"{ft_def}")
        # print(" function definitions loaded and validated")
    except Exception as e:
        print(e)

main()