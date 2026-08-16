from core.kernel.i34_core import I34Core
from modules.system.system_module import SystemModule
from modules.intent.intent_module import IntentModule


core = I34Core()

core.register_module("system", SystemModule())
core.register_module("intent", IntentModule())


system_result = core.call_module(
    "system",
    {
        "action": "status"
    }
)

intent_result = core.call_module(
    "intent",
    {
        "text": "Salom I34"
    }
)

print("SYSTEM:")
print(system_result)

print("INTENT:")
print(intent_result)
