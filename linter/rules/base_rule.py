# linter/rules/base_rule.py
import ast

class BaseRule:
    name = "BaseRule"

    def check(self, tree: ast.AST, filename: str) -> list:
        raise NotImplementedError("All rules must implement the check method.")
