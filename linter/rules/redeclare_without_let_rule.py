from .base_rule import BaseRule

class RedeclareWithoutLetRule(BaseRule):
    name = "RedeclareWithoutLetRule"

    def check(self, tree, filename: str) -> list:
        problems = []
        declared_vars = set() 

        for node in tree.body:
            self._traverse(node, declared_vars, filename, problems)

        return problems

    def _traverse(self, node, declared_vars, filename, problems):
        if node.type == "VariableDeclaration":
            for declaration in node.declarations:
                declared_vars.add(declaration.id.name)
        elif node.type == "AssignmentExpression":
            if node.left.type == "Identifier":
                var_name = node.left.name
                if var_name not in declared_vars:
                    problems.append({
                        "message": f"Variable '{var_name}' assigned without prior declaration.",
                        "filename": filename,
                        "lineno": node.loc.start.line,
                        "col_offset": node.loc.start.column + 1,
                        "end_col_offset": node.loc.end.column + 1,
                    })
        elif node.type == "BlockStatement":
            new_declared_vars = declared_vars.copy()
            for child in node.body:
                self._traverse(child, new_declared_vars, filename, problems)
        elif hasattr(node, "body") and isinstance(node.body, list):
            for child in node.body:
                self._traverse(child, declared_vars, filename, problems)
        elif hasattr(node, "__dict__"):
            for attr in node.__dict__.values():
                if isinstance(attr, list):
                    for child in attr:
                        if hasattr(child, "type"):
                            self._traverse(child, declared_vars, filename, problems)
                elif hasattr(attr, "type"):
                    self._traverse(attr, declared_vars, filename, problems)
