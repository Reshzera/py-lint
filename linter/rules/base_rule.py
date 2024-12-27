# linter/rules/base_rule.py
import ast

class BaseRule:
    """
    Classe base para todas as regras do linter.
    Cada regra deve ter um método 'check' que recebe a AST do arquivo
    e retorna uma lista de mensagens de aviso/erro.
    """
    name = "BaseRule"

    def check(self, tree: ast.AST, filename: str) -> list:
        """
        Deve retornar uma lista de dicionários (ou strings) com as informações
        sobre os problemas encontrados.
        Exemplo de retorno:
        [
            {
                "filename": "arquivo.py",
                "lineno": 10,
                "message": "Descrição do problema"
            },
            ...
        ]
        """
        raise NotImplementedError("As subclasses devem implementar este método.")
