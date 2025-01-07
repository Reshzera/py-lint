import esprima 
from typing import List
from linter.rules import PrintRule, RedeclareWithoutLetRule

def get_all_rules():
    return [
        PrintRule(),
        RedeclareWithoutLetRule(),
    ]

def check_file(filename: str) -> List[dict]:
    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    tree = esprima.parseScript(source, loc=True)

    rules = get_all_rules()

    all_problems = []
    for rule in rules:
        problems = rule.check(tree, filename)
        all_problems.extend(problems)

    return all_problems
