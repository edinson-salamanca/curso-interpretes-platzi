from enum import (
    auto,
    Enum,
    unique
)
from typing import (
    Dict,
    NamedTuple
)


@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    DIVISION = auto()
    EOF = auto()
    ELSE = auto()
    FUNCTION = auto()
    FALSE = auto()
    GT = auto()
    IDENT = auto()
    ILLEGAL = auto()
    INT = auto()
    IF = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    LT = auto()
    MINUS = auto()
    MULTIPLICATION = auto()
    NEGATION = auto()
    PLUS = auto()
    RPAREN = auto()
    RBRACE = auto()
    RETURN = auto()
    SEMICOLON = auto()
    TRUE = auto()


class Token (NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'


def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'falso': TokenType.FALSE,
        'procedimiento': TokenType.FUNCTION,
        'regresa': TokenType.RETURN,
        'si': TokenType.IF,
        'si_no': TokenType.ELSE,
        'variable': TokenType.LET,
        'verdadero': TokenType.TRUE
    }

    return keywords.get(literal, TokenType.IDENT)
