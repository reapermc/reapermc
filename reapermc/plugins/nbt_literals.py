from dataclasses import dataclass, field
from typing import Dict, Type, Any
from beet import Context
from beet.core.utils import required_field
from bolt import Accumulator, Runtime
from bolt.utils import internal
from mecha import AstNode, Mecha, Parser, Reducer, rule
from tokenstream import TokenStream, set_location
from nbtlib import Numeric, Byte, Short, Long, Float, Double
import operator

SUFFIXED_NUMBER = r"[+-]?(?:[0-9]*?\.[0-9]+|[0-9]+\.[0-9]*?|[1-9][0-9]*|0)(?:[eE][+-]?[0-9]+)?[bslfdBSLFD]\b"


# nbtlib monkey patch :)
def patch_nbtlib():
    def op_method(op: Any, reverse: Any = False):
        def method(self: Any, other: Any):
            value = op(other.real, self.real) if reverse else op(self.real, other.real)
            return self.__class__(value)

        return method

    Numeric.__add__ = op_method(operator.add)
    Numeric.__radd__ = op_method(operator.add, reverse=True)
    Numeric.__sub__ = op_method(operator.sub)
    Numeric.__rsub__ = op_method(operator.sub, reverse=True)
    Numeric.__mul__ = op_method(operator.mul)
    Numeric.__rmul__ = op_method(operator.mul, reverse=True)
    Numeric.__truediv__ = op_method(operator.truediv)
    Numeric.__rtruediv__ = op_method(operator.truediv, reverse=True)


def beet_default(ctx: Context):
    ctx.inject(nbt_literals)


def nbt_literals(ctx: Context):
    patch_nbtlib()

    mc = ctx.inject(Mecha)
    runtime = ctx.inject(Runtime)

    runtime.globals.update(
        {"Byte": Byte, "Short": Short, "Long": Long, "Float": Float, "Double": Double}
    )

    mc.spec.parsers["bolt:literal"] = NbtLiteralParser(
        parser=mc.spec.parsers["bolt:literal"]
    )

    runtime.modules.codegen.extend(NbtLiteralCodegen())

    runtime.helpers["nbt_literal"] = NbtLiteralConverter()


@dataclass(frozen=True)
class AstNbtLiteral(AstNode):
    value: float = required_field()
    suffix: str = required_field()


@dataclass
class NbtLiteralParser:
    parser: Parser

    def __call__(self, stream: TokenStream):
        with stream.syntax(nbt_literal=SUFFIXED_NUMBER):
            number = stream.get("nbt_literal")

            if not number:
                return self.parser(stream)

            value = float(number.value[:-1])
            suffix = number.value[-1].lower()

            node = AstNbtLiteral(value=value, suffix=suffix)

            return set_location(node, stream.current)


class NbtLiteralCodegen(Reducer):
    @rule(AstNbtLiteral)
    def nbt_literal(self, node: AstNbtLiteral, acc: Accumulator):
        result = acc.make_variable()
        rhs = acc.helper("nbt_literal", node.value, repr(node.suffix))

        acc.statement(f"{result} = {rhs}")

        return [result]


@dataclass
class NbtLiteralConverter:
    number_suffixes: Dict[str, Type[Numeric]] = field(
        default_factory=lambda: {
            "b": Byte,
            "s": Short,
            "l": Long,
            "f": Float,
            "d": Double,
        }
    )

    @internal
    def __call__(self, value: float, suffix: str):
        type = self.number_suffixes.get(suffix)

        if type is None:
            return value

        return type(value)
