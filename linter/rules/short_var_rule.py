# linter/rules/short_var_rule.py
import ast
from .base_rule import BaseRule

class ShortVarRule(BaseRule):
    name = "ShortVarRule"

    def check(self, tree: ast.AST, filename: str) -> list:
        problem = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if len(node.id) == 1 and node.id.isalpha():
                    problem.append({
                        "filename": filename,
                        "lineno": getattr(node, 'lineno', 0),
                        "message": f"Nome de variável muito curto: '{node.id}'"
                    })
        return problem
