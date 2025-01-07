# linter/rules/print_rule.py
from .base_rule import BaseRule

class PrintRule(BaseRule):
    name = "ConsoleLogRule"

    def check(self, tree, filename: str) -> list:
        problems = []
        for node in tree.body:
            self._traverse(node, filename, problems)
        return problems

    def _traverse(self, node, filename, problems):
        if self._is_console_log(node):
            problems.append({
                "filename": filename,
                "lineno": node.loc.start.line,
                "col_offset": node.loc.start.column + 1,
                "end_col_offset": node.loc.end.column + 1,
                "message": "Usage of console.log() found."
            })

        if node.type == "BlockStatement" or hasattr(node, "__dict__"):
            for _, value in node.__dict__.items():
                if isinstance(value, list):
                    for child in value:
                        if hasattr(child, "type"):
                            self._traverse(child, filename, problems)
                elif hasattr(value, "type"):
                    self._traverse(value, filename, problems)

    def _is_console_log(self, node):
        if node.type == "ExpressionStatement" and node.expression.type == "CallExpression":
            callee = node.expression.callee
            return (
                callee.type == "MemberExpression" and
                callee.object.type == "Identifier" and callee.object.name == "console" and
                callee.property.type == "Identifier" and callee.property.name == "log"
            )
        return False
