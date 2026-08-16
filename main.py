from core.kernel.i34_core import I34Core
from modules.system.system_module import SystemModule


core = I34Core()

system = SystemModule()

core.register_module("system", system)

result = core.call_module(
    "system",
    {
        "action": "status"
    }
)

print(result)
