# linter/rules/print_rule.py
import ast
from .base_rule import BaseRule

class PrintRule(BaseRule):
    name = "PrintRule"

    def check(self, tree: ast.AST, filename: str) -> list:
        problem = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == "print":
                    problem.append({
                        "filename": filename,
                        "lineno": node.lineno,
                        "message": "Uso de print() encontrado."
                    })
        return problem
