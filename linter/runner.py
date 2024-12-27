import ast
from typing import List
from linter.rules import PrintRule, ShortVarRule


def get_all_rules():
    return [
        PrintRule(),
        ShortVarRule()
    ]

def check_file(filename: str) -> List[dict]:
    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source, filename=filename)

    rules = get_all_rules()

    all_problems = []
    for rule in rules:
        problems = rule.check(tree, filename)
        all_problems.extend(problems)

    return all_problems
