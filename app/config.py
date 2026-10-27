import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"


def load_config():
    """Load and validate application configuration."""
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as file:
            config = json.load(file)
    except FileNotFoundError as exc:
        raise RuntimeError("Configuration file is missing.") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError("Configuration file contains invalid JSON.") from exc

    max_length = config.get("max_text_length")

    if not isinstance(max_length, int) or isinstance(max_length, bool) or max_length <= 0:
        raise ValueError("max_text_length must be a positive integer.")

    if not isinstance(config.get("show_word_list"), bool):
        raise ValueError("show_word_list must be true or false.")

    return config