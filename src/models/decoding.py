from .validation import Function
import json
from llm_sdk import Small_LLM_Model



def load_vocabulary(model: Small_LLM_Model):
    vocab_path = model.get_path_to_tokenizer_file()


def system_prompt_builder(functions: list[Function]) -> str:
    header = """You are an AI assistant that selects the correct function to call.

            You must ONLY return a JSON object.
            Do not explain anything.

            Rules:
            - Use ONLY the provided functions
            - Use exact function names
            - Use exact parameter names
            - Do not add extra fields
            - If no function matches, return:
            - Never use an unrelated function for a different task
            {"function": null, "arguments": {}}

            Format:
            {
            "function": "<function_name>",
            "arguments": { ... }
            }

            Available functions:
            """
    functions_str = ""
    for fn in functions:
        functions_str += f"\nFunction name: {fn.name}\n"
        functions_str += f"Description: {fn.description}\n"
        functions_str += f"Parameters:\n"

        for name, param in fn.parameters.items():
            functions_str += f"\t- {name} ({param.type})\n"

    return header + functions_str
