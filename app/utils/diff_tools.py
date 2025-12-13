import json

from deepdiff import DeepDiff


def json_diff(a: dict, b: dict) -> str:
    diff = DeepDiff(a, b, ignore_order=True)
    if not diff:
        return "No differences"
    return diff.pretty()
