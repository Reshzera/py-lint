# linter/rules/base_rule.py
import esprima

class BaseRule:
    name = "BaseRule"

    def check(self, tree: esprima.nodes.Module, filename: str) -> list:
        raise NotImplementedError("All rules must implement the check method.")
