"""Utility functions for file input/output operations."""


def read_text_file(file_path):
    """Read the content of a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_json_file(file_path):
    """Read the content of a JSON file."""
    import json

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
