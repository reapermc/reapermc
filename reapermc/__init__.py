__version__ = "1.0.2"


from beet import Context
from beet.contrib.load import load
from bolt import bolt


def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={"data/reapermc/modules": "@reapermc/modules"},
        ),
        bolt(entrypoint=["*:main", "reapermc:core"]),
        "bolt_expressions.plugin",
        "reapermc.plugins.nbt_literals",
    )
