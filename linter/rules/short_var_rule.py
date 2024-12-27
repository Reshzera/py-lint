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
                        "lineno": node.lineno,
                        "col_offset": node.col_offset + 1,
                        "end_col_offset": node.end_col_offset + 1,
                        "message": f"Too short variable name: '{node.id}'"
                    })
        return problem
