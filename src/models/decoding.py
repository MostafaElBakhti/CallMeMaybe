from .validation import Function
import json
from llm_sdk import Small_LLM_Model



def load_vocabulary(model: Small_LLM_Model):
    """Load the vocabulary from the tokenizer file.
    
    Args:
        model: The loaded Small_LLM_Model instance.
    
    Returns:
        A dictionary mapping token_id (int) -> token_string (str).
    """
    vocab_path = model.get_path_to_tokenizer_file()
    try : 
        with open(vocab_path , "r", encoding="utf-8") as f:
            tokenizer_data = json.load(f)
        vocab = tokenizer_data.get("model", {}).get("vocab", {})
    except OSError as e:
        raise RuntimeError(f"Failed to read tokenizer file: {e}")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in tokenizer file: {e}")
    
    id_to_token = {token_id: token_str for token_str, token_id in vocab.items()}
    return id_to_token


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
