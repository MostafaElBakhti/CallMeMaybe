from typing import Dict
from pydantic import BaseModel
from pydantic import ValidationError
import json


class Parameter(BaseModel):
    type: str

class Returns(BaseModel):
    type: str

class Function(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Parameter]
    returns: Returns




class Prompt(BaseModel):
    prompt: str

def function_definition_check(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except RuntimeError as e:
        print(f"Error occurred while reading {path}: {e}")
        raise RuntimeError("file not found , or permissions denied, or invalid JSON format ")
    
    if not isinstance(data, list):
        raise RuntimeError("function definitions file must be a list")

    validated = []

    for item in data:
        try:
            func = Function.model_validate(item)
            validated.append(func)
        except ValidationError as e:
            print(f"Validation error:\n{e}")
            raise

    return validated

def prompt_check(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except RuntimeError as e:
        raise RuntimeError("file not found , or permissions denied, or invalid JSON format ")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON format: {e}")

    if not isinstance(data, list):
        raise ValueError("prompt file must be a list")

    validated = []

    for item in data:
        try:
            prompt = Prompt.model_validate(item)
            validated.append(prompt)
        except ValidationError as e:
            print(f"Validation error:\n{e}")
            raise

    return validated