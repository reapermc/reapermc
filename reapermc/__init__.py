__version__ = "0.1.1"


from beet import Context
from beet.contrib.load import load
from bolt import bolt


def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={"data/reapermc/modules": "@reapermc/modules"},
        ),
        bolt(entrypoint="*:main"),
        "bolt_expressions.plugin",
    )
