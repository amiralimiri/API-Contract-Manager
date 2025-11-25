import json

from deepdiff import DeepDiff

# NOTE: deepdiff not in pyproject; if you want to use it add to deps or implement simple diff


def json_diff(a: dict, b: dict) -> str:
    dd = DeepDiff(a, b, ignore_order=True)
    return dd.pretty()
